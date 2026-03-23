#!/usr/bin/env python3
"""
kb_search.py — Semantic-aware CLI search tool for the finance research knowledge base.

Searches expand queries with related finance terms automatically.
"inflation" also finds deflation, CPI, disinflation, price stability, etc.

Usage:
    # Semantic keyword search (auto-expands to related terms)
    python3 kb_search.py search "inflation"
    python3 kb_search.py search "interest rates"

    # Exact keyword only (no expansion)
    python3 kb_search.py search "inflation" --exact

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

    # Show which expanded terms were used
    python3 kb_search.py search "inflation" --show-expansion

All commands return results sorted by confidence (descending).
"""

import argparse
import json
import os
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

KB_DIR = Path(__file__).parent

# ---------------------------------------------------------------------------
# Finance domain term expansion map
# Each key expands to a set of semantically related search terms.
# Matching is bidirectional: searching any term in a group finds all others.
# ---------------------------------------------------------------------------
TERM_GROUPS = [
    {"inflation", "deflation", "disinflation", "cpi", "pce", "price_level",
     "price_stability", "stagflation", "hyperinflation", "core_inflation",
     "headline_inflation", "inflation_expectations", "price_pressures"},
    {"interest_rates", "rates", "fed_funds", "policy_rate", "rate_hike",
     "rate_cut", "terminal_rate", "neutral_rate", "r_star", "overnight_rate",
     "fed_rate", "base_rate", "discount_rate"},
    {"yield_curve", "yield", "term_premium", "term_structure", "inversion",
     "steepening", "flattening", "2s10s", "10y", "treasury", "bond_yield",
     "duration", "convexity"},
    {"recession", "downturn", "contraction", "economic_slowdown", "hard_landing",
     "soft_landing", "gdp_decline", "negative_growth", "business_cycle"},
    {"equity", "stock", "equities", "shares", "stock_market", "s_p_500",
     "nasdaq", "earnings", "valuation", "pe_ratio", "equity_risk_premium"},
    {"credit", "credit_spread", "high_yield", "investment_grade", "default",
     "credit_risk", "corporate_bonds", "leveraged_loans", "credit_cycle",
     "credit_tightening", "lending_standards"},
    {"dollar", "usd", "dxy", "dollar_index", "greenback", "dollar_strength",
     "dollar_weakness", "reserve_currency"},
    {"fx", "currency", "exchange_rate", "forex", "carry_trade", "em_currency",
     "currency_regime", "devaluation", "appreciation", "depreciation"},
    {"oil", "crude", "brent", "wti", "energy", "petroleum", "opec",
     "oil_price", "energy_prices", "fossil_fuel"},
    {"fed", "federal_reserve", "fomc", "powell", "central_bank", "ecb",
     "boj", "pboc", "monetary_policy", "quantitative_easing", "qe", "qt",
     "quantitative_tightening", "tapering", "dovish", "hawkish"},
    {"fiscal", "fiscal_policy", "government_spending", "deficit", "surplus",
     "debt_ceiling", "fiscal_stimulus", "austerity", "fiscal_dominance",
     "budget_deficit", "national_debt", "public_debt"},
    {"volatility", "vix", "vol", "implied_vol", "realized_vol", "vol_surface",
     "risk_off", "risk_on", "tail_risk", "black_swan", "move_index"},
    {"commodity", "commodities", "raw_materials", "metals", "gold", "copper",
     "agricultural", "supercycle", "commodity_prices"},
    {"employment", "unemployment", "jobs", "labor", "labour", "payroll",
     "nfp", "wage", "wages", "wage_growth", "labor_market", "participation_rate",
     "jobless_claims"},
    {"housing", "real_estate", "shelter", "rent", "mortgage", "home_prices",
     "housing_market", "oer", "owners_equivalent_rent"},
    {"china", "chinese", "pbc", "renminbi", "rmb", "cny", "yuan",
     "china_growth", "chinese_economy"},
    {"emerging_markets", "em", "frontier_markets", "developing_economies",
     "em_debt", "em_equities", "em_currencies"},
    {"sovereign", "sovereign_debt", "government_bonds", "gilts", "bunds",
     "jgb", "sovereign_risk", "sovereign_default"},
    {"crypto", "bitcoin", "btc", "ethereum", "digital_assets", "defi",
     "blockchain", "stablecoin"},
    {"ai", "artificial_intelligence", "machine_learning", "tech", "technology",
     "ai_capex", "semiconductor", "chips", "nvidia"},
    {"liquidity", "money_supply", "m2", "reserves", "bank_reserves",
     "financial_conditions", "tightening", "easing", "credit_conditions"},
    {"correlation", "diversification", "stock_bond_correlation", "cross_asset",
     "portfolio", "asset_allocation", "risk_parity", "decorrelation"},
]


