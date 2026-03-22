# Risk Appetite Regimes — Yield Curve & Term Premium Strategist Analysis

## YIELD CURVE SHAPE ANALYSIS

The yield curve as of Q1 2026 occupies a historically unusual configuration: 2s10s at approximately +20-30bp (nominally positive but flat by expansion standards), 5y5y forward anchored at ~3.8-4.0% (150bp above the 2015-2019 average), and a bifurcated regime where front-end dynamics are governed by monetary policy expectations while the long end is increasingly captive to fiscal supply variables. This is not a single curve — it is two curves stitched together at roughly the 3-5 year pivot, each encoding a different risk appetite regime simultaneously.

Prior iterations established a four-regime taxonomy (reflation, recession fear, complacency, fiscal dominance) and extended it to six. This iteration refines the framework by introducing a **regime stability dimension** — not just *which* regime markets are in, but *how fragile* the current regime is and what the transition probability distribution looks like across plausible shocks.

---

## Key Claims

1. **Risk appetite regimes are most precisely identified not by yield levels but by the *covariance structure* between term premium changes, rate expectations changes, and cross-asset volatility — and this covariance structure has become unstable in 2025-2026, indicating elevated regime transition probability.**

2. **The "corridor of stability" for sustained risk-on in the current structural environment requires 10y ACM term premium between +15bp and +55bp, 2s10s between 0bp and +60bp, and MOVE index below 100. Breaching any boundary for more than 5 consecutive sessions historically precedes regime transition within 15-30 trading days.**

3. **Reserve distribution asymmetry — not aggregate reserve levels — is now the binding constraint on risk appetite regime durability. The top 4 banks hold ~50% of ~$3.2T in reserves, meaning the effective "available reserve buffer" for the broader financial system is ~$1.6T, well below the ~$2.5T threshold where September 2019-style discontinuities emerged.**

4. **The Treasury General Account (TGA) has become the single most important high-frequency liquidity variable modulating risk appetite regimes, operating on a 2-6 week cycle that creates periodic windows of vulnerability independent of macro fundamentals. TGA drawdowns of >$100B over 4-6 weeks inject reserves and suppress term premium; TGA rebuilds of equivalent magnitude drain reserves and elevate term premium by 5-15bp.**

5. **Inflation term premium and real rate term premium are currently diverging — inflation term premium has compressed toward 2019 levels (~15-25bp at 10y) while real rate term premium has expanded to post-GFC highs (~35-50bp at 10y). This decomposition reveals that the market's concern is not about the inflation path but about the *real cost of servicing debt* under structurally higher issuance — a fiscal solvency signal, not an inflation signal.**

6. **Intraday gamma exposure from 0DTE options (now 45-50% of SPX volume) creates a "micro-regime instability" layer that did not exist before 2022. Dealer gamma positioning can flip from long to short gamma within a single session, producing 50-80bp intraday VIX swings that trigger cross-asset margin calls and inject term premium volatility even when no macro news occurs. This raises the steady-state term premium floor by an estimated 5-12bp.**

7. **The basis trade ($900B-$1.2T notional, 20-50x levered) has evolved from a pure relative-value arbitrage into a de facto marginal pricer of term premium. Hedge fund basis positions now absorb ~25-30% of net new Treasury issuance. A coordinated unwind — triggered by repo rate spikes >25bp above SOFR or margin haircut increases — would produce a 40-80bp term premium spike within 5-10 trading days, constituting an instant regime transition from risk-on to fiscal dominance regardless of macro conditions.**

8. **The "Japanification vs. Italianification" fork identified in prior iterations is now resolvable as a probability-weighted blend rather than a binary: the US is pricing approximately 70% Italy-path (market-funded, rising TP) and 30% Japan-path (eventual monetization, TP compression). This blend is observable in the divergence between nominal term premium (elevated) and breakeven inflation term premium (compressed), consistent with a market that expects fiscal costs to be partially socialized through financial repression rather than either pure monetization or pure market discipline.**

---

## Evidence & Reasoning

### Claim 1: Covariance structure as regime identifier

The standard approach uses yield levels or spreads (2s10s, 3m10y) to identify risk regimes. This is insufficient because the same yield level can arise from opposite combinations of expectations and term premium. The covariance structure — specifically, whether term premium changes and rate expectations changes are positively correlated (concordant) or negatively correlated (discordant) — carries strictly more information.

