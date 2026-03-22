#!/usr/bin/env python3
"""Curriculum-aware topic selection for finance research pipeline.

Scoring: prioritizes topics with lowest confidence, oldest last_researched,
most knowledge_gaps, and unexplored connections. Deep-dive mode for depth >= 3.

Usage: python3 select_topic.py /path/to/topic_registry.json
Output: JSON to stdout with selected topic, mode (overview/deep_dive), and context.
"""
import json
import sys
import time
from pathlib import Path

def score_topic(topic_id: str, topic: dict, now: float) -> float:
    """Higher score = higher priority for research."""
    score = 0.0

    # 1. Low confidence → high priority (weight: 30%)
    confidence = topic.get("confidence_score", 5.0)
    score += (10.0 - confidence) * 3.0  # max 30

    # 2. Oldest last_researched → high priority (weight: 25%)
    last = topic.get("last_researched")
    if last is None:
        score += 25.0  # never researched = max priority
    else:
        try:
            from datetime import datetime, timezone
            dt = datetime.fromisoformat(last.replace("Z", "+00:00"))
            age_hours = (now - dt.timestamp()) / 3600.0
            score += min(age_hours * 0.5, 25.0)  # caps at 50 hours old
        except (ValueError, TypeError):
            score += 25.0

    # 3. Knowledge gaps → high priority (weight: 25%)
    gaps = len(topic.get("knowledge_gaps", []))
    score += min(gaps * 8.0, 25.0)  # 3+ gaps = max

    # 4. Unexplored connections (weight: 15%)
    connections = topic.get("connections", [])
    score += len(connections) * 3.0  # more connections = more to explore

    # 5. Low depth level bonus (weight: 5%)
    depth = topic.get("depth_level", 0)
    if depth == 0:
        score += 5.0
    elif depth == 1:
        score += 3.0

    return round(score, 2)


def select(registry_path: str) -> dict:
    reg = json.loads(Path(registry_path).read_text())
    topics = reg.get("topics", {})
    now = time.time()

    scored = []
    for tid, tdata in topics.items():
        s = score_topic(tid, tdata, now)
        scored.append((s, tid, tdata))

    scored.sort(key=lambda x: -x[0])  # highest score first

    if not scored:
        return {"error": "no topics in registry"}

    best_score, best_id, best_data = scored[0]
    depth = best_data.get("depth_level", 0)

    # Deep-dive mode for depth >= 3
    mode = "deep_dive" if depth >= 3 else "overview"

    # Build focus areas based on mode
    if mode == "deep_dive":
        focus = {
            "subtopics": best_data.get("subtopics", []),
            "knowledge_gaps": best_data.get("knowledge_gaps", []),
            "connections_to_explore": best_data.get("connections", []),
            "instruction": "This topic has been studied at overview level. Focus on: (1) specific subtopics listed, (2) closing identified knowledge gaps, (3) cross-topic interactions with connected topics, (4) edge cases and regime-dependent behavior."
        }
    else:
        focus = {
            "knowledge_gaps": best_data.get("knowledge_gaps", []),
            "connections_to_explore": best_data.get("connections", []),
            "instruction": "Build foundational understanding: define core concepts, establish theoretical frameworks, identify key empirical patterns, and map connections to related topics."
        }

    # Collect related topic info for context
    related = {}
    for conn_id in best_data.get("connections", [])[:5]:
        if conn_id in topics:
            ct = topics[conn_id]
            related[conn_id] = {
                "display_name": ct.get("display_name", conn_id),
                "confidence_score": ct.get("confidence_score", 0),
                "depth_level": ct.get("depth_level", 0)
            }

    # Top 5 candidates for transparency
    runners_up = [{"topic": tid, "score": s} for s, tid, _ in scored[1:6]]

    return {
        "selected_topic": best_id,
        "display_name": best_data.get("display_name", best_id),
        "category": best_data.get("category", "unknown"),
        "mode": mode,
        "depth_level": depth,
        "confidence_score": best_data.get("confidence_score", 0),
        "score": best_score,
        "focus": focus,
        "related_topics": related,
        "runners_up": runners_up,
        "key_concepts": best_data.get("key_concepts", [])
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "usage: select_topic.py <registry.json>"}))
        sys.exit(1)
    result = select(sys.argv[1])
    print(json.dumps(result, indent=2))
