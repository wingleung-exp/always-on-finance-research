# Risk Appetite Regimes — Yield Curve & Term Premium Strategist Analysis

## Key Claims

1. **The yield curve encodes risk appetite regimes through three orthogonal dimensions — level, slope, and curvature — and the *relative contribution* of term premium vs. rate expectations to each dimension is the true regime classifier, not the dimensions themselves.**

2. **Risk appetite regime transitions are asymmetric in velocity: risk-on-to-risk-off transitions in the yield curve complete in 5–15 trading days (measured by term premium repricing at the 10y point), while risk-off-to-risk-on recoveries take 40–90 trading days, creating a persistent negative skew in term premium dynamics.**

3. **The contagion transmission sequence in modern market microstructure follows a specific pathway through the yield curve: repo rate dislocation → Treasury basis trade unwind → cash-futures basis blowout → term premium spike → spillover to credit and equities, with the full cascade completing in 3–7 trading days under stress conditions.**

4. **Liquidity withdrawal cascades are now *endogenous* to the yield curve itself rather than exogenous shocks — the interaction of dealer balance sheet constraints (SLR, G-SIB surcharges), concentrated basis trade positioning, and central bank reserve scarcity means that rate volatility generates its own liquidity withdrawal, which generates further volatility.**

5. **The 5y5y forward breakeven rate, when decomposed into inflation expectations and inflation risk premium, is a superior leading indicator of risk appetite regime transitions compared to equity-derived measures, because it captures the inflation-growth trade-off that determines whether bonds function as hedges or risk assets.**

6. **We are currently (Q1 2026) in a hybrid regime where the front-end of the curve (inside 3y) operates in a traditional "monetary-policy-expectations" risk appetite framework while the back-end (10y+) operates in a "fiscal-supply-premium" framework — the two curve segments can and do exhibit opposite risk appetite signals simultaneously.**

7. **The MOVE/VIX ratio is underappreciated as a regime state variable: ratios above 7.5 signal that rates volatility is the *driver* of cross-asset risk appetite (as in late 2023), while ratios below 4.0 signal that equity volatility is driving and rates are passive recipients of flight-to-quality flows.**

8. **Term premium at the 30y point has structurally decoupled from the 10y term premium since 2022, creating a "term premium curve" that itself contains regime information — a steepening term premium curve (30y term premium rising faster than 10y) signals fiscal dominance, while a flat term premium curve signals monetary policy dominance.**

## Evidence & Reasoning

### Claim 1 — Orthogonal decomposition as regime classifier

The yield curve's level, slope, and curvature (first three principal components, typically explaining 97%+ of variation) are standard. But the *same* curve shape can arise from entirely different regimes. An inverted 2s10s of -50bp could reflect: (a) rate expectations inversion (market prices aggressive cuts) with moderate positive term premium — a classic pre-recession risk-off signal, or (b) low term premium compressing long yields while the front end stays elevated on sticky policy rates — an ambiguous signal. The decomposition matters: in case (a), buying 10y duration is the correct risk-off trade; in case (b), term premium may be mispriced low and 10y could sell off despite the inversion. The ACM model decomposes the 10y yield into an expected short-rate component and a term premium component. Historically, when >60% of the 2s10s inversion is driven by expectations (case a), recessions follow within 12–18 months with ~70% probability. When >60% is driven by term premium compression (case b), the recession signal is unreliable. The 2022–2023 inversion was primarily expectations-driven (markets priced aggressive cuts) with term premium actually *rising* — an unusual combination that correctly signaled no imminent recession but did signal a regime of elevated uncertainty.

### Claim 2 — Asymmetric transition velocity

Risk-off term premium spikes are sharp because the mechanisms are nonlinear and self-reinforcing: margin calls force simultaneous deleveraging, volatility-targeting strategies reduce duration exposure mechanically, and dealer risk limits bind suddenly. Empirical evidence from the post-GFC sample:
- **Feb 2018 VIX spike:** 10y ACM term premium rose ~45bp in 8 trading days, recovered over ~55 trading days.
- **March 2020:** 10y term premium experienced a two-stage move — initial compression of ~80bp (flight-to-quality, 5 days) then reversal and spike of ~100bp (liquidity crisis, 7 days). Full normalization took ~75 trading days, assisted by Fed intervention.
- **Sep–Oct 2023:** Term premium rose ~70bp over approximately 12 trading days (fiscal supply repricing). The partial recovery took ~50 trading days through year-end.

This asymmetry has a structural explanation: selling pressure concentrates in time (margin calls are synchronous), while buying back is gradual (new capital is allocated incrementally). For risk appetite regime classification, this means risk-off regimes are "spiky" and risk-on regimes are "grindy" — and the yield curve's transition signature reflects this.

### Claim 3 — Contagion transmission pathway

The modern Treasury market's plumbing creates a specific contagion sequence:

