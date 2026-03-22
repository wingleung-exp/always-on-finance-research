#!/usr/bin/env python3
"""Update agent scores and topic registry after a completed iteration.

Reads provenance from phase4/provenance.json, calls scoring/update_scores.py,
and updates topic_registry.json with new depth, confidence, gaps, and connections.

Usage:
    python3 phase6_score_update.py \
        --phase4-dir /path/to/outputs/iteration_42/phase4 \
        --base-dir /path/to/finance_research \
        --topic monetary_policy \
        --topic-category macro_frameworks \
        --iteration-id iteration_42
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def log(msg: str, log_file: str = "") -> None:
    """Print a timestamped log message to stderr and optionally a file."""
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    line = f"[{ts}] [phase6] {msg}"
    print(line, file=sys.stderr)
    if log_file:
        try:
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(line + "\n")
        except OSError:
            pass


def load_json(path: str) -> dict | list | None:
    """Load JSON from path, returning None if missing or invalid."""
    if not os.path.isfile(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None


def save_json(path: str, data) -> None:
    """Write data as formatted JSON."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def run_score_update(base_dir: str, provenance_path: str,
                     topic_category: str, iteration_id: str,
                     log_file: str) -> bool:
    """Call scoring/update_scores.py and return True on success."""
    scores_path = os.path.join(base_dir, "scoring", "agent_scores.json")

    # Create agent_scores.json if it doesn't exist yet
    if not os.path.isfile(scores_path):
        save_json(scores_path, {"version": 1, "scores": {}})
        log(f"Created initial agent_scores.json at {scores_path}", log_file)

    update_script = os.path.join(base_dir, "scoring", "update_scores.py")

    if not os.path.isfile(update_script):
        log(f"WARNING: update_scores.py not found at {update_script}", log_file)
        return False

    cmd = [
        sys.executable, update_script,
        "--scores", scores_path,
        "--provenance", provenance_path,
        "--topic-category", topic_category,
        "--iteration-id", iteration_id,
    ]

    log(f"Running: {' '.join(cmd)}", log_file)

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode == 0:
            log(f"Score update succeeded:\n{result.stdout.strip()}", log_file)
            return True
        else:
            log(f"Score update failed (exit {result.returncode}):\n"
                f"{result.stderr.strip()}", log_file)
            return False
    except subprocess.TimeoutExpired:
        log("Score update timed out", log_file)
        return False
    except OSError as e:
        log(f"Score update OS error: {e}", log_file)
        return False


