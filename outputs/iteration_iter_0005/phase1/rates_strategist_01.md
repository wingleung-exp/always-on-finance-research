# Risk Appetite Regimes — Yield Curve & Term Premium Strategist Analysis

## Key Claims

1. **Risk appetite regimes are identifiable through a composite of yield curve shape, term premium level, and the covariance structure between rates and equities — not through any single spread or indicator.**

2. **Term premium is the primary channel through which risk appetite transmits into the yield curve; shifts in risk appetite regimes cause term premium to move 50-150bp over a cycle, dwarfing the impact of expectations shifts at the long end.**

3. **The sign and magnitude of the stock-bond correlation is the most reliable real-time classifier of risk appetite regimes: positive correlation signals an inflation-fear regime (risk-off drives both stocks down and bonds down), while negative correlation signals a growth-fear regime (risk-off drives stocks down but bonds up as safe havens).**

4. **The current regime (as of early 2026) is a "fiscal-supply-dominant" risk appetite framework — a historically unusual state where risk-off episodes can steepen the curve rather than flatten it, because fiscal concerns contaminate the traditional safe-haven bid for duration.**

5. **Yield curve butterfly spreads (2s5s10s, 5s10s30s) are more sensitive regime-change detectors than simple slope measures, because they capture the nonlinear way risk appetite shifts redistribute demand across the curve.**

6. **Three distinct risk appetite regimes have characterized the post-GFC era — "central-bank-suppressed" (2012–2019), "pandemic-reflation" (2020–2021), and "fiscal-supply-aware" (2022–present) — each with fundamentally different yield curve signatures and term premium dynamics.**

7. **Forward term premium (e.g., the 5y5y term premium) is a leading indicator of regime transitions, typically moving 3–6 months before spot term premium confirms the shift, because institutional investors adjust long-duration positioning before the consensus narrative changes.**

8. **Hedge fund basis trade positioning (leveraged long cash Treasuries / short futures) has become a structurally important amplifier of risk appetite regime transitions, creating pro-cyclical dynamics where risk-off triggers forced unwinds that push term premium higher precisely when flight-to-quality would historically compress it.**

## Evidence & Reasoning

### Claim 1 — Composite identification required
No single yield curve metric reliably classifies risk appetite. The 2s10s slope inverted in 2022-2023 during a tightening cycle but also inverted in 2006-2007 under very different risk conditions. The VIX captures equity vol but misses rates-specific dynamics. Term premium captures duration risk pricing but not credit or liquidity components. The regime must be identified by combining: (a) curve shape (level, slope, curvature), (b) decomposed term premium at multiple tenors, (c) rates-equity covariance, and (d) cross-market implied vol ratios (MOVE/VIX). Each regime produces a recognizable fingerprint across these dimensions.

### Claim 2 — Term premium as the transmission channel
When risk appetite shifts, the expected path of short rates adjusts modestly (typically 25-75bp as recession/easing probabilities change), but term premium moves far more dramatically. During 2020 COVID risk-off, 10y term premium (ACM model) fell approximately 150bp in weeks. During the 2022-2023 fiscal/supply repricing, 10y term premium rose roughly 100-150bp (depending on model). The reason: risk appetite directly governs investors' willingness to bear duration risk. A shift from risk-on to risk-off can either compress term premium (traditional safe-haven bid) or expand it (fiscal-supply concern), but the magnitude is large either way.

### Claim 3 — Stock-bond correlation as regime classifier
The stock-bond correlation was consistently negative from roughly 2000-2021 (growth-fear dominant — bad news for growth was bad for stocks but good for bonds). This flipped intermittently positive in 2022-2023 as inflation became the dominant risk (bad inflation news was bad for both stocks and bonds). The 60-day rolling correlation between S&P 500 returns and 10y Treasury returns provides a clean, model-free classification:
- Sustained negative correlation → growth-fear regime (bonds are hedges)
- Sustained positive correlation → inflation-fear regime (bonds are risk assets)
- Unstable/oscillating correlation → transition regime

This matters enormously for portfolio construction: in the inflation-fear regime, the "60/40 portfolio" loses its diversification benefit, and demand for long-duration Treasuries falls, pushing term premium higher.

