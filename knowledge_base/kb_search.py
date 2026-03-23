#!/usr/bin/env python3
"""
kb_search.py — Lightweight CLI search tool for the finance research knowledge base.

Usage:
    # Search by keyword (searches slugs, definitions, mechanisms)
    python3 kb_search.py search "inflation"

    # Search by topic
    python3 kb_search.py topic "monetary_policy"

    # Find related concepts (1-hop graph traversal)
    python3 kb_search.py related "basis_trade_fragility"

    # Find related concepts (2-hop)
    python3 kb_search.py related "basis_trade_fragility" --depth 2

    # List all topics
    python3 kb_search.py topics

    # Get full detail on a concept
    python3 kb_search.py get "basis_trade_fragility"

    # High-confidence concepts (min confidence threshold)
    python3 kb_search.py search "inflation" --min-confidence 7

    # Output as JSON (for programmatic use by agents)
    python3 kb_search.py search "inflation" --json

All commands return results sorted by confidence (descending).
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

KB_DIR = Path(__file__).parent


def load_index():
    with open(KB_DIR / "index.json") as f:
        return json.load(f)["entries"]


def load_json(subdir, slug):
    path = KB_DIR / subdir / f"{slug}.json"
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return None


def load_all(subdir):
    results = []
    d = KB_DIR / subdir
    if not d.exists():
        return results
    for p in d.glob("*.json"):
        with open(p) as f:
            try:
                results.append(json.load(f))
            except json.JSONDecodeError:
                pass
    return results


def search_keyword(keyword, min_confidence=0):
    """Search across concepts, relationships, and frameworks by keyword."""
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    results = {"concepts": [], "relationships": [], "frameworks": []}

    for c in load_all("concepts"):
        if c.get("confidence", 0) < min_confidence:
            continue
        text = f"{c.get('slug', '')} {c.get('definition', '')} {' '.join(c.get('evidence', []))} {' '.join(c.get('related_concepts', []))}"
        if pattern.search(text):
            results["concepts"].append({
                "slug": c["slug"],
                "definition": c.get("definition", "")[:200],
                "confidence": c.get("confidence", 0),
                "topic": c.get("topic", ""),
                "related": c.get("related_concepts", []),
            })

    for r in load_all("relationships"):
        if r.get("confidence", 0) < min_confidence:
            continue
        text = f"{r.get('concept_a', '')} {r.get('concept_b', '')} {r.get('mechanism', '')}"
        if pattern.search(text):
            results["relationships"].append({
                "concept_a": r["concept_a"],
                "concept_b": r["concept_b"],
                "mechanism": r.get("mechanism", "")[:200],
                "direction": r.get("direction", ""),
                "confidence": r.get("confidence", 0),
                "topic": r.get("topic", ""),
            })

    for fw in load_all("frameworks"):
        if pattern.search(json.dumps(fw)):
            results["frameworks"].append({
                "slug": fw["slug"],
                "purpose": fw.get("purpose", "")[:200],
                "topic": fw.get("topic", ""),
            })

    results["concepts"].sort(key=lambda x: x["confidence"], reverse=True)
    results["relationships"].sort(key=lambda x: x["confidence"], reverse=True)
    return results


def search_topic(topic):
    """Get all concepts, relationships, and frameworks for a topic."""
    results = {"concepts": [], "relationships": [], "frameworks": []}

    for c in load_all("concepts"):
        if c.get("topic") == topic:
            results["concepts"].append({
                "slug": c["slug"],
                "definition": c.get("definition", "")[:200],
                "confidence": c.get("confidence", 0),
                "related": c.get("related_concepts", []),
            })

    for r in load_all("relationships"):
        if r.get("topic") == topic:
            results["relationships"].append({
                "concept_a": r["concept_a"],
                "concept_b": r["concept_b"],
                "mechanism": r.get("mechanism", "")[:200],
                "direction": r.get("direction", ""),
                "confidence": r.get("confidence", 0),
            })

    for fw in load_all("frameworks"):
        if fw.get("topic") == topic:
            results["frameworks"].append({
                "slug": fw["slug"],
                "purpose": fw.get("purpose", "")[:200],
            })

    results["concepts"].sort(key=lambda x: x["confidence"], reverse=True)
    results["relationships"].sort(key=lambda x: x["confidence"], reverse=True)
    return results


def find_related(slug, depth=1):
    """Graph traversal: find concepts connected via relationships and related_concepts fields."""
    visited = set()
    frontier = {slug}
    graph = {"nodes": [], "edges": []}

    for d in range(depth):
        next_frontier = set()
        for s in frontier:
            if s in visited:
                continue
            visited.add(s)

            concept = load_json("concepts", s)
            if concept:
                graph["nodes"].append({
                    "slug": s,
                    "definition": concept.get("definition", "")[:150],
                    "confidence": concept.get("confidence", 0),
                    "topic": concept.get("topic", ""),
                    "hop": d,
                })
                for rel in concept.get("related_concepts", []):
                    next_frontier.add(rel)

        # Also check relationships
        for r in load_all("relationships"):
            a, b = r.get("concept_a", ""), r.get("concept_b", "")
            if a in frontier or b in frontier:
                graph["edges"].append({
                    "from": a,
                    "to": b,
                    "mechanism": r.get("mechanism", "")[:150],
                    "direction": r.get("direction", ""),
                    "confidence": r.get("confidence", 0),
                })
                if a in frontier:
                    next_frontier.add(b)
                if b in frontier:
                    next_frontier.add(a)

        frontier = next_frontier - visited

    # Pick up any remaining frontier nodes
    for s in frontier:
        concept = load_json("concepts", s)
        if concept and s not in visited:
            graph["nodes"].append({
                "slug": s,
                "definition": concept.get("definition", "")[:150],
                "confidence": concept.get("confidence", 0),
                "topic": concept.get("topic", ""),
                "hop": depth,
            })

    graph["nodes"].sort(key=lambda x: (x["hop"], -x["confidence"]))
    return graph


def list_topics():
    """List all topics with concept counts."""
    index = load_index()
    topic_counts = {}
    for entry in index.values():
        t = entry.get("topic", "unknown")
        topic_counts[t] = topic_counts.get(t, 0) + 1
    return dict(sorted(topic_counts.items(), key=lambda x: -x[1]))


def get_concept(slug):
    """Get full detail for a concept."""
    return load_json("concepts", slug)


def format_text(data, command):
    """Human-readable text output."""
    lines = []

    if command == "search" or command == "topic":
        concepts = data.get("concepts", [])
        rels = data.get("relationships", [])
        fws = data.get("frameworks", [])

        if concepts:
            lines.append(f"CONCEPTS ({len(concepts)}):")
            for c in concepts[:20]:
                lines.append(f"  [{c['confidence']:.0f}] {c['slug']}")
                lines.append(f"       {c['definition']}")
                if c.get("related"):
                    lines.append(f"       related: {', '.join(c['related'][:5])}")
                if c.get("topic"):
                    lines.append(f"       topic: {c['topic']}")
                lines.append("")

        if rels:
            lines.append(f"RELATIONSHIPS ({len(rels)}):")
            for r in rels[:15]:
                arrow = " -> " if r["direction"] == "a_causes_b" else " <-> "
                lines.append(f"  [{r['confidence']:.0f}] {r['concept_a']}{arrow}{r['concept_b']}")
                lines.append(f"       {r['mechanism']}")
                lines.append("")

        if fws:
            lines.append(f"FRAMEWORKS ({len(fws)}):")
            for fw in fws[:10]:
                lines.append(f"  {fw['slug']}")
                lines.append(f"       {fw['purpose']}")
                lines.append("")

        if not concepts and not rels and not fws:
            lines.append("No results found.")

    elif command == "related":
        nodes = data.get("nodes", [])
        edges = data.get("edges", [])
        lines.append(f"RELATED CONCEPTS ({len(nodes)} nodes, {len(edges)} edges):")
        for n in nodes:
            hop_label = f"[hop {n['hop']}]" if n["hop"] > 0 else "[root]"
            lines.append(f"  {hop_label} [{n['confidence']:.0f}] {n['slug']} ({n['topic']})")
            lines.append(f"         {n['definition']}")
            lines.append("")

    elif command == "topics":
        lines.append("TOPICS (by entry count):")
        for topic, count in data.items():
            lines.append(f"  {count:4d}  {topic}")

    elif command == "get":
        if data:
            lines.append(json.dumps(data, indent=2))
        else:
            lines.append("Concept not found.")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Search the finance research knowledge base")
    sub = parser.add_subparsers(dest="command", required=True)

    p_search = sub.add_parser("search", help="Keyword search across KB")
    p_search.add_argument("keyword")
    p_search.add_argument("--min-confidence", type=float, default=0)
    p_search.add_argument("--json", action="store_true")

    p_topic = sub.add_parser("topic", help="Get all entries for a topic")
    p_topic.add_argument("topic_name")
    p_topic.add_argument("--json", action="store_true")

    p_related = sub.add_parser("related", help="Find related concepts (graph traversal)")
    p_related.add_argument("slug")
    p_related.add_argument("--depth", type=int, default=1)
    p_related.add_argument("--json", action="store_true")

    p_topics = sub.add_parser("topics", help="List all topics")
    p_topics.add_argument("--json", action="store_true")

    p_get = sub.add_parser("get", help="Get full detail for a concept")
    p_get.add_argument("slug")
    p_get.add_argument("--json", action="store_true")

    args = parser.parse_args()

    if args.command == "search":
        data = search_keyword(args.keyword, args.min_confidence)
    elif args.command == "topic":
        data = search_topic(args.topic_name)
    elif args.command == "related":
        data = find_related(args.slug, args.depth)
    elif args.command == "topics":
        data = list_topics()
    elif args.command == "get":
        data = get_concept(args.slug)

    if getattr(args, "json", False):
        print(json.dumps(data, indent=2))
    else:
        print(format_text(data, args.command))


if __name__ == "__main__":
    main()