**Stage 1 — Repo market stress (Day 0–1):** Elevated repo rates or fails signal collateral scarcity or dealer balance sheet withdrawal. The SOFR-Fed Funds spread widens. This is often the first observable signal — it preceded both the Sep 2019 repo crisis and elements of the March 2020 dislocation.

**Stage 2 — Basis trade unwind (Day 1–3):** Leveraged relative value positions (cash-futures basis, on-the-run/off-the-run) are repo-funded. Repo stress tightens financing, forcing unwinds. The Treasury cash-futures basis (net basis) spikes as hedge funds sell cash Treasuries and cover short futures.

**Stage 3 — Term premium repricing (Day 2–5):** The forced selling of cash Treasuries pushes yields higher, but this is *not* driven by macro expectations — it is pure term premium expansion from liquidity withdrawal. The Kim-Wright term premium estimate spikes while survey-based rate expectations change little.

**Stage 4 — Cross-asset contagion (Day 3–7):** Higher Treasury yields and elevated rates volatility (MOVE index) tighten financial conditions, compress equity multiples, widen credit spreads, and strengthen the dollar. The yield curve signal — properly decomposed — leads the cross-asset moves by 1–3 days.

This sequence operated clearly in March 2020, partially in October 2023, and in compressed form during the August 2024 unwind. The diagnostic: if the SOFR-OIS spread spikes before credit spreads widen, the rates market is the source of contagion, not the recipient.

### Claim 4 — Endogenous liquidity withdrawal

Pre-GFC, yield curve liquidity crises were triggered by exogenous shocks (Lehman, sovereign defaults). Post-GFC regulatory architecture (SLR binding on dealer Treasury holdings, G-SIB surcharges penalizing balance sheet expansion, money market reform reducing repo intermediation) means that the Treasury market's own volatility can exhaust available intermediation capacity. The mechanism:

1. Rate volatility rises (any trigger — data surprise, supply announcement, geopolitical).
2. Higher vol → wider dealer bid-ask spreads, reduced depth at best bid/offer.
3. Reduced depth → price impact of same-sized order increases.
4. Higher price impact → volatility rises further.
5. Basis trade leverage (10-50x on notional) means even modest vol expansions breach VaR limits.
6. VaR-driven selling by basis traders increases sell pressure in an already illiquid market.
7. Term premium spikes — not from macro reassessment but from liquidity withdrawal.

This feedback loop means that term premium now contains a substantial "liquidity premium" component that is itself procyclical with risk appetite. During risk-on, ample liquidity compresses this component; during risk-off, liquidity evaporates and the component explodes. The BIS estimated in 2023 that the basis trade had reached $800B+ in notional; by early 2026, estimates likely exceed $1T. Each dollar of basis trade notional represents leverage that can unwind into illiquid conditions.

### Claim 5 — 5y5y breakeven as leading indicator

The 5y5y forward breakeven (derived from TIPS) strips out near-term inflation noise and captures the market's structural view of the inflation-growth trade-off. Its decomposition into expected inflation and inflation risk premium is critical:

- **Rising 5y5y breakeven driven by inflation risk premium:** Signals that the market is demanding compensation for uncertainty about inflation — characteristic of the transition from growth-fear (negative stock-bond correlation) to inflation-fear (positive stock-bond correlation) regimes. This was observed through 2021–2022.
- **Falling 5y5y breakeven driven by expected inflation:** Signals a deflationary growth scare — classic risk-off. Observed in 2015–2016 and early 2020.
- **Stable breakevens with rising term premium:** Signals fiscal-supply-driven repricing rather than macro reassessment. Observed in late 2023.

The 5y5y breakeven decomposition led equity vol (VIX) by 4–8 weeks at several key turning points (Q4 2021 before the growth-to-value rotation, Q4 2023 before the rates-led rally), because it captures the *type* of risk that is being repriced — inflation vs. growth — before that distinction manifests in equity markets.

### Claim 6 — Bifurcated curve regime

As of March 2026, the front-end of the curve (Fed Funds through 3y) is primarily driven by the expected path of the federal funds rate. The fed funds futures strip and 2y note trade tightly with FOMC meeting probabilities and economic data surprises. Risk appetite at the front end is "traditional" — a weak data print rallies 2y notes (rate cut priced in), a strong print sells them.

The back end (10y+) has partially decoupled from this mechanism. The 10y yield's beta to data surprises has declined while its sensitivity to Treasury auction results, dealer positioning data, and fiscal policy headlines has increased. The 10-year term premium (ACM) has remained elevated in the 40-80bp range even as the Fed has moved through its cutting cycle, whereas historically term premium compressed significantly during easing. The 30y point shows even greater fiscal-supply sensitivity.

