#!/usr/bin/env python3
"""
rebuild_indexes.py — Build derived search indexes from source JSON files.

Generates:
  indexes/inverted_index.json  — token -> list of (type, slug) for O(1) keyword lookup
  indexes/topic_graph.json     — adjacency list for O(1) graph traversal
  indexes/topic_stats.json     — per-topic concept counts, avg confidence, top concepts

Run after any KB write. Takes <1s for 1000+ entries.

Usage:
    python3 rebuild_indexes.py [--kb-dir /path/to/knowledge_base]
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

KB_DIR = Path(__file__).parent


def load_all_json(subdir, kb_dir=None):
    """Load all JSON files from a subdirectory."""
    d = (kb_dir or KB_DIR) / subdir
    results = []
    if not d.exists():
        return results
    for p in sorted(d.glob("*.json")):
        try:
            with open(p) as f:
                data = json.load(f)
                data["_type"] = subdir.rstrip("s")  # concepts -> concept
                results.append(data)
        except (json.JSONDecodeError, OSError):
            pass
    return results


def tokenize(text):
    """Extract searchable tokens from text. Lowercased, split on non-alpha."""
    if not text:
        return set()
    return set(re.findall(r'[a-z0-9]{2,}', text.lower()))


def build_inverted_index(concepts, relationships, frameworks):
    """Build token -> [(type, slug, field)] inverted index."""
    index = defaultdict(list)

    for c in concepts:
        slug = c.get("slug", "")
        entry_ref = ("concept", slug)

        # Index slug tokens
        for token in tokenize(slug):
            index[token].append(entry_ref)

        # Index definition
        for token in tokenize(c.get("definition", "")):
            index[token].append(entry_ref)

        # Index topic
        for token in tokenize(c.get("topic", "")):
            index[token].append(entry_ref)

        # Index related concepts (as tokens)
        for rel in c.get("related_concepts", []):
            for token in tokenize(rel):
                index[token].append(entry_ref)

    for r in relationships:
        a = r.get("concept_a", "")
        b = r.get("concept_b", "")
        slug = f"{sorted([a, b])[0]}__{sorted([a, b])[1]}" if a and b else ""
        entry_ref = ("relationship", slug)

        for token in tokenize(a):
            index[token].append(entry_ref)
        for token in tokenize(b):
            index[token].append(entry_ref)
        for token in tokenize(r.get("mechanism", "")):
            index[token].append(entry_ref)

    for fw in frameworks:
        slug = fw.get("slug", "")
        entry_ref = ("framework", slug)

        for token in tokenize(slug):
            index[token].append(entry_ref)
        for token in tokenize(fw.get("purpose", "")):
            index[token].append(entry_ref)
        for token in tokenize(json.dumps(fw.get("components", []))):
            index[token].append(entry_ref)

    # Deduplicate entries per token
    deduped = {}
    for token, refs in index.items():
        seen = set()
        unique_refs = []
        for ref in refs:
            key = f"{ref[0]}:{ref[1]}"
            if key not in seen:
                seen.add(key)
                unique_refs.append(ref)
        deduped[token] = unique_refs

    return deduped


def build_topic_graph(concepts, relationships):
    """Build adjacency list for graph traversal.

    Returns: {slug: {neighbors: [slug, ...], relationships: [{a, b, mechanism, direction, confidence}, ...]}}
    """
    graph = defaultdict(lambda: {"neighbors": set(), "relationships": []})

    # From concept.related_concepts
    for c in concepts:
        slug = c.get("slug", "")
        for rel in c.get("related_concepts", []):
            graph[slug]["neighbors"].add(rel)
            graph[rel]["neighbors"].add(slug)

    # From relationships
    for r in relationships:
        a = r.get("concept_a", "")
        b = r.get("concept_b", "")
        if a and b:
            graph[a]["neighbors"].add(b)
            graph[b]["neighbors"].add(a)
            edge = {
                "concept_a": a,
                "concept_b": b,
                "mechanism": r.get("mechanism", "")[:200],
                "direction": r.get("direction", ""),
                "confidence": r.get("confidence", 0),
            }
            graph[a]["relationships"].append(edge)
            graph[b]["relationships"].append(edge)

    # Convert sets to sorted lists for JSON serialization
    serializable = {}
    for slug, data in graph.items():
        serializable[slug] = {
            "neighbors": sorted(data["neighbors"]),
            "relationships": data["relationships"],
        }

    return serializable


def build_topic_stats(concepts, relationships, frameworks):
    """Build per-topic statistics."""
    stats = defaultdict(lambda: {
        "concept_count": 0,
        "relationship_count": 0,
        "framework_count": 0,
        "total_confidence": 0,
        "top_concepts": [],
        "all_concept_slugs": [],
    })

    for c in concepts:
        topic = c.get("topic", "unknown")
        stats[topic]["concept_count"] += 1
        stats[topic]["total_confidence"] += c.get("confidence", 0)
        stats[topic]["all_concept_slugs"].append(c.get("slug", ""))
        stats[topic]["top_concepts"].append({
            "slug": c.get("slug", ""),
            "confidence": c.get("confidence", 0),
            "definition": c.get("definition", "")[:150],
        })

    for r in relationships:
        topic = r.get("topic", "unknown")
        stats[topic]["relationship_count"] += 1

    for fw in frameworks:
        topic = fw.get("topic", "unknown")
        stats[topic]["framework_count"] += 1

    # Finalize: sort top concepts, compute averages
    result = {}
    for topic, data in sorted(stats.items()):
        data["top_concepts"].sort(key=lambda x: -x["confidence"])
        data["top_concepts"] = data["top_concepts"][:10]
        data["avg_confidence"] = round(
            data["total_confidence"] / max(data["concept_count"], 1), 1
        )
        del data["total_confidence"]
        result[topic] = data

    return result


def main():
    parser = argparse.ArgumentParser(description="Rebuild KB search indexes")
    parser.add_argument("--kb-dir", default=str(KB_DIR))
    args = parser.parse_args()

    kb_dir = Path(args.kb_dir)

    print(f"Loading KB from {kb_dir}...")

    concepts = load_all_json("concepts", kb_dir)
    relationships = load_all_json("relationships", kb_dir)
    frameworks = load_all_json("frameworks", kb_dir)

    print(f"Loaded: {len(concepts)} concepts, {len(relationships)} relationships, "
          f"{len(frameworks)} frameworks")

    # Build indexes
    idx_dir = kb_dir / "indexes"
    idx_dir.mkdir(exist_ok=True)

    print("Building inverted index...")
    inverted = build_inverted_index(concepts, relationships, frameworks)
    with open(idx_dir / "inverted_index.json", "w") as f:
        json.dump(inverted, f, separators=(",", ":"))
    print(f"  {len(inverted)} unique tokens indexed")

    print("Building topic graph...")
    graph = build_topic_graph(concepts, relationships)
    with open(idx_dir / "topic_graph.json", "w") as f:
        json.dump(graph, f, separators=(",", ":"))
    print(f"  {len(graph)} nodes in graph")

    print("Building topic stats...")
    topic_stats = build_topic_stats(concepts, relationships, frameworks)
    with open(idx_dir / "topic_stats.json", "w") as f:
        json.dump(topic_stats, f, indent=2)
    print(f"  {len(topic_stats)} topics")

    print("Done.")


if __name__ == "__main__":
    main()
