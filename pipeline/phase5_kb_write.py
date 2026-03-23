#!/usr/bin/env python3
"""Write extracted knowledge entries to the KB directory.

Reads from phase4/ output files, writes to knowledge_base/.
Handles merge-or-create logic for concepts, relationships, and frameworks.

Usage:
    python3 phase5_kb_write.py \
        --phase4-dir /path/to/outputs/iteration_42/phase4 \
        --kb-dir /path/to/knowledge_base \
        --iteration-id iteration_42 \
        --topic monetary_policy \
        --topic-category macro_frameworks
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path


def log(msg: str, log_file: str = "") -> None:
    """Print a timestamped log message to stderr and optionally a file."""
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    line = f"[{ts}] [phase5] {msg}"
    print(line, file=sys.stderr)
    if log_file:
        try:
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(line + "\n")
        except OSError:
            pass


def load_json(path: str) -> list | dict | None:
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


def weighted_avg(old_val: float, old_weight: int,
                 new_val: float, new_weight: int = 1) -> float:
    """Compute weighted average of old and new values."""
    total_weight = old_weight + new_weight
    if total_weight == 0:
        return new_val
    return round((old_val * old_weight + new_val * new_weight) / total_weight, 2)


MAX_EVIDENCE = 10  # Cap evidence arrays to prevent unbounded growth
MAX_OPEN_QUESTIONS = 8


def merge_unique(existing: list, new_items: list,
                 max_items: int = 0) -> list:
    """Merge two lists, deduplicating by string equality.
    If max_items > 0, keep only the most recent max_items entries."""
    combined = list(existing)
    existing_set = set(str(item) for item in existing)
    for item in new_items:
        if str(item) not in existing_set:
            combined.append(item)
            existing_set.add(str(item))
    if max_items > 0 and len(combined) > max_items:
        combined = combined[-max_items:]
    return combined


def slug_token_overlap(slug_a: str, slug_b: str) -> float:
    """Compute token overlap ratio between two slugs."""
    tokens_a = set(slug_a.lower().split("_"))
    tokens_b = set(slug_b.lower().split("_"))
    if not tokens_a or not tokens_b:
        return 0.0
    intersection = tokens_a & tokens_b
    return len(intersection) / min(len(tokens_a), len(tokens_b))


def check_dedup(slug: str, topic: str, concepts_dir: str,
                log_file: str) -> str | None:
    """Check if a new concept slug might be a duplicate of an existing one.
    Returns the existing slug if overlap > 60%, else None."""
    for fname in os.listdir(concepts_dir):
        if not fname.endswith(".json"):
            continue
        existing_slug = fname[:-5]
        if existing_slug == slug:
            continue  # same slug = merge, not dedup issue
        # Only check within same topic for speed
        existing_data = load_json(os.path.join(concepts_dir, fname))
        if existing_data and existing_data.get("topic") == topic:
            overlap = slug_token_overlap(slug, existing_slug)
            if overlap >= 0.6:
                log(f"DEDUP WARNING: '{slug}' has {overlap:.0%} token overlap "
                    f"with existing '{existing_slug}' (same topic: {topic})",
                    log_file)
                return existing_slug
    return None


# ---------------------------------------------------------------------------
# Concept merge/create
# ---------------------------------------------------------------------------

def write_concepts(concepts: list, kb_dir: str, iteration_id: str,
                   min_confidence: int, log_file: str) -> int:
    """Write concept entries to KB. Returns count of entries written."""
    concepts_dir = os.path.join(kb_dir, "concepts")
    os.makedirs(concepts_dir, exist_ok=True)

    written = 0
    for concept in concepts:
        confidence = concept.get("confidence", 0)
        if confidence < min_confidence:
            continue  # skip to low_confidence handling

        slug = concept.get("slug", "").strip()
        if not slug:
            continue

        concept_path = os.path.join(concepts_dir, f"{slug}.json")
        existing = load_json(concept_path)

        # Dedup check for new concepts
        if existing is None:
            check_dedup(slug, concept.get("topic", ""), concepts_dir, log_file)

        if existing is not None:
            # Merge: update confidence (weighted avg), append evidence, etc.
            old_confidence = existing.get("confidence", 5.0)
            old_iterations = existing.get("research_iterations", 1)
            existing["confidence"] = weighted_avg(
                old_confidence, old_iterations,
                confidence, 1
            )
            existing["evidence"] = merge_unique(
                existing.get("evidence", []),
                concept.get("evidence", []),
                max_items=MAX_EVIDENCE,
            )
            existing["open_questions"] = merge_unique(
                existing.get("open_questions", []),
                concept.get("open_questions", []),
                max_items=MAX_OPEN_QUESTIONS,
            )
            existing["related_concepts"] = merge_unique(
                existing.get("related_concepts", []),
                concept.get("related_concepts", [])
            )
            existing["originating_agents"] = merge_unique(
                existing.get("originating_agents", []),
                concept.get("originating_agents", [])
            )
            existing["research_iterations"] = old_iterations + 1
            existing["last_updated"] = datetime.now(timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            )
            existing.setdefault("iteration_history", []).append(iteration_id)
            save_json(concept_path, existing)
            log(f"Merged concept: {slug} (confidence {old_confidence} -> "
                f"{existing['confidence']})", log_file)
        else:
            # Create new
            new_entry = {
                "slug": slug,
                "definition": concept.get("definition", ""),
                "confidence": confidence,
                "evidence": concept.get("evidence", []),
                "originating_agents": concept.get("originating_agents", []),
                "open_questions": concept.get("open_questions", []),
                "related_concepts": concept.get("related_concepts", []),
                "topic": concept.get("topic", ""),
                "created_at": datetime.now(timezone.utc).strftime(
                    "%Y-%m-%dT%H:%M:%SZ"
                ),
                "last_updated": datetime.now(timezone.utc).strftime(
                    "%Y-%m-%dT%H:%M:%SZ"
                ),
                "originating_iteration": iteration_id,
                "research_iterations": 1,
                "iteration_history": [iteration_id],
            }
            save_json(concept_path, new_entry)
            log(f"Created concept: {slug} (confidence {confidence})", log_file)

        written += 1

    return written


# ---------------------------------------------------------------------------
# Relationship merge/create
# ---------------------------------------------------------------------------

def write_relationships(relationships: list, kb_dir: str, iteration_id: str,
                        min_confidence: int, log_file: str) -> int:
    """Write relationship entries to KB. Returns count written."""
    rels_dir = os.path.join(kb_dir, "relationships")
    os.makedirs(rels_dir, exist_ok=True)

    written = 0
    for rel in relationships:
        confidence = rel.get("confidence", 0)
        if confidence < min_confidence:
            continue

        concept_a = rel.get("concept_a", "").strip()
        concept_b = rel.get("concept_b", "").strip()
        if not concept_a or not concept_b:
            continue

        # Canonical slug: alphabetical order
        sorted_pair = sorted([concept_a, concept_b])
        slug = f"{sorted_pair[0]}__{sorted_pair[1]}"
        rel_path = os.path.join(rels_dir, f"{slug}.json")
        existing = load_json(rel_path)

        if existing is not None:
            old_confidence = existing.get("confidence", 5.0)
            old_iterations = existing.get("research_iterations", 1)
            existing["confidence"] = weighted_avg(
                old_confidence, old_iterations, confidence, 1
            )
            existing["originating_agents"] = merge_unique(
                existing.get("originating_agents", []),
                rel.get("originating_agents", [])
            )
            # Keep the latest mechanism/direction if confidence is higher
            if confidence >= old_confidence:
                existing["mechanism"] = rel.get("mechanism",
                                                existing.get("mechanism", ""))
                existing["direction"] = rel.get("direction",
                                                existing.get("direction", ""))
                existing["regime_dependence"] = rel.get(
                    "regime_dependence",
                    existing.get("regime_dependence", "")
                )
            existing["research_iterations"] = old_iterations + 1
            existing["last_updated"] = datetime.now(timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            )
            existing.setdefault("iteration_history", []).append(iteration_id)
            save_json(rel_path, existing)
            log(f"Merged relationship: {slug}", log_file)
        else:
            new_entry = {
                "concept_a": concept_a,
                "concept_b": concept_b,
                "mechanism": rel.get("mechanism", ""),
                "direction": rel.get("direction", ""),
                "confidence": confidence,
                "regime_dependence": rel.get("regime_dependence", ""),
                "originating_agents": rel.get("originating_agents", []),
                "topic": rel.get("topic", ""),
                "created_at": datetime.now(timezone.utc).strftime(
                    "%Y-%m-%dT%H:%M:%SZ"
                ),
                "last_updated": datetime.now(timezone.utc).strftime(
                    "%Y-%m-%dT%H:%M:%SZ"
                ),
                "originating_iteration": iteration_id,
                "research_iterations": 1,
                "iteration_history": [iteration_id],
            }
            save_json(rel_path, new_entry)
            log(f"Created relationship: {slug}", log_file)

        written += 1

    return written


# ---------------------------------------------------------------------------
# Framework merge/create
# ---------------------------------------------------------------------------

def write_frameworks(frameworks: list, kb_dir: str, iteration_id: str,
                     log_file: str) -> int:
    """Write framework entries to KB. Returns count written."""
    fw_dir = os.path.join(kb_dir, "frameworks")
    os.makedirs(fw_dir, exist_ok=True)

    written = 0
    for fw in frameworks:
        slug = fw.get("slug", "").strip()
        if not slug:
            continue

        fw_path = os.path.join(fw_dir, f"{slug}.json")
        existing = load_json(fw_path)

        if existing is not None:
            # Merge: update components, limitations, assessment
            existing["components"] = merge_unique(
                existing.get("components", []),
                fw.get("components", [])
            )
            existing["limitations"] = merge_unique(
                existing.get("limitations", []),
                fw.get("limitations", [])
            )
            # Update assessment with the latest
            if fw.get("current_assessment"):
                existing["current_assessment"] = fw["current_assessment"]
            existing["last_updated"] = datetime.now(timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            )
            existing["research_iterations"] = existing.get(
                "research_iterations", 1) + 1
            existing.setdefault("iteration_history", []).append(iteration_id)
            save_json(fw_path, existing)
            log(f"Merged framework: {slug}", log_file)
        else:
            new_entry = {
                "slug": slug,
                "purpose": fw.get("purpose", ""),
                "components": fw.get("components", []),
                "current_assessment": fw.get("current_assessment", ""),
                "limitations": fw.get("limitations", []),
                "topic": fw.get("topic", ""),
                "created_at": datetime.now(timezone.utc).strftime(
                    "%Y-%m-%dT%H:%M:%SZ"
                ),
                "last_updated": datetime.now(timezone.utc).strftime(
                    "%Y-%m-%dT%H:%M:%SZ"
                ),
                "originating_iteration": iteration_id,
                "research_iterations": 1,
                "iteration_history": [iteration_id],
            }
            save_json(fw_path, new_entry)
            log(f"Created framework: {slug}", log_file)

        written += 1

    return written


# ---------------------------------------------------------------------------
# Index update
# ---------------------------------------------------------------------------

def update_index(kb_dir: str, iteration_id: str, topic: str,
                 topic_category: str, stats: dict) -> None:
    """Update knowledge_base/index.json with metadata for all entries."""
    index_path = os.path.join(kb_dir, "index.json")
    index = load_json(index_path) or {
        "version": 1,
        "entries": {},
        "iterations": [],
    }

    # Scan all concept, relationship, and framework files
    entries = index.setdefault("entries", {})

    for subdir, entry_type in [("concepts", "concept"),
                                ("relationships", "relationship"),
                                ("frameworks", "framework")]:
        dir_path = os.path.join(kb_dir, subdir)
        if not os.path.isdir(dir_path):
            continue
        for fname in os.listdir(dir_path):
            if not fname.endswith(".json"):
                continue
            slug = fname[:-5]
            fpath = os.path.join(dir_path, fname)
            data = load_json(fpath)
            if data is None:
                continue
            entries[f"{entry_type}:{slug}"] = {
                "type": entry_type,
                "slug": slug,
                "confidence": data.get("confidence", 0),
                "last_updated": data.get("last_updated", ""),
                "research_iterations": data.get("research_iterations", 1),
                "topic": data.get("topic", ""),
            }

    # Record this iteration
    iterations = index.setdefault("iterations", [])
    iterations.append({
        "iteration_id": iteration_id,
        "topic": topic,
        "topic_category": topic_category,
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "stats": stats,
    })

    index["last_updated"] = datetime.now(timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )

    save_json(index_path, index)


# ---------------------------------------------------------------------------
# Anti-knowledge and low-confidence (append, don't overwrite)
# ---------------------------------------------------------------------------

def append_evidence_entries(entries: list, filepath: str) -> None:
    """Append entries to an evidence JSON file (array of objects)."""
    existing = load_json(filepath)
    if existing is None or not isinstance(existing, list):
        existing = []
    existing.extend(entries)
    save_json(filepath, existing)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Write extracted knowledge entries to the KB directory."
    )
    parser.add_argument("--phase4-dir", required=True,
                        help="Phase 4 output directory.")
    parser.add_argument("--kb-dir", required=True,
                        help="Knowledge base root directory.")
    parser.add_argument("--iteration-id", required=True,
                        help="Iteration identifier.")
    parser.add_argument("--topic", required=True, help="Topic slug.")
    parser.add_argument("--topic-category", required=True,
                        help="Topic category.")
    parser.add_argument("--min-confidence", type=int, default=4,
                        help="Minimum confidence for KB write (default 4).")
    parser.add_argument("--log-file", default="",
                        help="Optional log file path.")

    args = parser.parse_args()
    log_file = args.log_file or os.environ.get("LOG_FILE", "")
    phase4_dir = args.phase4_dir
    kb_dir = args.kb_dir

    log("Starting KB write phase", log_file)

    # --- Read phase4 output files ---
    concepts = load_json(os.path.join(phase4_dir, "concepts.json"))
    if concepts is None:
        concepts = []
        log("WARNING: concepts.json not found or invalid", log_file)

    relationships = load_json(os.path.join(phase4_dir, "relationships.json"))
    if relationships is None:
        relationships = []
        log("WARNING: relationships.json not found or invalid", log_file)

    frameworks = load_json(os.path.join(phase4_dir, "frameworks.json"))
    if frameworks is None:
        frameworks = []
        log("WARNING: frameworks.json not found or invalid", log_file)

    anti_knowledge = load_json(os.path.join(phase4_dir, "anti_knowledge.json"))
    if anti_knowledge is None:
        anti_knowledge = []

    low_confidence_items = load_json(
        os.path.join(phase4_dir, "low_confidence.json")
    )
    if low_confidence_items is None:
        low_confidence_items = []

    # --- Write concepts (only HIGH_CONFIDENCE and MODERATE_CONFIDENCE) ---
    concepts_written = write_concepts(
        concepts, kb_dir, args.iteration_id, args.min_confidence, log_file
    )
    log(f"Concepts written to KB: {concepts_written}", log_file)

    # --- Write relationships ---
    rels_written = write_relationships(
        relationships, kb_dir, args.iteration_id, args.min_confidence, log_file
    )
    log(f"Relationships written to KB: {rels_written}", log_file)

    # --- Write frameworks ---
    fw_written = write_frameworks(
        frameworks, kb_dir, args.iteration_id, log_file
    )
    log(f"Frameworks written to KB: {fw_written}", log_file)

    # --- Anti-knowledge: append to evidence file ---
    evidence_dir = os.path.join(kb_dir, "evidence")
    os.makedirs(evidence_dir, exist_ok=True)

    if anti_knowledge:
        ak_path = os.path.join(evidence_dir, "anti_knowledge.json")
        append_evidence_entries(anti_knowledge, ak_path)
        log(f"Appended {len(anti_knowledge)} anti-knowledge entries", log_file)

    # --- Low-confidence: append to pending file ---
    if low_confidence_items:
        lc_path = os.path.join(evidence_dir, "low_confidence_pending.json")
        append_evidence_entries(low_confidence_items, lc_path)
        log(f"Appended {len(low_confidence_items)} low-confidence entries",
            log_file)

    # --- Update index ---
    stats = {
        "concepts_written": concepts_written,
        "relationships_written": rels_written,
        "frameworks_written": fw_written,
        "anti_knowledge_entries": len(anti_knowledge),
        "low_confidence_entries": len(low_confidence_items),
    }
    update_index(kb_dir, args.iteration_id, args.topic,
                 args.topic_category, stats)
    log("KB index updated", log_file)

    # --- Rebuild derived search indexes ---
    rebuild_script = os.path.join(kb_dir, "rebuild_indexes.py")
    if os.path.isfile(rebuild_script):
        import subprocess
        try:
            subprocess.run(
                ["python3", rebuild_script, "--kb-dir", kb_dir],
                capture_output=True, text=True, timeout=30
            )
            log("Search indexes rebuilt", log_file)
        except Exception as e:
            log(f"WARNING: Index rebuild failed: {e}", log_file)

    log("Phase 5 KB write complete", log_file)


if __name__ == "__main__":
    main()
