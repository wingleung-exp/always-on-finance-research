# Risk Appetite Regimes — Yield Curve & Term Premium Strategist Analysis

## Key Claims

1. **Risk appetite regimes are most reliably identified through term premium dynamics, not yield levels.** The level of yields conflates rate expectations with risk compensation; only by decomposing yields into expected short rates and term premium can one distinguish genuine risk-on/risk-off shifts from monetary policy repricing. A compression of term premium below 0 bp (as estimated by ACM or Kim-Wright models) signals a risk-seeking regime; a rapid expansion above +100 bp at the 10-year tenor signals a risk-averse or "term premium tantrum" regime.

2. **The yield curve encodes at least four distinct risk appetite regimes, each with a characteristic term structure signature:**
   - **Risk-On / Reflation:** Curve steepens via bear steepening (long rates rise faster than short rates), term premium expands modestly, breakevens widen. The 2s10s slope moves toward +100–200 bp.
   - **Risk-Off / Recession Fear:** Curve inverts or flattens aggressively via bull flattening (long rates fall faster), term premium compresses as duration becomes a hedge asset, flight-to-quality suppresses long yields. 2s10s moves below 0 bp.
   - **Complacency / Reach-for-Yield:** Curve is moderately steep but term premium is anomalously low or negative, credit spreads are tight, vol is suppressed. The 5y5y forward rate drifts lower despite no fundamental improvement in neutral rate estimates.
   - **Fiscal Dominance / Supply Shock:** Curve steepens via term premium expansion driven by issuance fears, not growth optimism. Long-end cheapens on a real yield basis while breakevens may be stable. Auction tails widen. This regime is distinct from reflation because credit spreads widen simultaneously.

3. **The transition between risk appetite regimes is driven more by term premium regime shifts than by changes in rate expectations.** Between 2020 and 2025, the majority of large yield curve moves—the 2021 bear steepening, the 2022 inversion, the October 2023 selloff, and the 2024–25 re-steepening—were predominantly term premium events, not rate expectation events, when properly decomposed.

4. **Hedge fund basis trade positioning in Treasury futures has become a structural amplifier of risk appetite regime transitions.** The leveraged short basis trade (short cash Treasuries, long futures) reached $800B+ in notional by late 2024/early 2025. Unwinds of this position during risk-off episodes create self-reinforcing term premium spikes that accelerate the transition from complacency to risk-aversion regimes, as seen in the March 2020 Treasury market dislocation and echoed in subsequent stress episodes.

5. **The 5y5y forward real rate is the cleanest single measure of where the market prices the long-run risk appetite regime.** When 5y5y real forwards are below estimated r* (roughly 1.0–1.5% in real terms for the US), the market is in a structurally risk-seeking posture for duration. When they exceed r* by more than 50 bp, the market is demanding meaningful compensation for macro uncertainty—a risk-averse posture for fixed income that typically spills into cross-asset risk appetite.

6. **Foreign official sector demand is a slow-moving but powerful regime determinant.** The secular decline in foreign official Treasury holdings (from ~33% of outstanding marketable debt in 2015 to ~22% by early 2026) has structurally raised the equilibrium term premium, shifting the baseline from which risk appetite regimes oscillate. This means that even "risk-on" regimes in the current era feature higher term premium than risk-off regimes of the 2010s.

7. **The repo market and Treasury bill supply function as the "plumbing" that either enables or constrains risk appetite regime persistence.** When the repo-OIS spread is tight and bill supply is ample (providing high-quality collateral), leveraged risk-taking is facilitated and risk-on regimes can persist. When repo stress emerges (wide spreads, reserve scarcity), it acts as an early warning that the risk-on regime is fragile—often before equity vol or credit spreads signal anything.

## Evidence & Reasoning

**Claim 1 — Term premium as regime identifier:**
The ACM model estimated 10-year term premium at approximately -100 bp in mid-2020 (extreme risk-seeking in duration, driven by QE and flight-to-safety), rising to approximately +60 bp by October 2023 (the "term premium tantrum" that took 10y yields to 5%). During this same period, rate expectations (the expected path of fed funds) moved by roughly 400 bp cumulatively. But the *regime-defining* moves—the ones that correlated with cross-asset risk appetite shifts—were the term premium moves. The equity selloff in Q3 2023 correlated with term premium expansion, not with changes in expected policy rates. This is because term premium reflects the *price of uncertainty* while rate expectations reflect the *central tendency*—and risk appetite is fundamentally about the price of uncertainty.

