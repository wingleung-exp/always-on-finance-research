# Yield Curve Shape, Inversion, & Term Premium — Behavioral Finance Critic & Historical Falsifier Analysis

## Key Claims

1. **The "7/7 recession-prediction record" is a misleading statistic that exploits survivorship bias, flexible dating, and hindsight in defining what counts as an "inversion" and what counts as a "predicted recession."** The actual conditional probability of recession given inversion is meaningfully lower than implied, and the base rate of recession in any given 24-month window is itself substantial (~25-30%), shrinking the marginal informational content of the signal.

2. **The "steepening trap" thesis — that recession arrives during steepening, not inversion — is a narrative fallacy constructed by selecting three confirming episodes (1990, 2001, 2007) while ignoring the mechanism's multiple failures and non-events.** The pattern is unfalsifiable as specified because the steepening phase encompasses a wide and variable time window that can be retroactively fitted to virtually any recession onset.

3. **The knowledge base's treatment of term premium models (ACM, Kim-Wright) as authoritative decompositions systematically understates model uncertainty, creating a precision illusion.** The 30-50bp divergence between models is not merely a "measurement issue" — it is frequently larger than the signal being extracted, rendering many of the KB's specific quantitative claims (e.g., "term premium accounts for the majority of the 2s10s slope") model-dependent artifacts rather than empirical facts.

4. **The fiscal supply → term premium causal narrative ("$2T+ issuance drives TP higher") exhibits classic availability bias and monocausal reasoning, ignoring multiple historical episodes where large fiscal expansions did not produce term premium increases.** Japan's decades of massive issuance with compressed term premia is the most devastating counterexample, but WWII-era US issuance and the 2020-2021 fiscal expansion also challenge the claimed mechanism.

5. **The "reflexive term premium loop" (r > g triggering self-reinforcing debt instability) is a conjunction fallacy: it requires multiple specific conditions to simultaneously hold, yet is discussed as if it were a single high-probability scenario rather than a compound low-probability event.** The UK Truss episode — the sole cited precedent — was driven by specific political credibility collapse, not by the generic fiscal mechanism being theorized.

6. **The KB's historical threshold claims for correlation regime identification (~200bp for 1967-68 flip, ~0bp for 1998-2000 flip) are anchoring artifacts from two data points that cannot constitute a statistical pattern.** Treating N=2 transitions as establishing "thresholds" is a fundamental sample size error that would not survive peer review in any empirical discipline.

7. **The vol-regime dependence framework (low MOVE = reliable curve signal, high MOVE = contaminated signal) is circular because both MOVE and term premium models are derived from the same yield curve inputs.** This circularity is acknowledged in the KB's own open questions but has not prevented the framework from being used as if it were an independent diagnostic.

8. **Across the entire yield curve KB, there is systematic overconfidence: confidence ratings of 7/10 are assigned to claims that rest on model-dependent decompositions, small samples, and untested mechanisms, creating a false sense of actionability.** A properly calibrated assessment would rate most of these claims at 4-5/10.

---

## Evidence & Reasoning

### Claim 1: The "7/7" Recession Record Is Misleading

**BIAS AUDIT: Survivorship bias, hindsight bias, flexible criteria**

The canonical "yield curve has predicted every recession" claim requires interrogation on multiple dimensions:

**Definition flexibility.** What counts as an "inversion"? The 2s10s spread, the 3m10y spread, and the full term structure can give conflicting signals. The 2s10s inverted briefly in 1998 without a recession following (unless one credits it with "predicting" the 2001 recession three years later — an unfalsifiably long lead time). The 3m10y did not invert before the 1990 recession using some data sources. The literature cherry-picks whichever tenor pair and whichever threshold confirms the narrative.

**Lead time variability.** The lag between inversion and recession onset ranges from 6 to 24+ months across episodes. A signal with a variable lead time of 6-24 months in a system where recessions occur roughly every 7-10 years has a much weaker information ratio than "7/7" suggests. If I told you a recession would occur "sometime in the next 6-24 months" at any random point in an expansion, the base rate alone would give me a 25-30% hit rate.