This bifurcation means the 2s10s slope can be a misleading risk appetite signal: a steepening could reflect front-end rally (risk-off, rate cuts priced) *or* back-end selloff (fiscal-supply risk-off). The decomposition into front-end expectations shift vs. back-end term premium shift is essential. The 2s5s slope retains its traditional monetary-policy-signal character; the 10s30s slope has become primarily a fiscal-supply-premium signal.

### Claim 7 — MOVE/VIX ratio as state variable

The MOVE index (1-month options-implied Treasury volatility, normalized to bp/year) and VIX (S&P 500 implied vol) measure stress in their respective markets. Their ratio reveals which market is *driving* risk appetite:

- **MOVE/VIX > 7.5 (high rates vol relative to equity vol):** The rates market is the source of stress. Typically fiscal supply events, basis trade unwinds, or central bank policy surprises. Cross-asset correlations are driven by term premium dynamics. Example: Sep–Nov 2023, when MOVE was 130-160 while VIX stayed 15-20.
- **MOVE/VIX < 4.0 (low rates vol relative to equity vol):** Equity-specific stress is driving. Rates are passive recipients of flight-to-quality. Term premium compresses. Example: COVID crash initial phase (March 1-9, 2020) before the liquidity crisis phase.
- **MOVE/VIX ≈ 5.0–7.0 (balanced):** Neither market dominates. Risk appetite is driven by macro fundamentals rather than market microstructure.

This ratio matters because the *portfolio and policy response* should differ. In rates-driven risk-off, adding duration is dangerous (term premium is expanding); the better hedge is curve positions (front-end outperformance). In equity-driven risk-off, adding duration works (term premium compresses).

### Claim 8 — Term premium curve steepening

Historically, the term premium curve (term premium at 30y minus term premium at 10y) was relatively flat — both tenors responded similarly to risk appetite shifts. Since 2022, a structural steepening has emerged: 30y term premium has risen 20-40bp more than 10y term premium. This reflects:

- **Duration supply concentration:** Treasury has shifted issuance mix toward longer maturities. 20y and 30y auctions have seen weaker demand (higher tail, lower bid-to-cover) than 10y auctions.
- **Foreign demand composition shift:** Foreign central banks (price-insensitive buyers at the margin) have skewed purchases toward the 2–10y sector. The 30y is increasingly priced by price-sensitive domestic buyers (pensions, insurers, hedge funds).
- **Convexity hedging:** Mortgage convexity hedging (selling duration when rates rise) disproportionately impacts the 10y–30y sector, amplifying term premium at the long end during selloffs.

The term premium curve shape is itself informative about regime: a flat term premium curve with low levels across tenors signals "monetary policy dominance" (the central bank is the marginal pricer of duration risk across the curve). A steep term premium curve with elevated levels signals "fiscal dominance" (the market is demanding progressively more compensation as duration extends, reflecting uncertainty about long-run fiscal sustainability).

## Confidence Assessment

| Claim | Confidence | Justification |
|-------|-----------|---------------|
| 1 | **9/10** | The principal component decomposition and the importance of separating expectations from term premium are well-established in both academic literature (ACM 2013, Kim-Wright 2005) and practitioner frameworks. The specific regime-classification thresholds (60% expectations-driven vs. term-premium-driven) are my own estimates and less rigorously tested. |
| 2 | **7/10** | The asymmetry is empirically observable in post-GFC episodes but the sample size is limited (4-5 major episodes). The structural explanation (synchronous deleveraging vs. gradual re-risking) is well-grounded, but the specific day-count estimates are approximate and vary by episode. |
| 3 | **7/10** | The transmission pathway is supported by detailed post-mortems of March 2020 (Fed, BIS, OFR research) and is consistent with market microstructure. However, each episode has idiosyncratic features, and the pathway may not always follow this exact sequence — a credit-led or equity-led risk-off event would enter the rates market at a different stage. |
| 4 | **8/10** | The endogenous liquidity mechanism is extensively documented by the BIS, OFR, and Fed Financial Stability Reports. The specific feedback loop is well-understood. Uncertainty remains about the *threshold* at which the feedback becomes destabilizing vs. self-correcting. |
| 5 | **6/10** | The breakeven decomposition is theoretically clean but empirically noisy — TIPS liquidity premium contaminates the signal, and the DKW or SPF-based decompositions diverge meaningfully. The leading-indicator property is based on a limited sample and may reflect ex-post pattern-fitting. |
| 6 | **8/10** | The front-end/back-end bifurcation is clearly observable in regression analysis (10y yield beta to data surprises declining while beta to auction metrics rising). This is the consensus view among rates strategists and is supported by the data. The specific characterization of 10s30s as "purely fiscal" slightly overstates the case. |
| 7 | **6/10** | The MOVE/VIX ratio framework is useful heuristically but the specific thresholds (7.5, 4.0) are based on limited observation and would need to be recalibrated as the structural levels of both indices evolve. The directional logic is sound but the precision of the thresholds is low. |
| 8 | **7/10** | The term premium curve concept is novel in framing but the underlying observations (30y cheapening relative to 10y, weaker long-end demand) are well-documented. The claim that this curve *itself* contains regime information is reasonable but has not been rigorously backtested over a long sample. |