### Claim 4 — Fiscal-supply-dominant regime
Post-2022, risk appetite has operated in a framework where fiscal deficits running 6-7% of GDP during non-recessionary periods generate persistent supply pressure. In this regime, a risk-off shock produces two competing forces: (a) flight-to-quality compresses the front end and belly of the curve, but (b) fiscal supply concerns and potential rating/deficit fears widen term premium at the long end. The net result is risk-off episodes that steepen rather than flatten the curve — the opposite of the pre-2020 pattern. The August 2023 and October 2023 selloff, where long-end yields surged despite equity weakness, was an early manifestation. The key diagnostic: if 30y yields rise during equity drawdowns of >5%, the fiscal-supply regime is dominant.

### Claim 5 — Butterflies as regime detectors
The 2s5s10s butterfly captures the curvature of the intermediate curve. In a "normal" risk-off (flight-to-quality), the belly outperforms — the butterfly becomes more negative as 5s rally relative to wings. In the fiscal-supply regime, the belly still benefits from easing expectations but the long end cheapens from supply, producing a different butterfly signature. The 5s10s30s butterfly is especially diagnostic: if it widens (30s underperform) during risk-off, this confirms fiscal-supply dominance. These nonlinear signatures appear 1-2 weeks before simple slope measures confirm the regime.

### Claim 6 — Three post-GFC regimes
**Central-bank-suppressed (2012-2019):** QE compressed term premium to near-zero or negative levels. 10y ACM term premium averaged roughly -25bp. Risk appetite was governed by forward guidance credibility and "taper tantrum" dynamics. Curve was flat-to-inverted despite no recession, because term premium suppression dominated. Risk-off episodes produced sharp bull-flattening.

**Pandemic-reflation (2020-2021):** Massive fiscal+monetary response crushed short rates to zero and forward rates reflected reflation. Term premium initially collapsed (pandemic flight-to-quality, Fed purchases) then began rising. Curve steepened dramatically (2s10s went from ~10bp to ~160bp). Risk appetite was pro-cyclical and straightforward — bear steepening on good news, bull flattening on bad.

**Fiscal-supply-aware (2022-present):** Term premium has risen structurally as markets price persistent fiscal deficits, QT, and reduced foreign official demand. 10y term premium (Kim-Wright) has moved from near-zero to 50-80bp+. Risk-off dynamics are ambiguous — front-end rallies but long-end can sell off. The curve shape is no longer a clean monetary policy signal.

### Claim 7 — Forward term premium as leading indicator
Institutional investors with long-duration mandates (pensions, insurers, sovereign wealth funds) adjust exposure at the margins before consensus views shift. This shows up first in 5y5y forward space because: (a) it strips out near-term policy expectations, (b) it is where structural demand/supply is most price-sensitive, and (c) it is where convexity hedging flows concentrate. Empirically, the 5y5y forward term premium began rising in late 2021, months before the spot 10y term premium confirmed the regime shift in 2022. Similarly, it peaked in Q4 2023 before the spot term premium rolled over.

### Claim 8 — Basis trade amplification
Leveraged Treasury basis trades (hedge funds long cash Treasuries, short futures, earning the basis at 10-50x leverage) have grown to an estimated $800B-1T+ in notional. In a risk-on regime, these flows absorb Treasury supply and compress term premium. In a risk-off regime, margin calls and VAR shocks force rapid unwinds — selling cash Treasuries into an illiquid market. This creates a pro-cyclical dynamic: risk-off → basis unwinds → yields spike → term premium rises → further risk-off. The March 2020 Treasury market dislocation and September-October 2019 repo crisis both demonstrated this amplification mechanism. The basis trade has effectively become the marginal pricer of term premium, making regime transitions sharper and more violent than the underlying macro shift would warrant.

## Confidence Assessment

| Claim | Confidence | Justification |
|-------|-----------|---------------|
| 1 | **9/10** | Well-established in academic and practitioner literature; no serious debate that multi-factor approaches dominate single-indicator approaches. |
| 2 | **8/10** | Strong empirical support from ACM and Kim-Wright decompositions across cycles. Modest uncertainty because term premium is model-dependent — different specifications can attribute more to expectations. |
| 3 | **8/10** | Robust empirical pattern, but the transition zones are noisy and the rolling window length matters. The post-2022 correlation has been unstable, complicating clean classification. |
| 4 | **7/10** | This regime hypothesis fits the 2022-2025 data well but has limited historical precedent (the last comparable fiscal environment was arguably the 1980s). Could be overfit to a specific episode. If deficits narrow or Fed restarts QE, the regime would shift. |
| 5 | **6/10** | Theoretically sound and supported by anecdotal pattern recognition, but rigorous backtesting is limited. Butterfly spreads are noisy and influenced by many factors (dealer hedging, mortgage convexity) beyond risk appetite. |
| 6 | **8/10** | The three-regime framework is a useful simplification with clear empirical support, but the boundaries are fuzzy and sub-regimes exist within each period. |
| 7 | **6/10** | The leading-indicator property is observed in the 2021-2023 episode but the sample is small. Forward term premium can also move due to supply technicals (e.g., Treasury refunding announcements) unrelated to regime shifts. |
| 8 | **8/10** | The mechanism is well-documented (BIS, Fed research, TBAC presentations). The exact sizing of basis trades is uncertain, but the directional impact on regime transition dynamics is supported by multiple episodes. |

