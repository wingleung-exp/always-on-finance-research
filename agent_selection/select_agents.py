#!/usr/bin/env python3
"""UCB1-based agent selection for multi-agent research pipeline.

Usage: python3 select_agents.py --topic-category macro_frameworks --pool ../agents/agent_pool.json --scores ../scoring/agent_scores.json
Output: JSON to stdout with selected agents and rationale.
"""

import argparse
import json
import math
import sys
from pathlib import Path


def load_json(path: str, label: str) -> dict:
    """Load a JSON file, exiting with a clear message if it is missing or invalid."""
    p = Path(path)
    if not p.exists():
        print(f"Error: {label} file not found: {path}", file=sys.stderr)
        sys.exit(1)
    try:
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as exc:
        print(f"Error: {label} file is not valid JSON: {exc}", file=sys.stderr)
        sys.exit(1)


def compute_ucb1(mean_contribution: float, n_total: int, n_i: int, c: float) -> float:
    """Compute the UCB1 score for one agent.

    Untried agents (n_i == 0) receive infinity so they are always selected
    before any tried agent.
    """
    if n_i == 0:
        return float("inf")
    exploration = c * math.sqrt(math.log(n_total) / n_i)
    return mean_contribution + exploration


def select_agents(
    pool: dict,
    scores: dict,
    topic_category: str,
    count: int,
    exploration_constant: float,
) -> dict:
    """Return the selection result dict with 'selected' and 'all_scores' keys."""

    agents = pool.get("roles", pool.get("agents", []))
    if not agents:
        print("Error: agent pool contains no agents (expected 'roles' or 'agents' key).", file=sys.stderr)
        sys.exit(1)

    score_data = scores.get("scores", {})

    # ---- Compute N_total (total iterations on this category) ---- #
    n_total = 0
    for role_id_scores in score_data.values():
        cat_entry = role_id_scores.get(topic_category, {})
        n_total += cat_entry.get("times_selected", 0)
    # Ensure at least 1 so log(N_total) is defined for tried agents.
    if n_total == 0:
        n_total = 1

    # ---- Score every agent ---- #
    agent_records = []
    all_scores = {}

    for agent in agents:
        role_id = agent["role_id"]
        agent_cat_scores = score_data.get(role_id, {}).get(topic_category, {})
        n_i = agent_cat_scores.get("times_selected", 0)
        mean_contribution = agent_cat_scores.get("mean_contribution", 0.5)

        ucb = compute_ucb1(mean_contribution, n_total, n_i, exploration_constant)

        agent_records.append({
            "role_id": role_id,
            "name": agent.get("name", role_id),
            "category": agent.get("category", "unknown"),
            "ucb_score": ucb,
            "n_i": n_i,
            "mean_contribution": mean_contribution,
        })
        all_scores[role_id] = {
            "ucb_score": ucb if ucb != float("inf") else "infinity",
            "mean_contribution": mean_contribution,
            "times_selected": n_i,
        }

    # ---- Enforce constraints ---- #
    # Partition agents by their declared category.
    generalists = [a for a in agent_records if a["category"] == "generalist"]
    challengers = [a for a in agent_records if a["category"] == "challenger"]
    others = [a for a in agent_records if a["category"] not in ("generalist", "challenger")]

    # Sort each bucket by UCB score descending.
    generalists.sort(key=lambda a: a["ucb_score"], reverse=True)
    challengers.sort(key=lambda a: a["ucb_score"], reverse=True)
    others.sort(key=lambda a: a["ucb_score"], reverse=True)

    selected = []
    selected_ids = set()

    # At least 2 generalists.
    for agent in generalists[:2]:
        agent["reason"] = "generalist slot (constraint: at least 2 generalists)"
        selected.append(agent)
        selected_ids.add(agent["role_id"])

    # At least 1 challenger.
    for agent in challengers[:1]:
        agent["reason"] = "challenger slot (constraint: at least 1 challenger)"
        selected.append(agent)
        selected_ids.add(agent["role_id"])

    # Fill remaining slots by pure UCB score across all agents not yet selected.
    remaining = [a for a in agent_records if a["role_id"] not in selected_ids]
    remaining.sort(key=lambda a: a["ucb_score"], reverse=True)

    slots_left = count - len(selected)
    for agent in remaining[:slots_left]:
        agent["reason"] = "selected by UCB1 score"
        selected.append(agent)
        selected_ids.add(agent["role_id"])

    # ---- Build output ---- #
    output_selected = []
    for agent in selected:
        ucb_display = agent["ucb_score"] if agent["ucb_score"] != float("inf") else "infinity"
        output_selected.append({
            "role_id": agent["role_id"],
            "name": agent["name"],
            "category": agent["category"],
            "ucb_score": ucb_display,
            "reason": agent["reason"],
        })

    return {"selected": output_selected, "all_scores": all_scores}


def main() -> None:
    parser = argparse.ArgumentParser(
        description="UCB1-based agent selection for the multi-agent research pipeline."
    )
    parser.add_argument(
        "--topic-category",
        required=True,
        help="Topic category to select agents for (e.g. macro_frameworks).",
    )
    parser.add_argument(
        "--pool",
        required=True,
        help="Path to agent_pool.json.",
    )
    parser.add_argument(
        "--scores",
        required=True,
        help="Path to agent_scores.json.",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=8,
        help="Number of agents to select (default: 8).",
    )
    parser.add_argument(
        "--exploration-constant",
        type=float,
        default=1.414,
        help="UCB1 exploration constant C (default: sqrt(2) ~ 1.414).",
    )

    args = parser.parse_args()

    if args.count < 4:
        print(
            "Error: --count must be at least 4 to satisfy constraints "
            "(2 generalists + 1 challenger + 1 other).",
            file=sys.stderr,
        )
        sys.exit(1)

    pool = load_json(args.pool, "agent pool")
    scores_data = load_json(args.scores, "agent scores")

    valid_categories = {
        "macro_frameworks",
        "credit_rates",
        "asset_class_dynamics",
        "structural_themes",
        "cross_asset",
    }
    if args.topic_category not in valid_categories:
        print(
            f"Warning: topic category '{args.topic_category}' is not one of the "
            f"standard categories: {sorted(valid_categories)}",
            file=sys.stderr,
        )

    result = select_agents(
        pool=pool,
        scores=scores_data,
        topic_category=args.topic_category,
        count=args.count,
        exploration_constant=args.exploration_constant,
    )

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
