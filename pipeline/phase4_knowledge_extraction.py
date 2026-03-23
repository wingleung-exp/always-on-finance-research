#!/usr/bin/env python3
"""Extract structured knowledge entries from panel synthesis.

Reads phase3/panel_synthesis.md and uses Claude to extract structured JSON,
then writes output files to phase4/.

Usage:
    python3 phase4_knowledge_extraction.py \
        --iter-dir /path/to/outputs/iteration_42 \
        --topic monetary_policy \
        --topic-category macro_frameworks \
        --iteration-id iteration_42
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


def log(msg: str, log_file: str = "") -> None:
    """Print a timestamped log message to stderr and optionally a file."""
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    line = f"[{ts}] [phase4] {msg}"
    print(line, file=sys.stderr)
    if log_file:
        try:
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(line + "\n")
        except OSError:
            pass


def run_claude(prompt_text: str) -> str:
    """Pipe prompt_text to claude --print and return stdout."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False,
                                      encoding="utf-8") as tmp:
        tmp.write(prompt_text)
        tmp_path = tmp.name

    try:
        result = subprocess.run(
            ["claude", "--print", "--no-session-persistence",
             "--setting-sources", "project,local",
             "--dangerously-skip-permissions", "--effort", "max"],
            stdin=open(tmp_path, "r", encoding="utf-8"),
            capture_output=True,
            text=True,
        )
        return result.stdout
    except FileNotFoundError:
        log("ERROR: claude CLI not found in PATH")
        return ""
    finally:
        os.unlink(tmp_path)


def extract_json_block(text: str) -> str:
    """Extract JSON from Claude output, handling optional ```json fences."""
    # Try to find a fenced JSON block first
    import re
    match = re.search(r"```(?:json)?\s*\n([\s\S]*?)\n```", text)
    if match:
        return match.group(1).strip()

    # Try to find raw JSON (starts with { or [)
    for line_idx, line in enumerate(text.split("\n")):
        stripped = line.strip()
        if stripped.startswith("{") or stripped.startswith("["):
            # Grab from here to end
            candidate = "\n".join(text.split("\n")[line_idx:])
            # Find the matching close
            depth = 0
            close_char = "}" if stripped.startswith("{") else "]"
            open_char = "{" if stripped.startswith("{") else "["
            for i, ch in enumerate(candidate):
                if ch == open_char:
                    depth += 1
                elif ch == close_char:
                    depth -= 1
                    if depth == 0:
                        return candidate[: i + 1]
            return candidate

    return text.strip()


def build_extraction_prompt(synthesis_text: str, topic: str,
                            topic_category: str, iteration_id: str) -> str:
    """Build the prompt for Claude to extract structured knowledge."""
    # Use a temp file to hold the synthesis, read it back for prompt assembly
    prompt_parts = []

    prompt_parts.append(
        "You are a knowledge extraction system. Read the following panel "
        "synthesis from a multi-agent finance research iteration and extract "
        "structured data.\n\n"
    )
    prompt_parts.append(f"Topic: {topic}\n")
    prompt_parts.append(f"Category: {topic_category}\n")
    prompt_parts.append(f"Iteration: {iteration_id}\n\n")
    prompt_parts.append("=== PANEL SYNTHESIS ===\n\n")
    prompt_parts.append(synthesis_text)
    prompt_parts.append("\n\n=== EXTRACTION INSTRUCTIONS ===\n\n")
    prompt_parts.append(
        'Output a single JSON object with exactly these keys:\n'
        '"concepts", "relationships", "frameworks", "provenance", '
        '"anti_knowledge", "low_confidence"\n\n'
    )
    prompt_parts.append(
        '"concepts": array of objects, each with:\n'
        '  - "slug": lowercase_underscored identifier\n'
        '  - "definition": clear 1-3 sentence definition\n'
        '  - "confidence": number 1-10\n'
        '  - "evidence": array of evidence strings\n'
        '  - "originating_agents": array of agent role_id strings\n'
        '  - "open_questions": array of question strings\n'
        '  - "related_concepts": array of concept slug strings\n\n'
    )
    prompt_parts.append(
        '"relationships": array of objects, each with:\n'
        '  - "concept_a": slug of first concept\n'
        '  - "concept_b": slug of second concept\n'
        '  - "mechanism": how they relate\n'
        '  - "direction": "a_causes_b", "b_causes_a", "bidirectional", or "correlated"\n'
        '  - "confidence": number 1-10\n'
        '  - "regime_dependence": description of when this relationship holds\n'
        '  - "originating_agents": array of agent role_id strings\n\n'
    )
    prompt_parts.append(
        '"frameworks": array of objects, each with:\n'
        '  - "slug": lowercase_underscored identifier\n'
        '  - "purpose": what question this framework answers\n'
        '  - "components": array of component descriptions\n'
        '  - "current_assessment": current state assessment\n'
        '  - "limitations": array of known limitation strings\n\n'
    )
    prompt_parts.append(
        '"provenance": object mapping agent role_id to:\n'
        '  - "claims_made": integer count of claims the agent made\n'
        '  - "claims_survived": integer count of claims that survived to synthesis\n\n'
    )
    prompt_parts.append(
        '"anti_knowledge": array of objects, each with:\n'
        '  - "claim": the refuted claim\n'
        '  - "reason": why it was refuted\n'
        '  - "refuted_by": array of agent role_ids that contributed to refutation\n\n'
    )
    prompt_parts.append(
        '"low_confidence": array of objects, each with:\n'
        '  - "claim": the low-confidence claim\n'
        '  - "source_agent": the agent role_id that made it\n'
        '  - "needs": what would be needed to corroborate\n\n'
    )
    prompt_parts.append(
        "IMPORTANT: Output ONLY valid JSON. No markdown fences, no commentary "
        "before or after. Just the JSON object.\n"
    )

    return "".join(prompt_parts)