## Connections to Other Topics

- **Monetary policy transmission:** Risk appetite regimes determine whether rate cuts are bullish-flatteners (growth-fear regime, traditional) or met with long-end selloffs (fiscal-supply regime, if cuts are seen as inflationary or fiscally irresponsible). The yield curve's reaction function to policy is regime-dependent.

- **Credit spreads & corporate bonds:** In the growth-fear regime, credit spreads and term premium are positively correlated (both widen in risk-off). In the inflation-fear regime, they can diverge — credit may perform while duration sells off, because the economy is still strong but inflation erodes bond value.

- **Equity factor rotations:** Negative stock-bond correlation (growth-fear regime) supports long-duration equity factors (growth, quality). Positive correlation (inflation-fear regime) favors short-duration equity factors (value, high-dividend). Regime identification from the yield curve is directly actionable for equity factor timing.

- **Dollar & FX dynamics:** Term premium shifts affect carry attractiveness and thus USD demand. A rising-term-premium regime driven by fiscal supply tends to strengthen USD (higher real yields) unless it triggers sovereign risk concerns (rare for the US but relevant for EM).

- **Volatility regime analysis:** MOVE index (rates vol) and VIX (equity vol) comovement is regime-dependent. In the central-bank-suppressed regime, MOVE was structurally low and disconnected from VIX. In the fiscal-supply regime, MOVE has risen structurally and often leads VIX.

- **Fiscal sustainability & sovereign risk:** The fiscal-supply-aware regime is a manifestation of the market gradually pricing sovereign fiscal dynamics into the term premium. If this persists, it represents a structural shift in how sovereign credit risk enters rates pricing in developed markets.

- **Global rates linkages:** Risk appetite regimes tend to synchronize across developed market yield curves (UST, Bunds, JGBs, Gilts), but with different term premium levels reflecting local fiscal and central bank dynamics. The Bund-Treasury spread contains information about relative fiscal risk appetite.

## Open Questions

1. **Is the fiscal-supply regime permanent or cyclical?** If deficits narrow (spending cuts, revenue growth) or the Fed eventually restarts balance sheet expansion, term premium could recompress and revert to the pre-2022 regime. How much of the current term premium is "structural" vs. cyclical?

2. **What is the threshold for basis trade unwinds to trigger systemic stress?** The March 2020 episode required Fed intervention. With basis trades now larger, is the threshold for dislocation lower or higher (due to better risk management post-2020)?

3. **Can the stock-bond correlation sustainably return to negative territory without a recession?** If inflation settles near 2% and growth slows gradually, does the correlation flip back, or has the fiscal-supply regime permanently raised the probability of positive correlation?

4. **How should term premium models be recalibrated for a high-deficit, positive-supply-shock environment?** ACM and Kim-Wright were estimated on data dominated by the disinflationary, low-supply era. Their estimates for 2024-2026 may be biased by training data that doesn't represent current structural conditions.

5. **What role does foreign official demand play as a regime variable?** If China and Japan continue reducing Treasury holdings while Gulf states increase, does the composition of foreign demand change the term premium's sensitivity to risk appetite?

6. **How do we distinguish "genuine" risk appetite shifts from positioning-driven moves?** If basis trade unwinds cause term premium to spike, and that spike triggers equity selling, is it a "real" risk-off regime or a technical dislocation? The policy and portfolio implications differ substantially.

7. **What does the next recession look like through a yield curve lens in the fiscal-supply regime?** Historically, recessions produce massive bull-flattening as the Fed cuts and duration is bid. But if the recession triggers fiscal expansion (automatic stabilizers + stimulus), could the long end actually sell off during a recession — an unprecedented outcome?