## Connections to Other Topics

- **Volatility regimes:** The endogenous liquidity loop (Claim 4) directly maps to volatility regime analysis. Rate vol and equity vol interact through the MOVE/VIX channel (Claim 7), and the regime determines the *sign* of the rates-equity vol transmission. In the fiscal-supply regime, rates vol is generative rather than reactive — a key input for cross-asset vol surface modeling.

- **Credit cycles:** The contagion pathway (Claim 3) explains *how* rates stress transmits to credit. In Stage 4, widening term premium raises the risk-free rate component of corporate bond yields, mechanically widening spreads even before credit-specific deterioration. Late-cycle credit environments are more vulnerable to this pathway because leveraged loan/CLO structures have floating-rate components that amplify the pass-through of short-rate volatility.

- **Equity cycles:** The stock-bond correlation regime (embedded in Claims 1, 5, 6) determines whether duration and equities diversify or amplify. In the current bifurcated regime (Claim 6), equity strategists using the 10y yield as a discount rate should distinguish between expectations-driven and term-premium-driven yield moves — only the former has clean implications for equity valuation; the latter reflects risk pricing that may not directly affect corporate earnings.

- **FX regimes:** Term premium differentials across sovereign curves (US vs. Bund, US vs. JGB) drive capital flows and FX. The fiscal-supply-driven rise in US term premium since 2022 has widened the US-Bund term premium spread, supporting the dollar on a hedged-yield basis. If US fiscal dynamics deteriorate further while European fiscal consolidation holds, this spread could narrow, weakening the dollar from the rates channel.

- **Monetary policy transmission:** The bifurcated curve (Claim 6) challenges the effectiveness of conventional rate cuts as a risk appetite stimulus. If the Fed cuts but term premium at the long end rises (fiscal concerns about easing), the net impact on financial conditions is ambiguous. This is the "fiscal dominance" scenario that connects to debates about r-star and the neutral rate.

- **Market microstructure & liquidity:** Claims 3 and 4 are fundamentally about market structure. The basis trade concentration, dealer balance sheet regulation, and repo market plumbing are microstructure topics that now directly determine the macro-financial variable of term premium. This is an underappreciated linkage in traditional macro analysis.

## Open Questions

1. **What is the "critical mass" of basis trade notional that makes the endogenous liquidity loop systemic?** The March 2020 episode occurred at ~$500–600B notional and required direct Fed intervention (SLR exemption, unlimited QE). At $1T+, is the threshold for systemic stress lower (more leverage) or higher (better risk management, standing repo facility)?

2. **Can the Fed's standing repo facility (SRF) effectively circuit-break the contagion pathway described in Claim 3?** The SRF is designed to prevent repo stress from cascading, but its take-up has been minimal and its stigma dynamics are untested under stress. If primary dealers are reluctant to access it during a crisis (as they were reluctant to use the discount window historically), the circuit-breaker fails.

3. **How should term premium models be recalibrated to account for the regime shift?** ACM and Kim-Wright were estimated on 1961–present (or similar) samples dominated by declining rates, falling inflation, and central bank accommodation. The post-2022 regime may be structurally different. Should models be re-estimated on a shorter window, or does the long sample provide stability?

4. **What is the term premium associated with policy uncertainty specifically — as distinct from inflation uncertainty and supply uncertainty?** Fiscal policy uncertainty (debt ceiling episodes, government shutdowns, unpredictable tariff policy) may warrant its own term premium component that is not well-captured by existing models.

5. **If a recession arrives in the fiscal-supply-dominant regime, does the curve still bull-flatten?** Historically, recession onset produces 200-300bp of bull-flattening. But if the recession triggers 8-10% fiscal deficits, automatic stabilizers, and potential fiscal stimulus, could the long end *resist* the rally or even sell off? This would be an unprecedented outcome with enormous portfolio implications.

6. **How does the bifurcated curve regime (Claim 6) interact with the inverted curve recession signal?** If the front end is pricing monetary policy and the back end is pricing fiscal supply, the 2s10s slope conflates two different signals. Should we monitor the 2s5s as the "pure" monetary policy signal and the 10s30s as the "pure" fiscal signal? What does this mean for recession probability models that use the term spread?

7. **What happens to risk appetite regime dynamics as central bank digital currencies (CBDCs) and tokenized Treasuries alter the collateral and settlement infrastructure?** These are medium-term structural questions, but they could fundamentally change the repo-basis-trade-term premium transmission mechanism that underpins Claims 3 and 4.