def update_topic_registry(base_dir: str, topic: str, topic_category: str,
                          iteration_id: str, phase4_dir: str,
                          log_file: str) -> bool:
    """Update topic_registry.json with results from this iteration."""
    registry_path = os.path.join(base_dir, "topic_registry",
                                 "topic_registry.json")

    registry = load_json(registry_path)
    if registry is None:
        log(f"WARNING: topic_registry.json not found at {registry_path}",
            log_file)
        return False

    topics = registry.get("topics", {})
    if topic not in topics:
        log(f"WARNING: topic '{topic}' not in registry", log_file)
        return False

    topic_data = topics[topic]

    # --- Increment depth level ---
    old_depth = topic_data.get("depth_level", 0)
    topic_data["depth_level"] = old_depth + 1
    log(f"Topic depth: {old_depth} -> {topic_data['depth_level']}", log_file)

    # --- Increment research count ---
    topic_data["research_count"] = topic_data.get("research_count", 0) + 1

    # --- Update last_researched ---
    topic_data["last_researched"] = datetime.now(timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )

    # --- Update confidence from concepts ---
    concepts = load_json(os.path.join(phase4_dir, "concepts.json"))
    if concepts and isinstance(concepts, list):
        confidences = [c.get("confidence", 0) for c in concepts
                       if isinstance(c.get("confidence", 0), (int, float))]
        if confidences:
            avg_confidence = sum(confidences) / len(confidences)
            old_confidence = topic_data.get("confidence_score", 5.0)
            old_count = topic_data.get("research_count", 1) - 1
            if old_count > 0:
                # Weighted average with history
                new_confidence = round(
                    (old_confidence * old_count + avg_confidence) /
                    (old_count + 1), 1
                )
            else:
                new_confidence = round(avg_confidence, 1)
            topic_data["confidence_score"] = new_confidence
            log(f"Topic confidence: {old_confidence} -> {new_confidence}",
                log_file)

    # --- Merge new gaps from low-confidence items ---
    low_confidence = load_json(os.path.join(phase4_dir, "low_confidence.json"))
    if low_confidence and isinstance(low_confidence, list):
        existing_gaps = set(topic_data.get("knowledge_gaps", []))
        new_gaps = []
        for lc in low_confidence:
            claim = lc.get("claim", "") or lc.get("needs", "")
            if claim and claim not in existing_gaps:
                new_gaps.append(claim)
                existing_gaps.add(claim)
        if new_gaps:
            topic_data["knowledge_gaps"] = list(existing_gaps)
            log(f"Added {len(new_gaps)} new knowledge gaps", log_file)

    # --- Remove gaps that have been answered (high confidence concepts) ---
    if concepts and isinstance(concepts, list):
        high_conf_slugs = set()
        high_conf_defs = set()
        for c in concepts:
            if c.get("confidence", 0) >= 7:
                high_conf_slugs.add(c.get("slug", ""))
                high_conf_defs.add(c.get("definition", "").lower())

        if high_conf_slugs:
            old_gaps = topic_data.get("knowledge_gaps", [])
            remaining_gaps = []
            closed = 0
            for gap in old_gaps:
                gap_lower = gap.lower()
                # Check if any high-confidence concept addresses this gap
                addressed = False
                for slug in high_conf_slugs:
                    if slug.replace("_", " ") in gap_lower:
                        addressed = True
                        break
                if not addressed:
                    remaining_gaps.append(gap)
                else:
                    closed += 1
            if closed > 0:
                topic_data["knowledge_gaps"] = remaining_gaps
                log(f"Closed {closed} knowledge gaps via high-confidence "
                    f"concepts", log_file)

    # --- Merge new connections from relationships ---
    relationships = load_json(os.path.join(phase4_dir, "relationships.json"))
    if relationships and isinstance(relationships, list):
        existing_connections = set(topic_data.get("connections", []))
        new_connections = []
        all_topic_ids = set(topics.keys())

        for rel in relationships:
            for concept_key in ["concept_a", "concept_b"]:
                concept = rel.get(concept_key, "")
                # Check if concept matches a known topic ID
                if concept in all_topic_ids and concept != topic:
                    if concept not in existing_connections:
                        new_connections.append(concept)
                        existing_connections.add(concept)

        if new_connections:
            topic_data["connections"] = list(existing_connections)
            log(f"Added {len(new_connections)} new topic connections",
                log_file)

    # --- Update key_concepts from extracted concepts ---
    if concepts and isinstance(concepts, list):
        existing_key_concepts = set(topic_data.get("key_concepts", []))
        for c in concepts:
            slug = c.get("slug", "")
            if slug and c.get("confidence", 0) >= 6:
                existing_key_concepts.add(slug)
        topic_data["key_concepts"] = sorted(existing_key_concepts)

    # --- Save registry ---
    registry["last_updated"] = datetime.now(timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    save_json(registry_path, registry)
    log(f"Topic registry updated for '{topic}'", log_file)
    return True


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Update agent scores and topic registry after iteration."
    )
    parser.add_argument("--phase4-dir", required=True,
                        help="Phase 4 output directory.")
    parser.add_argument("--base-dir", required=True,
                        help="Finance research base directory.")
    parser.add_argument("--topic", required=True, help="Topic slug.")
    parser.add_argument("--topic-category", required=True,
                        help="Topic category.")
    parser.add_argument("--iteration-id", required=True,
                        help="Iteration identifier.")
    parser.add_argument("--log-file", default="",
                        help="Optional log file path.")

    args = parser.parse_args()
    log_file = args.log_file or os.environ.get("LOG_FILE", "")

    log("Starting phase 6: score update and registry update", log_file)

    provenance_path = os.path.join(args.phase4_dir, "provenance.json")

    # --- Step 1: Check provenance exists ---
    if not os.path.isfile(provenance_path):
        log(f"ERROR: provenance.json not found at {provenance_path}", log_file)
        sys.exit(1)

    provenance = load_json(provenance_path)
    if provenance is None:
        log("ERROR: provenance.json is invalid JSON", log_file)
        sys.exit(1)

    agent_contributions = provenance.get("agent_contributions", {})
    log(f"Loaded provenance for {len(agent_contributions)} agents", log_file)

    # --- Step 2: Call scoring/update_scores.py ---
    score_ok = run_score_update(
        base_dir=args.base_dir,
        provenance_path=provenance_path,
        topic_category=args.topic_category,
        iteration_id=args.iteration_id,
        log_file=log_file,
    )
    if score_ok:
        log("Agent score update: SUCCESS", log_file)
    else:
        log("Agent score update: FAILED (non-fatal, continuing)", log_file)

    # --- Step 3: Update topic registry ---
    registry_ok = update_topic_registry(
        base_dir=args.base_dir,
        topic=args.topic,
        topic_category=args.topic_category,
        iteration_id=args.iteration_id,
        phase4_dir=args.phase4_dir,
        log_file=log_file,
    )
    if registry_ok:
        log("Topic registry update: SUCCESS", log_file)
    else:
        log("Topic registry update: FAILED (non-fatal)", log_file)

    log("Phase 6 complete", log_file)


if __name__ == "__main__":
    main()