**False positives suppressed.** The 1966 near-inversion (or actual inversion, depending on data source) did not produce a recession. The 1998 2s10s inversion did not produce an immediate recession. The 2022-2023 inversion — the deepest and most prolonged in 40 years — has not (as of March 2026) produced a recession. The KB acknowledges this last point under "vol regime dependence" but treats it as an exception that proves the rule rather than as a falsification.

**Proper Bayesian framing.** P(recession | inversion) is not the same as P(inversion | recession). Even if every recession was preceded by inversion, the signal's value depends on the false positive rate. With at least 2-3 false positives in the record and a 25-30% base rate of recession in any 24-month window, the Bayesian lift from observing inversion is moderate (perhaps 1.5-2x the base rate), not the near-certainty implied by "7/7."

### Claim 2: The "Steepening Trap" Is a Narrative Fallacy

**BIAS AUDIT: Narrative fallacy, confirmation bias, unfalsifiable framing**

The steepening trap thesis states: "recession arrives during steepening, not inversion." Examine what this actually claims:

**Temporal flexibility makes it unfalsifiable.** The steepening phase can last 6-18+ months. Claiming recession arrives "during steepening" is effectively claiming recession arrives "at some point after inversion ends," which is trivially true for any recession that follows an inversion — it must arrive after the curve has un-inverted (or while un-inverting). This is a near-tautology, not a prediction.

**The mechanism is underspecified.** Why would steepening cause recession? The thesis implies that the Fed cutting rates (which steepens the curve) is itself a recessionary signal — but this is simply restating that the Fed cuts during or before recessions, which is already known. The "steepening trap" repackages a well-known fact (Fed easing often comes too late) as a novel pattern discovery.

**Counterexamples.** The curve steepened significantly in 2019 after its inversion — no recession arrived until the exogenous COVID shock in 2020. One can argue COVID "doesn't count," but this is special pleading. The curve has steepened and re-steepened multiple times without recession (mid-1990s, 2012-2013 taper tantrum). The thesis selectively counts confirming cases.

**The "markets celebrate un-inversion" claim is straw-manning.** Which markets? The S&P 500 did not rally on un-inversion in 2007 — it had already peaked in October 2007 before full un-inversion occurred. The claim that there is a reliable behavioral pattern of market complacency during un-inversion needs empirical verification that has not been provided.

### Claim 3: Term Premium Models Create a Precision Illusion

**BIAS AUDIT: Overconfidence, anchoring on model outputs**

The KB repeatedly treats ACM and Kim-Wright decompositions as factual measurements of an observable quantity. They are not. Key problems:

**30-50bp divergence on a 50-100bp estimate.** When the claimed term premium level is 50-80bp (ACM) and the model divergence is 30-50bp, the signal-to-noise ratio approaches 1:1. Stating that "term premium accounts for the majority of the 2s10s slope" when the slope is ~20-40bp and model uncertainty is 30-50bp means the statement is within model error bounds of being false.