def write_json(path: str, data) -> None:
    """Write data as formatted JSON to path."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract structured knowledge from panel synthesis."
    )
    parser.add_argument("--iter-dir", required=True,
                        help="Iteration output directory.")
    parser.add_argument("--topic", required=True, help="Topic slug.")
    parser.add_argument("--topic-category", required=True,
                        help="Topic category.")
    parser.add_argument("--iteration-id", required=True,
                        help="Iteration identifier.")
    parser.add_argument("--log-file", default="",
                        help="Optional log file path.")

    args = parser.parse_args()

    iter_dir = args.iter_dir
    phase3_dir = os.path.join(iter_dir, "phase3")
    phase4_dir = os.path.join(iter_dir, "phase4")
    os.makedirs(phase4_dir, exist_ok=True)

    synthesis_path = os.path.join(phase3_dir, "panel_synthesis.md")
    log_file = args.log_file or os.environ.get("LOG_FILE", "")

    # Read synthesis
    if not os.path.isfile(synthesis_path):
        log(f"ERROR: Synthesis file not found: {synthesis_path}", log_file)
        sys.exit(1)

    with open(synthesis_path, "r", encoding="utf-8") as f:
        synthesis_text = f.read()

    if not synthesis_text.strip():
        log("ERROR: Synthesis file is empty", log_file)
        sys.exit(1)

    log(f"Read synthesis: {len(synthesis_text)} bytes", log_file)

    # Build extraction prompt
    prompt = build_extraction_prompt(
        synthesis_text=synthesis_text,
        topic=args.topic,
        topic_category=args.topic_category,
        iteration_id=args.iteration_id,
    )

    log("Running Claude for knowledge extraction...", log_file)
    raw_output = run_claude(prompt)

    if not raw_output.strip():
        log("ERROR: Claude returned empty output for extraction", log_file)
        sys.exit(1)

    log(f"Claude output: {len(raw_output)} bytes", log_file)

    # Parse JSON from output
    json_str = extract_json_block(raw_output)

    try:
        extracted = json.loads(json_str)
    except json.JSONDecodeError as e:
        log(f"ERROR: Failed to parse extraction JSON: {e}", log_file)
        log(f"Raw JSON string (first 500 chars): {json_str[:500]}", log_file)
        # Write raw output for debugging
        debug_path = os.path.join(phase4_dir, "extraction_raw_debug.txt")
        with open(debug_path, "w", encoding="utf-8") as f:
            f.write(raw_output)
        sys.exit(1)

    # Add metadata to each section
    metadata = {
        "topic": args.topic,
        "topic_category": args.topic_category,
        "iteration_id": args.iteration_id,
        "extracted_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    # Write output files
    concepts = extracted.get("concepts", [])
    for concept in concepts:
        concept.setdefault("topic", args.topic)
        concept.setdefault("iteration_id", args.iteration_id)
    write_json(os.path.join(phase4_dir, "concepts.json"), concepts)
    log(f"Wrote {len(concepts)} concepts", log_file)

    relationships = extracted.get("relationships", [])
    for rel in relationships:
        rel.setdefault("topic", args.topic)
        rel.setdefault("iteration_id", args.iteration_id)
    write_json(os.path.join(phase4_dir, "relationships.json"), relationships)
    log(f"Wrote {len(relationships)} relationships", log_file)

    frameworks = extracted.get("frameworks", [])
    for fw in frameworks:
        fw.setdefault("topic", args.topic)
        fw.setdefault("iteration_id", args.iteration_id)
    write_json(os.path.join(phase4_dir, "frameworks.json"), frameworks)
    log(f"Wrote {len(frameworks)} frameworks", log_file)

    # Provenance: reformat for scoring system
    raw_provenance = extracted.get("provenance", {})
    provenance = {"agent_contributions": {}, "metadata": metadata}
    for role_id, data in raw_provenance.items():
        if isinstance(data, dict):
            provenance["agent_contributions"][role_id] = {
                "claims_made": data.get("claims_made", 0),
                "claims_survived": data.get("claims_survived", 0),
            }
        elif isinstance(data, (list, tuple)) and len(data) >= 2:
            provenance["agent_contributions"][role_id] = {
                "claims_made": data[0],
                "claims_survived": data[1],
            }
    write_json(os.path.join(phase4_dir, "provenance.json"), provenance)
    log(f"Wrote provenance for {len(provenance['agent_contributions'])} agents",
        log_file)

    anti_knowledge = extracted.get("anti_knowledge", [])
    for ak in anti_knowledge:
        ak.setdefault("topic", args.topic)
        ak.setdefault("iteration_id", args.iteration_id)
    write_json(os.path.join(phase4_dir, "anti_knowledge.json"), anti_knowledge)
    log(f"Wrote {len(anti_knowledge)} anti-knowledge entries", log_file)

    low_confidence = extracted.get("low_confidence", [])
    for lc in low_confidence:
        lc.setdefault("topic", args.topic)
        lc.setdefault("iteration_id", args.iteration_id)
    write_json(os.path.join(phase4_dir, "low_confidence.json"), low_confidence)
    log(f"Wrote {len(low_confidence)} low-confidence entries", log_file)

    log("Phase 4 extraction complete", log_file)


if __name__ == "__main__":
    main()