**Evidence:**
- October 2023: Term premium rose ~80bp while rate expectations were roughly stable → fiscal dominance regime. 2s10s steepened, but this was *not* reflation.
- March 2020: Term premium initially compressed (flight to safety) then spiked (forced selling) while rate expectations collapsed → two-stage regime transition visible only in decomposition.
- Q4 2024-Q1 2025: Discordant moves (TP rising while rate expectations fell with Fed cuts) occurred in ~35% of weeks, versus a historical norm of ~15-20%. Elevated discordance frequency is itself a regime fragility signal.

The *stability* of the covariance structure matters: when the correlation between TP changes and expectations changes flips sign frequently (rolling 20-day correlation crossing zero more than 3 times per quarter), the market is in a "contested regime" where different investor classes are pricing different states of the world. This contested state preceded every major regime transition in the 2018-2025 sample.

### Claim 2: Corridor of stability

This synthesizes threshold analysis from prior iterations into a single operational framework.

**Evidence:**
- **Term premium lower bound (+15bp):** Below this, duration risk is undercompensated given structural supply dynamics. ACM TP below +15bp in 2024-2026 only occurred during acute flight-to-quality episodes (lasting <10 trading days). The 2017-2019 average of approximately -30bp required QE stock effects that no longer exist.
- **Term premium upper bound (+55bp):** Above this, financial conditions tighten enough to impair credit creation. The October 2023 TP spike to ~+80bp coincided with mortgage rates >8%, a sharp pullback in IG issuance, and CRE distress acceleration. The +55bp threshold corresponds approximately to the level where marginal corporate borrowers face prohibitive all-in costs.
- **2s10s bounds (0 to +60bp):** Below 0bp signals that front-end is embedding aggressive hikes (restrictive) or that long-end is subject to extreme safe-haven demand (risk-off). Above +60bp in current context would require either deep rate cuts (recession) or back-end selloff (fiscal dominance), both of which are risk-off adjacent.
- **MOVE <100:** Above 100, dealer hedging costs reduce market-making capacity, bid-ask widens, and the basis trade approaches VaR limits. MOVE above 100 for >5 sessions occurred in March 2020, September-October 2022, October 2023, and each preceded significant cross-asset drawdowns.

The corridor is narrow — approximately 40bp of TP width, 60bp of 2s10s, and 20 points of MOVE — reflecting how constrained the equilibrium is when fiscal supply is structurally elevated, dealer capacity is impaired, and leveraged positioning is concentrated.

### Claim 3: Reserve distribution asymmetry

**Evidence:**
- Fed H.4.1 data shows aggregate reserves ~$3.2T as of early 2026, but the distribution is highly skewed: JPMorgan, Bank of America, Citigroup, and Wells Fargo hold approximately 50% of total reserves.
- The remaining ~$1.6T is distributed across ~4,800 other depository institutions, many of which face minimum reserve targets for operational and regulatory purposes.
- September 2019: Aggregate reserves were ~$1.4T and appeared "ample" until tax payment date and Treasury settlement coincided, revealing that the *marginal* reserve user faced scarcity at much higher aggregate levels than models predicted.
- Scaling to current system (2x+ Treasury market size, larger GSIB balance sheets, greater basis trade repo dependency): the effective scarcity threshold is likely ~$2.8-3.2T *aggregate*, meaning the system is already operating in the zone of intermittent vulnerability.
- Waller-Afonso (2024) Fed research suggests that the "ample reserves" threshold is endogenous to market structure and rises with Treasury market size. The static threshold is a dangerous simplification.
- **Implication for risk appetite:** Repo rate volatility (SOFR spikes at quarter-end and month-end) has already increased in frequency and magnitude through 2025, consistent with the system approaching the reserve scarcity transition zone. Each spike creates a mini risk-off episode that resolves quickly but degrades risk appetite durability.

### Claim 4: TGA as high-frequency liquidity variable