def expand_query(keyword):
    """Expand a search keyword to include semantically related finance terms."""
    kw_lower = keyword.lower().replace(" ", "_")
    expanded = {keyword}  # always include original

    for group in TERM_GROUPS:
        # Check if keyword matches any term in the group (substring match)
        group_lower = {t.lower() for t in group}
        matched = False
        for term in group_lower:
            if kw_lower in term or term in kw_lower:
                matched = True
                break
        if matched:
            expanded.update(group)

    return expanded


def load_inverted_index():
    """Load pre-built inverted index if available."""
    idx_path = KB_DIR / "indexes" / "inverted_index.json"
    if idx_path.exists():
        try:
            with open(idx_path) as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return None


def load_topic_graph():
    """Load pre-built topic graph if available."""
    graph_path = KB_DIR / "indexes" / "topic_graph.json"
    if graph_path.exists():
        try:
            with open(graph_path) as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return None


def load_topic_stats():
    """Load pre-built topic stats if available."""
    stats_path = KB_DIR / "indexes" / "topic_stats.json"
    if stats_path.exists():
        try:
            with open(stats_path) as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return None


def index_search(keyword, inverted_index, min_confidence=0, exact=False):
    """Fast search using the inverted index. Returns candidate (type, slug) pairs
    scored by how many query tokens matched."""
    if exact:
        terms = {keyword}
    else:
        terms = expand_query(keyword)

    # Tokenize all terms
    query_tokens = set()
    for t in terms:
        query_tokens.update(re.findall(r'[a-z0-9]{2,}', t.lower()))

    # Score each entry by number of matching tokens
    scores = {}  # (type, slug) -> match_count
    for token in query_tokens:
        for entry_ref in inverted_index.get(token, []):
            key = tuple(entry_ref)
            scores[key] = scores.get(key, 0) + 1

    # Sort by score descending
    ranked = sorted(scores.items(), key=lambda x: -x[1])
    return ranked, terms


def fuzzy_slug_match(keyword, slug, threshold=0.6):
    """Fuzzy match keyword against a concept slug."""
    kw = keyword.lower().replace(" ", "_")
    s = slug.lower()
    # Direct substring
    if kw in s or s in kw:
        return True
    # Token overlap
    kw_tokens = set(kw.split("_"))
    s_tokens = set(s.split("_"))
    if kw_tokens & s_tokens:
        overlap = len(kw_tokens & s_tokens) / max(len(kw_tokens), 1)
        if overlap >= 0.5:
            return True
    return False


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


def search_keyword(keyword, min_confidence=0, exact=False):
    """Search across concepts, relationships, and frameworks by keyword.

    Uses pre-built inverted index for O(1) token lookup when available.
    Falls back to full-scan regex if indexes aren't built yet.
    By default, expands the query to include semantically related finance terms.
    """
    inverted = load_inverted_index()

    if inverted:
        return _search_indexed(keyword, inverted, min_confidence, exact)
    else:
        return _search_fullscan(keyword, min_confidence, exact)


