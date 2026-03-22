#!/usr/bin/env python3
"""Update agent scores after a completed iteration.

Usage: python3 update_scores.py --scores ../scoring/agent_scores.json --provenance provenance.json --topic-category macro_frameworks --iteration-id iteration_42
"""

import argparse
import json
import sys
from datetime import datetime, timezone
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


def save_json(path: str, data: dict) -> None:
    """Write a dict to a JSON file with pretty formatting."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def update_scores(
    scores: dict,
    provenance: dict,
    topic_category: str,
    iteration_id: str,
) -> list[str]:
    """Mutate *scores* in place and return a list of summary lines."""

    agent_contributions = provenance.get("agent_contributions", {})
    if not agent_contributions:
        return ["No agent contributions found in provenance file. Nothing to update."]

    scores_map = scores.setdefault("scores", {})
    summaries: list[str] = []

    for role_id, contrib in agent_contributions.items():
        claims_made = contrib.get("claims_made", 0)
        claims_survived = contrib.get("claims_survived", 0)

        # Validate
        if claims_made < 0 or claims_survived < 0:
            print(
                f"Warning: negative claim counts for {role_id}, skipping.",
                file=sys.stderr,
            )
            continue
        if claims_survived > claims_made:
            print(
                f"Warning: claims_survived ({claims_survived}) > claims_made "
                f"({claims_made}) for {role_id}. Clamping to claims_made.",
                file=sys.stderr,
            )
            claims_survived = claims_made

        # Ensure nested structure exists.
        if role_id not in scores_map:
            scores_map[role_id] = {}
        if topic_category not in scores_map[role_id]:
            scores_map[role_id][topic_category] = {
                "times_selected": 0,
                "total_claims_made": 0,
                "claims_survived_to_kb": 0,
                "mean_contribution": 0.5,
                "last_selected_iteration": None,
            }

        entry = scores_map[role_id][topic_category]

        # Increment counters.
        entry["times_selected"] += 1
        entry["total_claims_made"] += claims_made
        entry["claims_survived_to_kb"] += claims_survived

        # Compute this iteration's survival rate.
        this_rate = claims_survived / claims_made if claims_made > 0 else 0.0

        # Incremental mean update: new_mean = old_mean + (1/n) * (this_rate - old_mean)
        n = entry["times_selected"]
        old_mean = entry["mean_contribution"]
        new_mean = old_mean + (1.0 / n) * (this_rate - old_mean)
        entry["mean_contribution"] = round(new_mean, 6)

        entry["last_selected_iteration"] = iteration_id

        summaries.append(
            f"  {role_id}: claims {claims_survived}/{claims_made} survived "
            f"(rate={this_rate:.3f}), mean_contribution {old_mean:.4f} -> {new_mean:.4f}, "
            f"times_selected={n}"
        )

    # Update top-level metadata.
    scores["version"] = scores.get("version", 1)
    scores["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    return summaries


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Update agent scores after a completed research iteration."
    )
    parser.add_argument(
        "--scores",
        required=True,
        help="Path to agent_scores.json (read and overwritten).",
    )
    parser.add_argument(
        "--provenance",
        required=True,
        help="Path to provenance.json with agent contribution data.",
    )
    parser.add_argument(
        "--topic-category",
        required=True,
        help="Topic category for this iteration (e.g. macro_frameworks).",
    )
    parser.add_argument(
        "--iteration-id",
        required=True,
        help="Unique identifier for this iteration (e.g. iteration_42).",
    )

    args = parser.parse_args()

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

    scores = load_json(args.scores, "agent scores")
    provenance = load_json(args.provenance, "provenance")

    summaries = update_scores(
        scores=scores,
        provenance=provenance,
        topic_category=args.topic_category,
        iteration_id=args.iteration_id,
    )

    save_json(args.scores, scores)

    print(f"Score update complete for category '{args.topic_category}', "
          f"iteration '{args.iteration_id}':")
    for line in summaries:
        print(line)
    print(f"\nScores written to: {args.scores}")


if __name__ == "__main__":
    main()