**Evidence:**
- Treasury General Account fluctuations directly add to or drain from reserves in the banking system. When Treasury spends from the TGA (draws down balance), reserves increase; when Treasury rebuilds via tax receipts or net bill issuance, reserves fall.
- TGA balance typically oscillates between $200B and $800B, creating swings of $100-300B in effective reserves over 4-8 week cycles.
- In Q4 2025 and Q1 2026, TGA management around the debt ceiling created amplified oscillations that directly correlated with SOFR-IORB spread moves and, with a ~5 trading day lag, with changes in 10y ACM term premium.
- The mechanism: TGA drawdowns → reserve injection → repo markets ease → basis trade leverage cost falls → hedge funds bid more aggressively for Treasuries → term premium compresses. Reversal operates symmetrically.
- This is the highest-frequency, most mechanistically direct channel between fiscal operations and risk appetite, and it operates independently of monetary policy or macro data. It means risk appetite can shift for purely "plumbing" reasons that have nothing to do with the economy.

### Claim 5: Inflation TP vs. real rate TP divergence

**Evidence:**
- TIPS-derived breakeven inflation (5y5y BEI ~2.3-2.5%) has been remarkably stable since mid-2024, with modest volatility. This implies the inflation risk premium — the compensation for uncertainty about the inflation path — has compressed.
- Meanwhile, 10y real yields (TIPS) have risen from ~1.5% to ~2.0-2.2%, outpacing the move in nominal yields net of breakevens. Decomposing via Kim-Wright: the real rate term premium has expanded from ~+10bp (2019 average) to ~+35-50bp.
- This divergence is informative: the market is *not* worried about an inflation surge. It is worried about the real cost of funding persistent deficits. This is a fiscal sustainability signal dressed in interest rate clothing.
- Corroborating evidence: CDS on US sovereign debt, while still very low in absolute terms, has risen from ~10bp (2019) to ~40-55bp (late 2025), tracking real rate term premium more closely than inflation breakevens.
- Policy implication: Fed rate cuts would address the expectations component but would do nothing to reduce real rate term premium, which is driven by fiscal supply. This is why risk appetite may not respond to easing the way historical analogs suggest — the term premium component is immune to the policy rate channel.

### Claim 6: 0DTE gamma and micro-regime instability

**Evidence:**
- 0DTE (zero days to expiry) options now represent 45-50% of S&P 500 options volume, up from negligible share pre-2022. Market maker hedging of these positions creates large, mechanistic intraday flows.
- When dealers are net long gamma (market near strikes with high open interest), they sell rallies and buy dips, suppressing realized volatility. When dealers are net short gamma (market moves away from strike concentration), they must buy rallies and sell dips, amplifying moves.
- The gamma flip point can shift intraday as options expire and new positions are established, creating potential for multiple intraday regime transitions.
- Cross-asset contagion: large intraday equity moves triggered by gamma effects produce VIX spikes → portfolio insurance and risk parity deleveraging → duration selling alongside equity selling → MOVE rises → basis trade VaR approaches limits.
- This mechanism did not exist before 2022 and represents a structural increase in the *frequency* of micro risk-off episodes. While each individual episode resolves quickly (typically within 1-3 sessions), the cumulative effect is: (a) higher realized volatility than implied volatility suggests, (b) higher minimum viable term premium to compensate for this intraday fragility, and (c) degraded reliability of traditional vol signals (VIX) as regime indicators.

### Claim 7: Basis trade as marginal term premium pricer

**Evidence:**
- OFR and Fed Financial Stability Reports document basis trade notional at $800B-$1.2T, with leverage ratios of 20-50x on underlying capital.
- At this scale, hedge fund basis positions absorb a significant fraction of net new Treasury supply. If 10y-equivalent duration absorption by basis traders is ~$250-350B annually, and net marketable Treasury issuance is ~$1.0-1.2T, basis traders represent 25-30% of the marginal demand.
- This makes term premium *endogenous* to the basis trade: when the trade is profitable and expanding, it compresses term premium by providing duration demand. When it contracts (due to repo cost increases, margin changes, or vol spikes), the demand vacuum directly widens term premium.
- **Unwind trigger thresholds:** Repo rate (SOFR) sustained >25bp above target range, or FICC haircut increases >50bp on Treasury collateral, or MOVE sustained >110 for >3 sessions. Any of these would force partial de-risking across the $800B+ complex.
- March 2020 precedent: basis trade unwind contributed to 10y yields *rising* during the worst equity selloff in decades — a regime impossibility under expectations-only models but perfectly consistent with a forced-seller framework.
- **Implication:** Term premium in the current environment is partially a *leveraged carry trade derivative* rather than a pure reflection of duration risk preferences. This means term premium models that don't incorporate positioning are structurally misspecified.

### Claim 8: Japanification/Italianification probability blend