def _search_indexed(keyword, inverted, min_confidence=0, exact=False):
    """Fast search path using inverted index."""
    ranked, terms = index_search(keyword, inverted, min_confidence, exact)

    results = {"concepts": [], "relationships": [], "frameworks": []}
    kw_pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    seen = set()

    for (entry_type, slug), score in ranked:
        if slug in seen:
            continue
        seen.add(slug)

        if entry_type == "concept":
            c = load_json("concepts", slug)
            if not c or c.get("confidence", 0) < min_confidence:
                continue
            is_direct = bool(kw_pattern.search(
                f"{slug} {c.get('definition', '')} {c.get('topic', '')}"))
            results["concepts"].append({
                "slug": slug,
                "definition": c.get("definition", "")[:200],
                "confidence": c.get("confidence", 0),
                "topic": c.get("topic", ""),
                "related": c.get("related_concepts", []),
                "match_type": "direct" if is_direct else "expanded",
                "_score": score,
            })

        elif entry_type == "relationship":
            r = load_json("relationships", slug)
            if not r or r.get("confidence", 0) < min_confidence:
                continue
            is_direct = bool(kw_pattern.search(
                f"{r.get('concept_a', '')} {r.get('concept_b', '')} {r.get('mechanism', '')}"))
            results["relationships"].append({
                "concept_a": r.get("concept_a", ""),
                "concept_b": r.get("concept_b", ""),
                "mechanism": r.get("mechanism", "")[:200],
                "direction": r.get("direction", ""),
                "confidence": r.get("confidence", 0),
                "topic": r.get("topic", ""),
                "match_type": "direct" if is_direct else "expanded",
                "_score": score,
            })

        elif entry_type == "framework":
            fw = load_json("frameworks", slug)
            if not fw:
                continue
            results["frameworks"].append({
                "slug": slug,
                "purpose": fw.get("purpose", "")[:200],
                "topic": fw.get("topic", ""),
            })

    # Sort: direct first, then by score, then confidence
    results["concepts"].sort(
        key=lambda x: (0 if x["match_type"] == "direct" else 1,
                       -x.get("_score", 0), -x["confidence"]))
    results["relationships"].sort(
        key=lambda x: (0 if x["match_type"] == "direct" else 1,
                       -x.get("_score", 0), -x["confidence"]))

    # Remove internal score from output
    for c in results["concepts"]:
        c.pop("_score", None)
    for r in results["relationships"]:
        r.pop("_score", None)

    if not exact:
        results["_expanded_terms"] = sorted(terms)

    return results