**Claim 2 — Four regime taxonomy:**
- *Reflation (H1 2021):* 2s10s widened from ~80 bp to ~155 bp. ACM term premium rose from -60 bp to roughly flat. 10y breakevens rose from 2.0% to 2.5%. Credit spreads tightened. Classic risk-on steepening.
- *Recession Fear (2022 inversion):* 2s10s inverted to -108 bp (July 2022, deepest since early 1980s). Kim-Wright term premium compressed to roughly -50 bp at the 10y even as policy rates rose 500 bp. Duration was a hedge—risk-off regime despite hawkish Fed.
- *Complacency (early 2024):* 2s10s at roughly -30 to 0 bp, ACM term premium ~+20 bp, VIX sub-15, IG spreads at ~90 bp. Markets priced 150 bp of cuts and a soft landing simultaneously. The 5y5y nominal forward was ~4.0%, below most estimates of nominal neutral.
- *Fiscal Dominance (Oct 2023, echoed in late 2025):* 10y yields rose from 4.0% to 5.0% in Q3 2023. ACM term premium surged +80 bp in two months. But the catalyst was the Treasury refunding announcement (larger-than-expected coupon issuance), not a change in Fed expectations. IG credit spreads *widened* slightly—ruling out reflation as the driver.

**Claim 3 — Term premium drives regime transitions:**
Decomposing the 10-year yield into ACM components across the 2020–2025 period: the October 2023 selloff was ~70% term premium, ~30% rate expectations. The 2024 rally was ~60% term premium compression (as Treasury shifted issuance toward bills), ~40% rate cut expectations. The 2022 inversion was ~80% rate expectations (Fed hiking cycle) but the *depth* of inversion was amplified by term premium compression at the long end. In each case, the term premium component was the marginal driver of the regime-relevant signal.

**Claim 4 — Basis trade as amplifier:**
OFR and Fed research documented the basis trade at $800B+ notional by late 2024. The mechanism: hedge funds short cash Treasuries and go long futures to capture the cash-futures basis (~15–30 bp annualized). This trade is leveraged 20–50x via repo. During risk-off episodes, repo financing tightens, margin calls force unwinds, which means forced *buying* of futures and *selling* of cash Treasuries—widening the basis further and disrupting the cash market. This was the proximate cause of the March 2020 Treasury dysfunction and has created a fragility overhang since. The concentration of this trade means that risk appetite regime transitions can become non-linear.

**Claim 5 — 5y5y real forward as regime barometer:**
The 5y5y real forward (derived from TIPS) has ranged from approximately -0.5% (2020–2021, deep risk-seeking) to +2.3% (late 2023, risk-averse for duration). As of early 2026, estimates of the real neutral rate (r*) range from 1.0% (NY Fed Holston-Laubach-Williams) to 1.5% (market-implied). When the 5y5y real forward is significantly below this range, duration is "cheap to own" on a risk-adjusted basis, enabling leveraged risk-taking. When it exceeds r* by 50+ bp, fixed income itself becomes a source of risk rather than a diversifier, which constrains cross-asset risk appetite.

**Claim 6 — Foreign demand regime shift:**
Treasury International Capital (TIC) data show foreign official holdings of Treasuries declining from ~$4.1 trillion (2015) to ~$3.6 trillion (end of 2025), while total marketable debt has grown from ~$13 trillion to ~$27 trillion. This share decline from ~33% to ~22% removes a price-insensitive buyer that historically suppressed term premium. Warnock and Warnock (2009) estimated that foreign official purchases reduced 10y yields by 80–100 bp. The reversal of this trend structurally elevates term premium by an estimated 30–60 bp relative to the 2010s baseline, meaning the "zero line" for term premium in risk appetite terms has shifted upward.

**Claim 7 — Repo as plumbing constraint:**
The September 2019 repo spike (overnight repo to 10%) was a precursor to the March 2020 Treasury market dislocation. More recently, the drawdown of the Fed's Reverse Repo Facility (RRP) from $2.5 trillion (peak 2022) to near-zero by mid-2025 has reduced the liquidity buffer in the system. When reserves become scarce relative to bank demand, repo rates spike, financing costs for leveraged positions rise, and the system's capacity to support risk-taking contracts. The SOFR-IORB spread is a real-time indicator: when persistently positive, risk appetite plumbing is functioning; when it spikes or becomes volatile, the regime is fragile.

## Confidence Assessment

| Claim | Confidence | Justification |
|-------|-----------|---------------|
| 1. Term premium as regime identifier | **8/10** | Strongly supported by academic literature (e.g., Bauer & Rudebusch, Wright) and empirical decomposition. Model dependence (ACM vs Kim-Wright diverge by 40–80 bp at times) introduces some uncertainty. |
| 2. Four-regime taxonomy | **7/10** | Historically well-supported, but regime classification is inherently subjective. The "fiscal dominance" regime is the most novel and least tested—only 2–3 clear episodes since 2020. Boundaries between regimes are blurry in real time. |
| 3. Term premium drives transitions | **7/10** | Decomposition results depend heavily on model choice. ACM and Kim-Wright sometimes disagree on whether a move was expectations or term premium. The qualitative conclusion is robust; the precise attribution ratios are model-dependent. |
| 4. Basis trade as amplifier | **8/10** | Well-documented by regulators (OFR, BIS, Fed). The mechanism is clear and the March 2020 precedent is unambiguous. Uncertainty lies in whether the next stress episode will follow the same pattern or whether regulatory changes have altered the dynamics. |
| 5. 5y5y real forward as barometer | **7/10** | Conceptually clean but requires an estimate of r* that is itself highly uncertain. The HLW model has wide confidence intervals (±150 bp). The signal is most useful at extremes. |
| 6. Foreign demand regime shift | **8/10** | TIC data are noisy but the trend is clear. The magnitude of the term premium impact is uncertain (Warnock estimates are 15+ years old and the elasticity may have changed). |
| 7. Repo plumbing as constraint | **8/10** | September 2019 and March 2020 are clear evidence. The RRP drawdown and reserve dynamics are well-tracked. The SOFR-IORB spread is observable in real time. Uncertainty is in the *threshold* at which plumbing stress becomes binding. |