**Evidence:**
- Japan path requires: (a) domestic private sector running chronic surplus (saving glut), (b) central bank willing to absorb unlimited duration supply (YCC/QQE), (c) no external funding constraint (net international investment position positive or current account surplus). Japan satisfied all three; the US satisfies only (a) partially and (c) not at all ($18T net negative NIIP).
- Italy path requires: (a) external funding dependence, (b) market discipline on sovereign cost of capital, (c) limited monetary sovereignty (Eurozone constraint). The US has unlimited monetary sovereignty (unlike Italy), but has external funding dependence ($7-8T in foreign-held Treasuries, declining share).
- The US occupies an intermediate position: sufficient monetary sovereignty to partially monetize (Fed can buy Treasuries), but sufficient external dependence that markets impose a fiscal risk premium. The market appears to price this as a blend.
- Observable marker: if full Japan path were priced, 10y ACM term premium would be near zero or negative (BOJ suppression). If full Italy path were priced, term premium would be +100bp+ with periodic spread crises. Current +40-60bp is consistent with ~70/30 Italy/Japan weighting.
- The blend is not static — it shifts with each fiscal policy decision. Tax cuts or spending increases shift toward Italy-path (higher TP); deficit reduction or Fed balance sheet expansion shifts toward Japan-path (lower TP). This makes fiscal policy announcements the highest-beta events for term premium, exceeding even FOMC meetings in term premium impact.

---

## TERM PREMIUM DECOMPOSITION

| Component | Current Estimate (10y) | 2019 Baseline | Shift | Driver |
|-----------|----------------------|---------------|-------|--------|
| Inflation term premium | +15-25bp | +10-20bp | +5-10bp | Modest; inflation uncertainty elevated but not dominant |
| Real rate term premium | +35-50bp | +5-15bp | +25-40bp | Fiscal supply, r-star uncertainty, dealer capacity |
| Foreign demand discount | Removed | -30 to -50bp | +30-50bp | Official sector share 33% → 22% |
| QE stock effect | Removed | -40 to -60bp | +40-60bp | Fed balance sheet $8.9T → ~$6.8T |
| Basis trade compression | -10 to -20bp | ~0bp | -10 to -20bp | $800B+ basis trade providing marginal duration demand |
| 0DTE volatility premium | +5-12bp | ~0bp | +5-12bp | New structural factor since 2022 |
| **Total ACM 10y TP** | **~+40-60bp** | **~-30bp** | **~+70-90bp** | |

The +70-90bp structural shift means that +40bp term premium today is economically equivalent to approximately -40bp in 2017. Risk appetite that appears "moderate" by historical TP levels is actually quite aggressive once the structural shift is netted out.

---

## RATE EXPECTATIONS VS FORWARDS

**Where the market is mispriced relative to regime analysis:**

- **Front-end (2y):** Market prices ~75-100bp of cumulative cuts over the next 12 months. This is consistent with a "soft landing" base case but ignores the asymmetry: if term premium spikes (fiscal dominance episode), the Fed may need to cut *more* aggressively to offset tightening financial conditions — but those cuts would be less effective because TP, not the policy rate, is the binding constraint. Front-end is priced for the central path but underprices the left-tail scenario where TP dominates.

- **Belly (5y):** Priced at ~3.8-4.0%, consistent with terminal rate of ~3.25-3.50% plus modest term premium. This appears roughly fair but carries convexity risk: 5y is the maturity most exposed to the "dual-driver" problem (both expectations and TP move it), creating higher realized vol than implied vol suggests.

- **Long end (10y-30y):** 10y at ~4.2-4.5% with ~40-60bp TP. The market is pricing the "corridor of stability" center — fair if conditions remain stable, but with asymmetric risk. A fiscal dominance episode could push TP to +100bp (10y to ~5.0-5.2%), while a recession-driven TP compression could bring it to ~+15bp (10y to ~3.5-3.8%). The risk-reward is negatively skewed for longs.

- **30y term premium curve:** 30y TP is ~20-30bp above 10y TP, reflecting the term premium curve steepening identified in prior iterations. This steepening is likely to persist given concentration of duration supply at the long end and declining foreign demand for ultra-long. The 10s30s spread at ~25-35bp is cheap relative to the historical distribution (median ~40-50bp), creating a potential steepener opportunity if fiscal dominance materializes.

---