def _search_fullscan(keyword, min_confidence=0, exact=False):
    """Fallback full-scan search (used when indexes aren't built)."""
    if exact:
        terms = {keyword}
    else:
        terms = expand_query(keyword)

    escaped = []
    for t in terms:
        escaped.append(re.escape(t))
        if "_" in t:
            escaped.append(re.escape(t.replace("_", " ")))
        elif " " in t:
            escaped.append(re.escape(t.replace(" ", "_")))
    pattern = re.compile("|".join(escaped), re.IGNORECASE)

    results = {"concepts": [], "relationships": [], "frameworks": []}
    seen_concepts = set()

    for c in load_all("concepts"):
        if c.get("confidence", 0) < min_confidence:
            continue
        slug = c.get("slug", "")
        text = f"{slug} {c.get('definition', '')} {' '.join(c.get('evidence', []))} {' '.join(c.get('related_concepts', []))} {c.get('topic', '')}"
        matched = pattern.search(text) or (not exact and fuzzy_slug_match(keyword, slug))
        if matched and slug not in seen_concepts:
            seen_concepts.add(slug)
            kw_pattern = re.compile(re.escape(keyword), re.IGNORECASE)
            is_direct = bool(kw_pattern.search(text))
            results["concepts"].append({
                "slug": slug,
                "definition": c.get("definition", "")[:200],
                "confidence": c.get("confidence", 0),
                "topic": c.get("topic", ""),
                "related": c.get("related_concepts", []),
                "match_type": "direct" if is_direct else "expanded",
            })

    for r in load_all("relationships"):
        if r.get("confidence", 0) < min_confidence:
            continue
        text = f"{r.get('concept_a', '')} {r.get('concept_b', '')} {r.get('mechanism', '')} {r.get('topic', '')}"
        if pattern.search(text):
            kw_pattern = re.compile(re.escape(keyword), re.IGNORECASE)
            is_direct = bool(kw_pattern.search(text))
            results["relationships"].append({
                "concept_a": r["concept_a"],
                "concept_b": r["concept_b"],
                "mechanism": r.get("mechanism", "")[:200],
                "direction": r.get("direction", ""),
                "confidence": r.get("confidence", 0),
                "topic": r.get("topic", ""),
                "match_type": "direct" if is_direct else "expanded",
            })

    for fw in load_all("frameworks"):
        if pattern.search(json.dumps(fw)):
            results["frameworks"].append({
                "slug": fw["slug"],
                "purpose": fw.get("purpose", "")[:200],
                "topic": fw.get("topic", ""),
            })

    results["concepts"].sort(key=lambda x: (0 if x["match_type"] == "direct" else 1, -x["confidence"]))
    results["relationships"].sort(key=lambda x: (0 if x["match_type"] == "direct" else 1, -x["confidence"]))

    if not exact:
        results["_expanded_terms"] = sorted(terms)

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
    """Graph traversal: find concepts connected via relationships and related_concepts fields.

    Uses pre-built topic graph for O(1) neighbor lookup when available.
    Falls back to full scan otherwise.
    """
    topic_graph = load_topic_graph()
    visited = set()
    frontier = {slug}
    result = {"nodes": [], "edges": []}

    for d in range(depth):
        next_frontier = set()
        for s in frontier:
            if s in visited:
                continue
            visited.add(s)

            concept = load_json("concepts", s)
            if concept:
                result["nodes"].append({
                    "slug": s,
                    "definition": concept.get("definition", "")[:150],
                    "confidence": concept.get("confidence", 0),
                    "topic": concept.get("topic", ""),
                    "hop": d,
                })

            if topic_graph and s in topic_graph:
                # Fast path: use pre-built adjacency list
                node_data = topic_graph[s]
                for neighbor in node_data.get("neighbors", []):
                    next_frontier.add(neighbor)
                for edge in node_data.get("relationships", []):
                    result["edges"].append({
                        "from": edge.get("concept_a", ""),
                        "to": edge.get("concept_b", ""),
                        "mechanism": edge.get("mechanism", "")[:150],
                        "direction": edge.get("direction", ""),
                        "confidence": edge.get("confidence", 0),
                    })
            else:
                # Slow path: scan related_concepts field
                if concept:
                    for rel in concept.get("related_concepts", []):
                        next_frontier.add(rel)
                # Scan all relationships
                for r in load_all("relationships"):
                    a, b = r.get("concept_a", ""), r.get("concept_b", "")
                    if a == s or b == s:
                        result["edges"].append({
                            "from": a,
                            "to": b,
                            "mechanism": r.get("mechanism", "")[:150],
                            "direction": r.get("direction", ""),
                            "confidence": r.get("confidence", 0),
                        })
                        if a == s:
                            next_frontier.add(b)
                        if b == s:
                            next_frontier.add(a)

        frontier = next_frontier - visited

    # Pick up frontier nodes at final depth
    for s in frontier:
        concept = load_json("concepts", s)
        if concept and s not in visited:
            result["nodes"].append({
                "slug": s,
                "definition": concept.get("definition", "")[:150],
                "confidence": concept.get("confidence", 0),
                "topic": concept.get("topic", ""),
                "hop": depth,
            })

    # Deduplicate edges
    seen_edges = set()
    unique_edges = []
    for e in result["edges"]:
        key = f"{e['from']}:{e['to']}"
        if key not in seen_edges:
            seen_edges.add(key)
            unique_edges.append(e)
    result["edges"] = unique_edges

    result["nodes"].sort(key=lambda x: (x["hop"], -x["confidence"]))
    return result


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