**Estimation instability.** Both ACM and Kim-Wright models are affine term structure models with different identifying assumptions. Their estimates are sensitive to sample period selection, number of principal components, and assumptions about risk premia stationarity. The "adjusted estimate" of 80-130bp mentioned in the KB (adjusting ACM's 50-80bp upward) involves a subjective correction that compounds rather than resolves uncertainty.

**Post-QE structural break.** The KB itself acknowledges that QE/QT has created a structural break, and that the post-QT sample is ~3 years — too short for reliable estimation. Yet it simultaneously uses these models to make specific quantitative claims about current term premium levels. This is internally contradictory: you cannot simultaneously argue the models are unreliable due to regime change AND cite their specific outputs as evidence.

### Claim 4: Fiscal Supply → Term Premium Is Not a Universal Law

**BIAS AUDIT: Availability bias, monocausal reasoning, international counterexamples**

The KB's central narrative — that $2T+ Treasury issuance mechanistically drives term premium higher — treats one historical correlation as a causal law. Counterexamples:

**Japan (1990-present).** Japan's government debt/GDP rose from ~60% to ~260% with massive JGB issuance. The 10Y JGB term premium remained compressed for decades, often near zero or negative. The standard response is "BOJ bought it all," but this demonstrates that central bank behavior dominates fiscal supply — exactly the variable the fiscal supply thesis treats as secondary.

**United States 2020-2021.** The US ran the largest peacetime fiscal deficits in history ($3.1T in 2020, $2.8T in 2021) while the term premium was deeply negative. Again, QE was the dominant force. The fiscal supply argument requires the assumption that QE is "over" and won't return — an assumption, not a fact.

**United States 1942-1945.** Debt/GDP rose from ~40% to ~120% with massive war issuance. Long rates were pegged via yield curve control. The term premium was effectively set by policy, not by supply/demand.

**The argument requires price-insensitive demand to disappear.** The petrodollar erosion and BOJ normalization narratives are real but their magnitudes are speculative. Petrodollar recycling has been declining for two decades without producing term premium increases proportional to the KB's implied elasticity. BOJ normalization is proceeding very gradually (25bp increments) and Japanese institutions have strong home bias that limits the substitution effect.

### Claim 5: The Reflexive Loop Is a Conjunction Fallacy

**BIAS AUDIT: Conjunction fallacy, availability bias (UK Truss), single-scenario thinking**

The reflexive term premium loop requires: (a) term premium rises enough that (b) r > g for a sustained period, and (c) fiscal authorities fail to consolidate, and (d) the central bank does not intervene with yield curve control or QE, and (e) market participants do not reprice the probability of (d), which would itself compress term premium. Each condition has a probability less than 1, and they must jointly hold.

**The UK Truss analogy fails on specifics.** The gilt crisis was triggered by: (i) an unfunded fiscal event announced without OBR scoring, (ii) into an LDI-leveraged pension system that created a mechanical selling cascade, (iii) by a government with no electoral mandate for its program, (iv) in a country with no reserve currency and limited monetary sovereignty. None of these conditions apply to the United States. Using this as the precedent for a US doom loop is availability bias — it is vivid and recent, so it feels representative, but it is structurally non-analogous.

**Japan provides the counter-scenario.** Japan has had r > g for brief periods, debt/GDP at 260%, and no reflexive crisis — because the BOJ intervened and domestic institutions absorbed issuance. The US has more monetary sovereignty than the UK, more reserve currency privilege, and a more diversified investor base. The reflexive loop is possible but its probability is far lower than the narrative implies.

### Claim 6: N=2 Does Not Establish "Thresholds"

**BIAS AUDIT: Anchoring, small sample illusion, false precision**

The KB claims: "Historical thresholds: ~200bp+ associated with 1967-68 flip; ~0bp associated with 1998-2000 flip." This is presented as if these are empirically established levels. In reality:

**Two data points define a line, not a distribution.** With N=2 regime transitions in the US post-war period, there are zero degrees of freedom for estimating a threshold with any confidence interval. The 200bp and 0bp levels are simply what happened to prevail at those two moments — they are descriptive observations, not estimated parameters.

**The structural context differs radically.** 1967-68 featured Bretton Woods, no securitized fixed income market, no risk parity, no basis trade, different regulatory capital requirements, and fundamentally different market microstructure. The 1998-2000 transition occurred during a government surplus, LTCM-driven flight to quality, and the tech bubble's equity mania. Comparing term premium levels across these regimes as if they represent a stable functional relationship is anachronistic.

**The KB acknowledges this but proceeds anyway.** The open questions section correctly asks "Are historical threshold levels (~150bp) applicable given different market structure?" — but the concept is still assigned confidence 7/10 and used as an input to other analyses. The analytical framework should be downgraded until this fundamental question is addressed.

### Claim 7: The Vol-Regime Framework Is Circular

**BIAS AUDIT: Circularity, model-dependency**

The framework states: MOVE low → curve signals expectations → reliable; MOVE high → term premium noise contaminates → unreliable. The circularity:

**MOVE is derived from Treasury option prices, which embed the same term structure information.** When MOVE is high, it may simply mean that the term structure is uncertain — which is tautologically equivalent to saying the yield curve signal is unreliable. The framework adds no independent information; it restates the uncertainty in a different metric.

**The natural experiment is contaminated.** The 2019 vs 2022-23 comparison is cited as a "clean natural experiment," but these episodes differ in every relevant dimension: policy rate level, QE/QT regime, fiscal backdrop, inflation environment, labor market conditions, global supply chains. A natural experiment requires controlling for confounders — this comparison controls for nothing.

**Operationally, the framework is not actionable.** If the signal can only be used when MOVE is low, and MOVE is only low during calm periods when recession risk is already perceived as low, then the framework tells you the curve is reliable precisely when you least need it and unreliable precisely when you most need it.

### Claim 8: Systematic Overconfidence Across the KB

**CALIBRATION ASSESSMENT**

The KB assigns confidence 7/10 to the following claims, all of which rest on substantially uncertain foundations:

| Concept | KB Rating | Assessed Rating | Key Issue |
|---------|-----------|-----------------|-----------|
| yield_curve_term_premium_decomposition | 7 | 5 | Model-dependent, 30-50bp uncertainty on 50-80bp signal |
| steepening_trap | 7 | 4 | N=3 confirming cases, unfalsifiable framing, COVID counterexample |
| term_premium_dynamics | 7 | 5 | Japan/2020-21 counterexamples, model uncertainty |
| yield_curve_vol_regime_dependence | 7 | 4 | Circularity acknowledged but unresolved |
| term_premium_fiscal_signal | 7 | 5 | Post-QE structural break acknowledged but estimates still cited |
| term_premium_steepener | 7 | 5 | Decomposition is model-dependent artifact |
| term_premium_leading_indicator | 7 | 3 | N=2 threshold data points, radically different structural contexts |

**Why this matters operationally:** Confidence 7/10 suggests a claim is "well-supported with minor gaps" and suitable for moderate position sizing. Confidence 4-5/10 suggests "directionally plausible but empirically fragile" — appropriate for hypothesis tracking, not portfolio construction. The 2-3 point gap between KB ratings and calibrated ratings represents a meaningful overconfidence that, if acted upon, would lead to inadequate hedging and excessive concentration.

---

## Confidence Assessment

| Claim # | Description | Confidence | Justification |
|---------|-------------|------------|---------------|
| 1 | "7/7" record is misleading | 8/10 | Well-documented false positive problem in academic literature (Engstrom & Sharpe 2019). Base rate argument is arithmetically verifiable. |
| 2 | Steepening trap is narrative fallacy | 7/10 | Strong logical argument about unfalsifiability. COVID counterexample is clean. Slightly lower because the directional pattern (recession follows easing) is real even if repackaged. |
| 3 | Term premium models create precision illusion | 9/10 | Signal-to-noise ratio is arithmetically demonstrable. Model divergence relative to estimate magnitude is a mathematical fact, not an interpretive claim. |
| 4 | Fiscal supply thesis has major counterexamples | 8/10 | Japan counterexample is irrefutable. 2020-21 episode is recent and clean. The thesis may still be directionally correct for current conditions but is not a universal law. |
| 5 | Reflexive loop is conjunction fallacy | 7/10 | Logical structure is sound but the direction of TP risk may still be correctly identified even if the extreme scenario is overweighted. |
| 6 | N=2 thresholds are meaningless | 9/10 | This is a statistical truism. Zero degrees of freedom cannot estimate parameters. Not a matter of interpretation. |
| 7 | Vol-regime framework is circular | 6/10 | Circularity argument is strong but the framework may still have pragmatic value even if theoretically circular — similar to how technical analysis can "work" via self-fulfilling prophecy. |
| 8 | Systematic overconfidence in KB ratings | 8/10 | Meta-assessment consistent with Tetlock's finding that domain experts are systematically overconfident. The specific 2-3 point downgrade is a judgment call, not a mathematical proof. |

---

## Connections to Other Topics

**Credit Cycles & Spread Analysis (iter_0029):** The term premium precision illusion directly contaminates credit spread analysis that uses Treasury term premium as a "risk-free" decomposition input. If term premium estimates carry 30-50bp uncertainty, then credit spread decompositions inheriting these inputs have at least that much additional uncertainty — a point likely underappreciated in the credit analysis.

**Fiscal Dominance (iter_0016):** The reflexive loop critique connects to the broader fiscal dominance analysis. The Japan counterexample suggests fiscal dominance can persist for decades without a crisis — the "gradual path" may be the modal outcome rather than the "acute path," and the KB may be anchored on vivid acute episodes (Truss, eurozone) rather than the more probable gradual ones.

**Equity Cycles (iter_0024):** The steepening trap critique matters for equity cycle timing. If the steepening trap is not a reliable timing signal, then equity cycle analyses that incorporate it as a "Tier 2b signpost" are building on sand. The equity cycle framework needs to acknowledge this fragility explicitly rather than treating the yield curve as a validated leading indicator.

**Volatility Regimes (iter_0010):** The circularity critique of the MOVE-based regime framework suggests the volatility regime analysis may be less independently validated than claimed. If MOVE and term premium are jointly determined by the same underlying curve dynamics, using one to validate the other is double-counting evidence.

**Real Estate / CRE (iter_0030):** The "term premium drives CRE valuations" claim inherits all of the term premium measurement uncertainty. If the true term premium is anywhere in the 30-130bp range (spanning the KB's own estimates), the implied CRE valuation impact ranges from modest to severe — that uncertainty should be made explicit rather than presenting a point estimate.

**Monetary Policy:** The entire yield curve analytical framework is downstream of assumptions about central bank reaction functions. If the Fed (or BOJ, or ECB) responds to term premium dislocations with QE, yield curve control, or other interventions, the "natural" term premium dynamics discussed in the KB become hypothetical rather than predictive. The analysis systematically underweights the endogeneity of central bank behavior.

---

## Open Questions

1. **What is the actual false positive rate of yield curve inversion as a recession predictor, using a consistent definition of "inversion" and "prediction window" applied prospectively rather than retrospectively?** This is empirically answerable and has not been rigorously done in the KB.

2. **Can the steepening trap thesis be formulated as a falsifiable prediction?** As currently stated, it cannot. What specific 2s10s level, over what time horizon, with what decomposition, would constitute a "steepening trap" signal versus a normal steepening? Without these parameters specified ex ante, the concept has no predictive content.

3. **What would it take to resolve the ACM vs Kim-Wright divergence?** Is there a model-free term premium estimator, or is the concept of "term premium" inherently model-dependent and therefore inherently uncertain to 30-50bp? If the latter, this uncertainty should propagate through every downstream analysis.

4. **Why does the fiscal supply → term premium mechanism work in the US 2023-2026 but not in Japan 1995-2026 or the US 2020-2021?** The standard answer ("BOJ/Fed bought it all") simply moves the question to: under what conditions does the central bank absorb supply? This is a question about central bank reaction functions, not about fiscal supply per se, and the KB should reframe accordingly.

5. **Is the "term premium leading indicator" for correlation regimes actually adding information beyond what a simple moving average of realized stock-bond correlation provides?** If a model-dependent, low-frequency indicator (term premium) performs no better than a model-free, high-frequency observable (rolling correlation), Occam's razor favors the simpler metric.

6. **What is the KB's forecasting track record?** Across 30 iterations, have the confidence-weighted claims made in prior iterations been validated or falsified by subsequent data? Without this self-audit, the calibration assessment above is itself speculative. The KB should implement a systematic prediction tracking mechanism.

7. **How should "model-dependent uncertainty" be treated in a decision framework?** The KB frequently acknowledges model uncertainty in open questions but then assigns confidence ratings as if the point estimates were correct. A framework for propagating model uncertainty through confidence ratings — analogous to sensitivity analysis in quantitative models — is needed but absent.