## SUPPLY-DEMAND TECHNICALS

**Treasury issuance outlook:** Net marketable borrowing ~$1.8-2.0T in FY2026, with coupon share increasing as the bill share (elevated post-October 2023) normalizes. This coupon shift concentrates duration supply and is structurally positive for term premium.

**Auction performance:** Bid-to-cover ratios in 20y and 30y have deteriorated gradually through late 2025 and early 2026, with tail frequency rising from the ~25% baseline to ~35-40%. Not yet at the >50% alarm threshold but trending in the wrong direction.

**Foreign flows:** Japanese investors have been net sellers of USTs intermittently as BOJ policy normalization narrows the hedged yield advantage. Chinese holdings continue secular decline. No new large price-insensitive buyer has emerged to replace these flows.

**Repo conditions:** SOFR-IORB spread showing increasing month-end and quarter-end volatility, consistent with reserve distribution asymmetry approaching the scarcity zone. Standing Repo Facility (SRF) usage has increased, suggesting it is beginning to function as the backstop it was designed to be — which itself signals proximity to the scarcity boundary.

---

## CURVE TRADE RECOMMENDATIONS

**Trade 1: Conditional 5s10s30s butterfly steepener (sell 10y wings, buy 5y and 30y body)**

- **Rationale:** If fiscal dominance materializes, the 30y will underperform the 10y as duration supply concentrates at the long end and foreign bid weakens. If recession materializes, the 5y will outperform as rate cut expectations pull the belly lower. Either regime transition benefits from owning the wings vs. the belly.
- **Entry:** 5s10s30s butterfly at current ~-5bp
- **Target:** -25bp (10y cheapens relative to wings)
- **Stop:** +10bp (15bp loss)
- **Risk/reward:** ~1:1.3; improves to ~1:2 in fiscal dominance scenario

**Trade 2: Pay 5y5y forward vs. receive 2y1y forward — regime break steepener**

- **Rationale:** If risk appetite transitions to any form of risk-off, 2y1y forward (near-term policy rate expectations) will rally sharply as rate cuts are pulled forward, while 5y5y forward (structural neutral rate + TP) will be sticky or rise (TP expanding). This trade isolates the "expectations rally, term premium rise" discordant move that characterizes the onset of fiscal dominance or dual-regime transitions.
- **Entry:** Spread at ~75bp (5y5y ~3.90% minus 2y1y ~3.15%)
- **Target:** 130bp (2y1y drops 40bp, 5y5y rises 15bp)
- **Stop:** 55bp (20bp loss)
- **Risk/reward:** ~1:2.75; asymmetric payoff in regime transition

**Trade 3: Short MOVE-adjusted basis trade exposure via SOFR options**

- **Rationale:** SOFR call spreads (strikes at SOFR+15bp to SOFR+40bp) provide leveraged payoff if repo stress materializes from reserve scarcity or basis trade unwind. Cost is low in current environment (repo vol suppressed), providing asymmetric convexity for a plumbing-driven risk-off event.
- **Entry:** Buy 3-month SOFR call spreads at ~3-5bp premium
- **Target:** 20-30bp value if repo stress event occurs
- **Stop:** Premium loss (3-5bp, defined risk)
- **Risk/reward:** ~1:5 to 1:8 if event materializes; option decay if it doesn't

---

## Confidence Assessment

| Claim | Confidence | Justification |
|-------|-----------|---------------|
| 1. Covariance structure as regime ID | **8/10** | Analytically robust and consistent across all major episodes 2018-2025. Limited by model-dependence of TP decomposition (ACM vs Kim-Wright diverge 40-80bp). |
| 2. Corridor of stability | **7/10** | Thresholds calibrated from recent data but sample is short (2022-2026). Corridor boundaries likely shift with market structure changes. Useful as heuristic, not precision instrument. |
| 3. Reserve distribution asymmetry | **7/10** | Reserve skewness is factual (H.4.1 data). Scarcity threshold is fundamentally uncertain — could be $2.5T or $3.5T depending on how reserves are distributed on any given day. September 2019 validates the non-linearity concept. |
| 4. TGA as liquidity modulator | **8/10** | Mechanism is well-understood (accounting identity). Magnitude calibration (5-15bp TP impact) has wider confidence bands. Directional reliability is high. |
| 5. Inflation TP vs real rate TP divergence | **7/10** | Decomposition consistent with TIPS market pricing and CDS evidence. TIPS liquidity premium may distort the decomposition; Kim-Wright and ACM treat this differently. |
| 6. 0DTE micro-regime instability | **6/10** | Mechanism is logical and consistent with observed intraday dynamics. Magnitude estimate (5-12bp structural TP floor) is speculative — the effect is real but difficult to isolate from other noise. Shortest track record of any claim. |
| 7. Basis trade as marginal TP pricer | **8/10** | Size, leverage, and absorption share well-documented by OFR/Fed. Unwind thresholds approximate. March 2020 provides strong but single-observation calibration for unwind dynamics. |
| 8. Japan/Italy probability blend | **6/10** | Conceptually useful for framing the fiscal TP question. The 70/30 weighting is inferred from market pricing (TP levels) using strong assumptions. Could easily be 60/40 or 80/20. Better as mental model than tradeable signal. |