def get_topic_summary(topic_name):
    """Get pre-computed topic stats and top concepts for a topic."""
    stats = load_topic_stats()
    if not stats:
        # Fallback: compute on the fly
        return search_topic(topic_name)

    if topic_name not in stats:
        # Try partial match
        matches = [t for t in stats if topic_name.lower() in t.lower()]
        if matches:
            topic_name = matches[0]
        else:
            return {"error": f"Topic '{topic_name}' not found",
                    "available_topics": sorted(stats.keys())}

    data = stats[topic_name]
    return {
        "topic": topic_name,
        "concept_count": data["concept_count"],
        "relationship_count": data["relationship_count"],
        "framework_count": data["framework_count"],
        "avg_confidence": data["avg_confidence"],
        "top_concepts": data["top_concepts"],
    }


def format_text(data, command, show_expansion=False):
    """Human-readable text output."""
    lines = []

    if command == "search" or command == "topic":
        # Show expansion info if present
        expanded = data.get("_expanded_terms", [])
        if expanded and show_expansion:
            lines.append(f"EXPANDED TERMS: {', '.join(expanded)}")
            lines.append("")

        concepts = data.get("concepts", [])
        rels = data.get("relationships", [])
        fws = data.get("frameworks", [])

        if concepts:
            lines.append(f"CONCEPTS ({len(concepts)}):")
            for c in concepts[:30]:
                match_tag = f" [{c['match_type']}]" if c.get("match_type") == "expanded" else ""
                lines.append(f"  [{c['confidence']:.0f}] {c['slug']}{match_tag}")
                lines.append(f"       {c['definition']}")
                if c.get("related"):
                    lines.append(f"       related: {', '.join(c['related'][:5])}")
                if c.get("topic"):
                    lines.append(f"       topic: {c['topic']}")
                lines.append("")

        if rels:
            lines.append(f"RELATIONSHIPS ({len(rels)}):")
            for r in rels[:20]:
                arrow = " -> " if r["direction"] == "a_causes_b" else " <-> "
                match_tag = f" [{r['match_type']}]" if r.get("match_type") == "expanded" else ""
                lines.append(f"  [{r['confidence']:.0f}] {r['concept_a']}{arrow}{r['concept_b']}{match_tag}")
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

    elif command == "summary":
        if "error" in data:
            lines.append(f"Error: {data['error']}")
            if "available_topics" in data:
                lines.append(f"Available: {', '.join(data['available_topics'])}")
        else:
            lines.append(f"TOPIC SUMMARY: {data['topic']}")
            lines.append(f"  Concepts: {data['concept_count']}")
            lines.append(f"  Relationships: {data['relationship_count']}")
            lines.append(f"  Frameworks: {data['framework_count']}")
            lines.append(f"  Avg Confidence: {data['avg_confidence']}")
            lines.append("")
            lines.append("TOP CONCEPTS:")
            for c in data.get("top_concepts", []):
                lines.append(f"  [{c['confidence']:.0f}] {c['slug']}")
                lines.append(f"       {c['definition']}")
                lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Search the finance research knowledge base")
    sub = parser.add_subparsers(dest="command", required=True)

    p_search = sub.add_parser("search", help="Keyword search across KB (semantic expansion by default)")
    p_search.add_argument("keyword")
    p_search.add_argument("--min-confidence", type=float, default=0)
    p_search.add_argument("--exact", action="store_true", help="Disable term expansion, match keyword literally")
    p_search.add_argument("--show-expansion", action="store_true", help="Show which expanded terms were used")
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

    p_summary = sub.add_parser("summary", help="Get topic summary with stats and top concepts")
    p_summary.add_argument("topic_name")
    p_summary.add_argument("--json", action="store_true")

    args = parser.parse_args()

    if args.command == "search":
        data = search_keyword(args.keyword, args.min_confidence, exact=args.exact)
    elif args.command == "topic":
        data = search_topic(args.topic_name)
    elif args.command == "related":
        data = find_related(args.slug, args.depth)
    elif args.command == "topics":
        data = list_topics()
    elif args.command == "get":
        data = get_concept(args.slug)
    elif args.command == "summary":
        data = get_topic_summary(args.topic_name)

    if getattr(args, "json", False):
        print(json.dumps(data, indent=2))
    else:
        show_exp = getattr(args, "show_expansion", False)
        print(format_text(data, args.command, show_expansion=show_exp))


if __name__ == "__main__":
    main()