## Connections to Other Topics

- **Monetary policy transmission:** Risk appetite regimes are the *channel* through which monetary policy affects financial conditions. A rate cut in a "fiscal dominance" regime may fail to ease financial conditions if term premium continues to rise—the so-called "pushing on a string" problem. The yield curve shape determines whether policy is stimulative or restrictive beyond the overnight rate.

- **Credit markets and corporate finance:** The risk appetite regime determines whether credit spread compression is driven by genuine fundamentals (risk-on/reflation) or by technical reach-for-yield (complacency). In the complacency regime, IG and HY spreads can reach historically tight levels despite deteriorating fundamentals—creating fragility. The transition from complacency to risk-off typically produces the sharpest credit spread widening.

- **Equity valuation and factor rotation:** The term premium component of long rates is far more relevant for equity duration (growth stock valuations) than rate expectations. A rise in 10y yields driven by term premium expansion compresses equity multiples; the same rise driven by higher growth expectations may *support* multiples. The regime matters more than the level.

- **Dollar and FX dynamics:** Risk appetite regimes interact with yield differentials to drive FX flows. A US "fiscal dominance" regime that raises US term premium may attract capital inflows (supporting the dollar) initially, but if it reflects fiscal unsustainability, it eventually triggers dollar weakness—the timing of this transition is one of the hardest calls in macro.

- **Central bank balance sheet policy (QE/QT):** QE compresses term premium and facilitates complacency/risk-on regimes. QT does the reverse but with asymmetric speed—QE effects were immediate; QT effects have been gradual until they suddenly aren't (September 2019). The Fed's balance sheet trajectory is a structural input to the risk appetite regime.

- **Fiscal policy and sovereign credit:** The emergence of the "fiscal dominance" regime as a distinct risk appetite state is a post-2020 development driven by the rapid expansion of US government debt from ~80% to ~100%+ of GDP. This connects to sovereign credit risk analysis and the question of whether US Treasuries can continue to function as the global risk-free asset.

- **Volatility regimes:** Interest rate volatility (MOVE index) is both a consequence and a cause of risk appetite regime transitions. MOVE above 120 typically signals a regime transition is underway; MOVE below 80 is consistent with the complacency regime. The MOVE/VIX ratio reveals whether the regime stress is rates-led (fiscal/supply) or equity-led (growth/earnings).

## Open Questions

1. **How do we calibrate the "fiscal dominance" term premium threshold?** At what level of term premium does the market signal that fiscal supply is the dominant driver rather than macro expectations? The October 2023 episode suggests ~+50 bp ACM term premium may be a threshold, but the sample is too small to be confident.

2. **Has the basis trade reached a size that makes Treasury market dislocations a recurring feature of risk-off transitions?** If so, does this fundamentally alter the diversification properties of Treasuries in multi-asset portfolios, and does it change the equilibrium level of term premium investors demand?

3. **Where is the reserve scarcity threshold for the current banking system?** The Fed's QT has reduced reserves from ~$4 trillion to ~$3.2 trillion (est. early 2026). Most estimates place the "ample reserves" floor at $2.5–3.0 trillion, but the true threshold is only revealed in a stress event.

4. **Can the term premium models (ACM, Kim-Wright) reliably distinguish between expectations and term premium in real time, or are the decompositions only useful in hindsight?** Real-time vintage estimates have historically been revised substantially. This is a fundamental limitation of the entire analytical framework.

5. **How does the emergence of non-bank intermediaries (money market funds, hedge funds, insurance/pension) as marginal Treasury buyers change the term premium sensitivity to supply?** The "buyer of last resort" for Treasuries is increasingly price-sensitive private capital rather than price-insensitive central banks—does this permanently steepen the supply-term premium elasticity?

6. **What is the interaction between US risk appetite regimes and global term structures?** With the BOJ exiting yield curve control and European fiscal expansion (post-2025 defense spending), are global term premium dynamics becoming more correlated or more divergent? A global term premium repricing could overwhelm domestic US factors.

7. **Does the current 2s10s slope (estimate: +30 to +60 bp range as of early 2026) reflect a "normal" post-inversion steepening or the beginning of a fiscal dominance steepening that has further to run?** The answer determines whether the steepener trade is crowded and late, or still in its early innings.