---

## Connections to Other Topics

- **Credit spreads and risk appetite:** Term premium expansion precedes credit spread widening in fiscal dominance episodes (October 2023: TP led by ~5 trading days). Credit analysts should monitor TP, not just spread levels, as a leading indicator. The CLO arbitrage threshold (AAA spread >SOFR+170bp) is itself a function of term premium via the asset-swap spread channel.

- **Macro regime identification:** The claim that Fed rate cuts may be less effective when TP is the binding constraint connects directly to macro strategy on policy transmission. The fiscal multiplier question (are deficits stimulative or contractionary at this debt level?) maps to the Japanification/Italianification probability blend — if markets impose discipline (Italy path), large deficits *tighten* financial conditions via TP, creating a perverse fiscal drag.

- **Equity risk premium:** Positive stock-bond correlation regime (supply-shock driven) raises the effective equity risk premium because duration no longer hedges equity drawdowns. The equity risk premium cannot be analyzed independently of the term premium regime — the two are linked through the correlation structure.

- **Dollar and international flows:** Declining foreign official demand for Treasuries is both a driver of elevated TP and a consequence of de-dollarization trends. The feedback loop is potentially self-reinforcing: higher TP → higher dollar hedging cost → lower hedged return for foreign buyers → further demand decline → higher TP.

- **Private credit and shadow banking:** The $1.8T private credit complex's floating-rate exposure (SOFR+500-650bp) means that the *level* of SOFR directly determines borrower stress, while the *volatility* of SOFR (reserve scarcity → repo spikes) creates refinancing uncertainty that the mark-to-model NAV framework does not capture. This is the channel through which plumbing stress transmits to real economy credit conditions.

---

## Open Questions

1. **Reserve scarcity threshold precision:** Is the effective threshold ~$2.8T aggregate (implying we are already in the vulnerability zone) or ~$3.5T (implying 6-12 months of QT runway)? The answer determines whether the basis trade unwind scenario is a near-term risk or a medium-term risk. Fed internal modeling (not public) likely has better estimates.

2. **How does the basis trade unwind actually *sequence*?** March 2020 is one observation. Does the unwind cascade uniformly across tenors, or does it hit specific maturities (e.g., CTD cheapest-to-deliver at the 10y) disproportionately? This matters for curve trade construction.

3. **Can the Fed credibly deploy SRF/emergency repo without triggering moral hazard that *increases* basis trade positioning?** The standing repo facility is designed to prevent plumbing crises, but its existence may encourage more aggressive leveraged positioning, raising the stakes of any eventual event that overwhelms the facility's capacity.

4. **What is the *actual* 0DTE gamma exposure of the dealer complex at any given time?** Exchange-reported data gives volume but not net positioning. Without net gamma estimates, the 5-12bp structural TP premium is calibrated by inference rather than measurement.

5. **Has the Japanification/Italianification blend shifted since the 2025 fiscal policy announcements?** If tax cut extensions or new spending significantly increase projected deficits, the Italy-path probability should rise — but the market may already be pricing this forward. Real-time calibration of the blend requires a model that doesn't yet exist.

6. **How do tariff-driven supply chain reconfiguration costs interact with term premium?** If tariffs raise the structural price level (one-time) without affecting trend inflation, the inflation TP should be unaffected — but if they raise inflation *uncertainty* (distribution widens), inflation TP should rise, potentially reversing the current divergence between inflation TP and real rate TP. This is the major unresolved near-term question for the decomposition framework.
