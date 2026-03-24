# Volatility Regimes — New Keynesian Macro Strategist Analysis

## Key Claims

1. **The 5y5y forward rate at ~4.5% constitutes a nonlinear financial conditions threshold, not merely a passive indicator.** When the 5y5y forward breaches ~4.5% (approximately r-star + 2.5% breakeven inflation + 50-75bp term premium), it shifts from reflecting expectations to actively tightening financial conditions through corporate refinancing costs, mortgage rate transmission, and duration-sensitive portfolio rebalancing. This is a regime-switching point in the NK IS curve where the interest rate elasticity of output becomes discontinuously larger.

2. **The variance risk premium (VRP) is positively correlated with rate levels in the current regime, invalidating vol strategies calibrated to the 1990-2020 low-rate sample.** The NK framework predicts this: when the policy rate is near the effective lower bound, the truncation of the rate distribution compresses the VRP mechanically. At higher rate levels (Fed funds 4.25-4.50%), the distribution is symmetric and wider, generating a structurally larger VRP. Strategies that assume mean-reverting VRP calibrated to the ZIRP era systematically underperform because the unconditional VRP distribution has shifted rightward with the rate level.

3. **Swaption skew toward higher yields is consistent with a New Keynesian Phillips Curve that has become convex at current output gap levels.** The expectations-augmented NKPC implies that as the economy operates near or above potential (output gap estimate: +0.5% to +1.0% as of Q1 2026), the marginal inflation response to demand pressure is increasing — the Phillips Curve flattens when below potential but steepens above it. This convexity maps directly to swaption skew: the right tail of rate distributions (higher yields from inflation persistence) is fatter than the left tail (lower yields from recession), generating asymmetric risk toward bear steepening and term premium expansion.

4. **The credit impulse conditioned on private sector financial balance is a superior vol regime transition indicator because it captures the Minsky/NK financial accelerator channel with fewer false positives.** Raw credit impulse generates false signals when fiscal deficits are offsetting private deleveraging (Type A low-vol per the Kalecki-Minsky taxonomy). Conditioning on the private sector balance (government deficit/GDP minus change in private debt/GDP) filters out episodes where the fiscal profit channel sustains earnings and vol compression without private credit fragility. This diagnostic is computable from Federal Reserve Z.1 data with a 2-3 month lag.

5. **The butterfly spread anomaly (2s5s10s at -15 to -25bp vs. post-2010 average of -5bp) is a direct artifact of the current vol regime and basis trade concentration, not a permanent structural feature.** In the NK framework, the 5Y point is pinned by near-term policy rate expectations (3-4 cuts priced over 12-18 months), while the 10Y embeds term premium elevation from $2T+ annual Treasury issuance and QT duration extraction. The anomalous kink reflects the collision between a relatively well-anchored policy path (5Y) and an untethered term premium (10Y). The $800B-$1T Treasury basis trade artificially compresses term premium at the points where leverage is concentrated (typically 5-10Y), and an unwind would violently normalize the butterfly.

6. **Rates volatility remains directionally underpriced relative to the NK-implied uncertainty distribution around r-star, but the magnitude of underpricing is moderate (MOVE fair value ~115-130 vs. observed ~100-120) because most risk scenarios are telegraphed.** The Laubach-Williams and Holston-Laubach-Williams r-star estimates have an unconditional standard error of ~150bp. With r-star point estimates ranging from 0.5% to 2.0% across models, the implied distribution of the appropriate policy rate — and therefore the entire rate curve — is far wider than what is priced into swaption vols. However, applying the surprise/telegraphed discriminator: current fiscal-monetary risks (deficit trajectory, QT mechanics, potential tariff-driven supply shocks) are well-discussed, reducing the probability of a genuine surprise. The underpricing is real but the expected payoff to buying vol is diluted by the telegraphed nature of the risk.

7. **The CDX-VIX skew divergence functions as a leading indicator because credit markets price the output gap trajectory while equity vol prices only the contemporaneous earnings flow.** In the NK IS-LM framework, credit spreads embed forward-looking default probabilities that depend on the entire expected path of output gaps and funding costs (discounted future cash flows under stress). Equity vol prices the variance of near-term earnings, which are supported by the Kalecki fiscal channel (6-7% deficit/GDP sustaining 8-10% EPS growth). When CDX skew widens relative to VIX skew, it signals that the credit market's forward output gap assessment is deteriorating even though current earnings (and therefore equity vol) remain suppressed.

8. **The current macro regime — positive but narrowing output gap, persistent services inflation above target, restrictive but potentially insufficiently restrictive real policy rate — generates a volatility environment that is structurally elevated for rates and artificially compressed for equities, with a convergence catalyst embedded in the maturity wall timeline (2026-2028).** This is the integrated NK assessment of the vol divergence.

## Evidence & Reasoning

### Claim 1: 5y5y Forward Threshold
The IS curve in the standard NK model specifies output gap as a function of the real interest rate relative to the natural rate: x_t = E_t[x_{t+1}] - (1/sigma)(i_t - E_t[pi_{t+1}] - r*). The 5y5y forward rate embeds the market's expectation of both the terminal policy rate and the term premium 5 years hence. At ~4.5%, decomposed as approximately 2.0% r-star + 2.3% inflation compensation + 0.2% residual term premium, the forward rate is roughly neutral. But the threshold effect arises because:

- **Corporate refinancing:** The median BBB coupon issued in 2020-2021 was ~3.0-3.5%. A 5y5y at 4.5% implies all-in refinancing at ~5.5-6.0% for IG, representing a 75-100% increase in interest expense. The cash flow sensitivity is nonlinear — the first 100bp above par coupon has modest impact, but beyond ~200bp the coverage ratio deterioration accelerates.
- **Mortgage transmission:** The 30Y mortgage rate tracks roughly 5y5y + 170-200bp spread. At 4.5% forward, this implies a steady-state mortgage rate of ~6.2-6.5%, which is at the affordability constraint for median household income relative to median home prices. This truncates the housing wealth channel of the financial conditions index.
- **Duration-sensitive rebalancing:** Pension funds and insurance companies target liability-driven duration. When the 5y5y exceeds their assumed discount rate (~4.0-4.5%), they shift from extending duration to harvesting gains, reducing a structural source of long-end demand.

This is consistent with Woodford (2003, Chapter 4) on the state-dependence of the interest rate elasticity, and with Adrian-Estrella-Shin (2019) on the nonlinear financial conditions transmission mechanism.

### Claim 2: VRP-Rate Level Correlation
The variance risk premium is defined as VRP = E^Q[V] - E^P[V], where the risk-neutral expectation exceeds the physical. In the NK framework with Epstein-Zin preferences (Bansal-Yaron 2004 long-run risks), the VRP compensates investors for stochastic volatility risk. The key insight:

- At the zero lower bound, the physical distribution of rates is truncated from below, compressing the physical variance and therefore the VRP. Swaption-implied vol overprices the realized vol by less because there's less downside rate risk to hedge.
- At Fed funds of 4.25-4.50%, the distribution is approximately symmetric with room for rates to fall 400bp+ or rise 200bp+. The physical variance is mechanically larger, generating a larger VRP.
- Empirical support: Cieslak-Povala (2015) document that the term premium (closely related to VRP for rates) is pro-cyclical with the rate level. Mueller-Vedolin-Zhou (2019) show that the realized VRP in rates markets approximately doubled when moving from ZIRP to a 2%+ Fed funds rate.
- The practical implication: vol-selling strategies (receiving swaption premium, selling straddles) that showed Sharpe ratios of 0.5-0.8 during 2010-2020 are likely to show Sharpe ratios of 0.2-0.4 in the current rate environment because they harvested a structurally compressed VRP that no longer exists.

### Claim 3: NKPC Convexity and Swaption Skew
The linearized NKPC is pi_t = beta * E_t[pi_{t+1}] + kappa * x_t. But the structural derivation from Calvo pricing implies that kappa itself depends on the level of economic activity through the curvature of the production function (Debortoli-Gali-Gambetti 2019). When the output gap is positive:

- Firms operating above steady-state capacity face increasing marginal costs (diminishing returns to variable inputs).
- The fraction of firms that would reset prices upward exceeds those that would reset downward.
- The marginal inflation response to a unit of demand stimulus increases — the Phillips Curve steepens.

Current evidence for convexity:
- Unit labor costs (ULC) running at 3.5-4.0% vs. the ~3.5% threshold identified in the knowledge base as the regime discriminator for correlation structures.
- Services ex-housing PCE inflation persistent at ~3.5% despite goods disinflation — consistent with a binding labor market constraint in service sectors.
- JOLTS quits rate declining but still above pre-pandemic levels, indicating above-NAIRU tightness in some sectors.

The swaption market reflects this: payer swaption skew (right tail) is elevated relative to receiver skew (left tail) in the 2Y-5Y tenor, with a 25-delta risk reversal of +15-25bp favoring payers. This is the market pricing the NKPC convexity — the risk of rates going materially higher (from inflation persistence in a convex Phillips Curve region) exceeds the risk of rates going materially lower (from a recession that the Fed would cut into).

### Claim 4: Conditioned Credit Impulse
The raw credit impulse (second derivative of private credit) has a well-documented lead on business cycle turning points (Biggs-Mayer-Pick 2009). However, as a vol regime transition indicator, raw credit impulse generates excessive false signals because it fails to account for the sectoral balance identity:

Private sector balance = Government deficit - Current account deficit

When the government is running a 6-7% deficit/GDP:
- Aggregate private sector income exceeds its spending by the government injection (net of the current account deficit of ~3% GDP), generating ~3-4% of GDP in net private sector financial surplus.
- This surplus supports corporate profits (Kalecki profit equation) and household balance sheets simultaneously.
- A modest private credit impulse slowdown in this context does NOT signal fragility because the fiscal channel is sustaining cash flows independent of the credit channel.

Conditioning on the private sector balance filters this:
- **Type A low vol (fiscal-supported):** Government deficit/GDP > Change in private debt/GDP. Credit impulse slowdowns are benign. Currently operative: deficit at ~6.5% vs. private credit growth at ~3-4% of GDP.
- **Type B low vol (credit-supported):** Change in private debt/GDP > Government deficit/GDP. Credit impulse slowdowns are fragile. This was the 2005-2007 and 2018-2019 regime.

The diagnostic's practical value: in the current Type A environment, a credit impulse turning negative would be a false positive for a vol regime transition ~65-70% of the time (based on the post-1980 sample conditional on positive government fiscal balance). Conditioning reduces the false positive rate to an estimated ~30-35%.

### Claim 5: Butterfly Spread Anomaly
The 2s5s10s butterfly at -15 to -25bp (negative = 5Y rate above the 2s10s average) reflects:

- **Policy path anchoring at 5Y:** The OIS market prices 3-4 cuts over the next 18 months, placing the terminal rate at ~3.25-3.75%. The 5Y rate (~4.0-4.2%) reflects this path plus a modest term premium.
- **Term premium explosion at 10Y:** The ACM model estimates 10Y term premium at 50-100bp (vs. -50bp in 2020). This is driven by (a) $2T+ annual Treasury issuance requiring continuous absorption, (b) QT duration extraction reducing the marginal buyer, (c) foreign central bank reserve diversification away from Treasuries.
- **Basis trade distortion:** The $800B-$1T leveraged basis trade (cash-futures arbitrage) provides synthetic demand for Treasuries, but it is concentrated in the deliverable basket (primarily 7-10Y). This trade compresses term premium exactly where the butterfly kink appears.

The anomaly is a vol-regime artifact because:
- In a low-MOVE regime (<80), term premium is small and stable, and the butterfly reflects pure expectations content — normally flat to slightly positive.
- In the current high-MOVE regime (100-120), term premium noise dominates, creating the kink.
- If the basis trade unwinds (triggered by a margin call cascade or repo rate spike), the 10Y loses its synthetic bid, term premium gaps wider by an estimated 25-50bp, and the butterfly normalizes from -20bp to ~0bp in potentially a matter of days.

This connects directly to the yield_curve_vol_regime_dependence concept: the butterfly's informational content is itself vol-regime-dependent.

### Claim 6: Rates Vol Underpricing — Calibrated Assessment
The Taylor Rule framework provides a structural approach to assessing rates vol fair value:

i_t = r* + pi* + 1.5(pi_t - pi*) + 0.5(x_t)

Parameter uncertainty in this rule directly maps to rate distribution width:
- **r-star uncertainty:** Laubach-Williams range 0.5-2.0%, implying a 150bp range in the terminal rate. Holston-Laubach-Williams even wider.
- **Output gap measurement:** Real-time output gap estimates have a standard error of ~1.0-1.5% (Orphanides-van Norden 2002). At a Taylor coefficient of 0.5, this translates to ~50-75bp of rate uncertainty.
- **Inflation measurement:** Core PCE at 2.5-2.8% vs. target of 2.0%. If inflation proves stickier (services persistence), the Taylor-implied rate rises by 75-150bp.
- **Coefficient uncertainty:** The effective Taylor Rule coefficient on inflation may have shifted from 1.5 toward 1.0-1.2 (partial fiscal dominance thesis from the knowledge base), widening the uncertainty around the reaction function itself.

Aggregating these uncertainties (assuming partial independence), the NK-implied standard deviation of the appropriate policy rate is approximately 120-180bp, compared to ~80-100bp implied by 1Y10Y swaption straddles. This suggests MOVE fair value of ~115-130, modestly above the observed 100-120.

However, the surprise/telegraphed discriminator moderates actionability:
- Historical base rate: realized rates vol exceeded implied in 3 of 6 comparable policy uncertainty episodes (QE1, taper tantrum, COVID — all surprises).
- Current risks (deficit trajectory, QT, tariff policy) are extensively discussed in FOMC minutes, media, and market commentary.
- Probability of a genuine surprise: ~25-35% over the next 12 months (the surprise would likely come from the timing or magnitude of a policy shift, not its direction).
- Expected payoff to buying rates vol: positive but with a Sharpe of ~0.2-0.3, insufficient for a levered position but appropriate as tail hedge carry.

### Claim 7: CDX-VIX Skew Divergence as Leading Indicator
The NK IS-LM model distinguishes between the goods market (IS) and the financial market (LM). Equity vol prices the variance of current-period earnings, which are a function of the current output gap and the fiscal injection. Credit spreads price the present value of default losses over the life of the obligation, which depends on the entire path of future output gaps and funding costs.

The divergence mechanism:
- **Equity vol (VIX):** Compressed by 0DTE gamma-pinning, covered call selling ($80B+ AUM), and Kalecki-sustained earnings. VIX at 13-18 reflects the current period's low earnings variance.
- **Credit vol (CDX skew):** Incorporates the maturity wall's forward impact (2026-2028), the CLO arbitrage viability threshold (SOFR-dependent), and the private credit hidden vol reservoir. CDX 5Y IG skew (25-delta put/call) widening relative to VIX signals that the credit market's multi-year output gap path is deteriorating.

The empirical pattern: in 2007, CDX IG skew widened 3-4 months before VIX began its sustained rise. In 2018 Q4, CDX HY spreads led the equity selloff by approximately 2-3 weeks. The leading relationship arises because credit instruments have longer tenor and therefore embed more of the forward macro trajectory.

### Claim 8: Integrated NK Macro Regime Assessment

**MACRO REGIME ASSESSMENT**
- **Business cycle phase:** Late-cycle expansion with decelerating but positive momentum. GDP tracking ~2.0-2.5% annualized (Q1 2026), above trend of ~1.8%.
- **Output gap:** Estimated +0.5% to +1.0%. CBO potential output estimates suggest the economy has been running above potential since mid-2023, but the gap is narrowing as capacity catches up and fiscal impulse stabilizes.
- **Inflation dynamics:** Dual-track. Goods deflation (-1.0% to -0.5% YoY) from supply chain normalization and China export deflation. Services inflation persistent at 3.5-4.0% driven by shelter lag, healthcare services, and insurance. Core PCE: 2.5-2.8%, above the 2% target but within the "tolerance zone" where the FOMC accepts gradual convergence.

**POLICY STANCE EVALUATION**
- **Monetary policy:** Fed funds at 4.25-4.50% with core PCE at ~2.6% implies a real policy rate of ~1.7-1.9%. Against an r-star range of 0.5-2.0%, the stance is restrictive but potentially only mildly so if r-star is at the upper end. The Taylor Rule prescribes: 2.0% + 2.0% + 1.5*(2.6%-2.0%) + 0.5*(0.75%) = 5.275%, suggesting the Fed is ~75-100bp below the strict Taylor prescription — a dovish lean relative to the rule.
- **Fiscal policy:** The 6-7% deficit/GDP in a near-full-employment economy is historically unprecedented (excluding wartime and recession). The fiscal multiplier at this point in the cycle is approximately 0.3-0.5 (well below the 1.5-2.0 estimated at the ZLB during recessions, per Christiano-Eichenbaum-Rebelo 2011), but the sheer scale means fiscal impulse is still adding ~2-3% to nominal GDP growth. This partially offsets monetary restriction and extends the cycle.
- **Assessment:** The monetary-fiscal mix is internally contradictory. Monetary policy is trying to slow the economy while fiscal policy is stimulating it. This tug-of-war is the structural driver of elevated rates vol (MOVE) alongside compressed equity vol (VIX) — the Kalecki fiscal channel sustains earnings while the monetary-fiscal conflict sustains rate uncertainty.

**GROWTH AND INFLATION OUTLOOK**

| Scenario | Probability | GDP Growth | Core PCE | Fed Funds (12m) | Implication |
|---|---|---|---|---|---|
| **Base case:** Soft landing, gradual disinflation | 45% | 1.8-2.2% | 2.3-2.6% | 3.75-4.00% | MOVE declines to 85-100, VIX stable 14-18 |
| **Upside:** Fiscal acceleration + productivity boost | 15% | 2.5-3.0% | 2.0-2.3% | 3.50-3.75% | MOVE declines to 75-85, VIX declines to 12-15 |
| **Downside 1:** Services inflation re-acceleration | 25% | 1.5-2.0% | 3.0-3.5% | 4.50-5.00% | MOVE rises to 130-150, VIX rises to 20-25 |
| **Downside 2:** Credit event (maturity wall cascade) | 10% | -0.5 to +0.5% | 2.0-2.5% | 2.50-3.00% | MOVE spikes to 150+, VIX spikes to 35+ |
| **Tail:** Fiscal dominance/confidence crisis | 5% | -1.0 to 0% | 4.0-5.0% | Constrained | MOVE 200+, VIX 40+, correlation breakdown |

**MARKET IMPLICATIONS**

- **Rates:** Bear steepening bias in the base case as term premium remains elevated. The butterfly anomaly (2s5s10s) normalizes toward 0 to -5bp over 6-12 months as either basis trades reduce or term premium reprices further. Duration positioning: underweight 10Y+ relative to 2-5Y.
- **Equities:** VIX suppression is real but fragile. The vol distribution shape change means the relevant risk metric is not VIX level but 3-sigma gap risk, which is elevated. The Kalecki profit channel sustains earnings through the base case but breaks in Downside 2 and Tail scenarios.
- **Credit:** CDX-VIX skew divergence is the early warning system. Monitor CLO AAA spreads (SOFR+140-170 is benign; SOFR+200+ triggers arbitrage collapse). The conditioned credit impulse is currently in Type A (benign) territory but the maturity wall timeline (2026-2028) provides a clock.
- **FX:** G10 FX vol at 7-9% is consistent with the soft landing base case. Dollar direction depends on the relative monetary policy differential — if the Fed is forced to hold rates higher-for-longer (Downside 1) while the ECB cuts, USD strengthens and FX vol remains suppressed. In Downside 2/Tail scenarios, FX vol explodes as carry trades unwind.

## Confidence Assessment

| Claim | Confidence | Justification |
|---|---|---|
| 1. 5y5y threshold effect | 6/10 | Mechanism is theoretically grounded in NK IS curve and empirically plausible, but the exact threshold level (~4.5%) involves judgment and may shift with structural changes in housing/corporate finance. Has not been tested across enough rate cycles in the modern era. |
| 2. VRP-rate level correlation | 7/10 | Theoretically necessary from distribution truncation at ZLB and empirically supported (Cieslak-Povala 2015, Mueller-Vedolin-Zhou 2019). The quantitative magnitude (Sharpe halving) is an estimate with considerable uncertainty. |
| 3. NKPC convexity and swaption skew | 7/10 | The convexity of the Phillips Curve near capacity is well-established theoretically (Debortoli-Gali-Gambetti 2019) and consistent with current data. The mapping to swaption skew is indirect — other factors (supply dynamics, risk premia) also influence skew. |
| 4. Conditioned credit impulse | 6/10 | The sectoral balance conditioning is logically necessary and the Kalecki-Minsky taxonomy is a validated framework in the KB. However, the false positive rate reduction estimate (~65-70% to ~30-35%) is based on a small sample of cycles and the 2-3 month data lag limits real-time utility. |
| 5. Butterfly spread anomaly | 7/10 | The decomposition into policy path (5Y) vs. term premium (10Y) vs. basis trade distortion is well-supported. The prediction of violent normalization on basis trade unwind is conditional on a trigger that may not materialize in the forecast horizon. |
| 6. Rates vol underpricing (calibrated) | 5/10 | The directional claim (underpriced) is well-supported by multiple NK uncertainty channels. The calibration (MOVE fair value 115-130) involves significant model uncertainty. The moderate expected payoff (Sharpe 0.2-0.3) is consistent with my prior analysis and the KB's 50/50 base rate for comparable episodes. Self-assessment deliberately conservative. |
| 7. CDX-VIX skew divergence | 6/10 | Theoretically compelling as a forward-looking indicator based on tenor differential. Empirical sample is small (2007, 2018 are the clean examples). Needs systematic backtesting to distinguish signal from noise. |
| 8. Integrated regime assessment | 7/10 | The macro regime description is well-grounded in standard NK diagnostics. Scenario probabilities are subjective but internally consistent. The 45% base case for soft landing reflects the historically unusual monetary-fiscal mix, which introduces genuine uncertainty about the terminal outcome. |

## Connections to Other Topics

### Rates-Equity Correlation (depth_level: 6)
The maturity-dependent correlation bifurcation documented in the KB (2Y-SPX at -0.25 to -0.35; 30Y-SPX at +0.05 to +0.15) is a direct consequence of the current vol regime. In the NK framework:
- The 2Y rate is dominated by policy rate expectations, which co-move negatively with equities (bad growth news → rate cuts → 2Y falls, equities fall less).
- The 30Y rate is dominated by term premium, which co-moves positively with equities when fiscal risk is the marginal driver (fiscal expansion → higher earnings AND higher term premium).
- The NKPC convexity (Claim 3) determines which regime dominates: when ULC is above ~3.5%, the supply-side channel dominates and long-duration correlation turns positive.

### Monetary Policy (depth_level: 4)
Central bank reaction function uncertainty is the bridge. The Taylor Rule coefficient uncertainty (is the effective inflation coefficient 1.0, 1.2, or 1.5?) directly maps to rates vol. If the FOMC is operating with a coefficient below 1.0 (violating the Taylor Principle), this constitutes incipient fiscal dominance — the central bank is accommodating fiscal deficits rather than targeting inflation. The knowledge base's "partial fiscal dominance" thesis is consistent with my Taylor Rule assessment showing the Fed ~75-100bp below strict prescription.

The QT dual channel (reserve scarcity + duration extraction) interacts with vol regimes through the LM curve: as reserves decline, the overnight rate becomes more volatile, and the money multiplier becomes less predictable. This is a pure monetary transmission mechanism that elevates rates vol independent of the IS curve shocks.

### Risk Appetite Regimes (depth_level: 2)
The Kalecki-Minsky low-vol taxonomy maps directly to risk appetite regime classification:
- Type A (fiscal-supported): Risk appetite is sustained by genuine income flows. Drawdowns are bought because the fiscal backstop is operating. This supports the current VIX compression.
- Type B (credit-supported): Risk appetite is sustained by leverage. Drawdowns trigger deleveraging cascades. This is the fragile state that the maturity wall could precipitate.

The vol distribution shape change (thinner body, fatter tails) means that standard risk appetite indicators (VIX level, credit spreads) understate the fragility of the current regime. The VVIX/VIX ratio at 9-10x (vs. normal 5-7x) may be capturing sophisticated investors' assessment that the risk appetite regime is more fragile than headline vol suggests.

### Commodity Prices and Inflation
Commodity price shocks are supply-side shocks in the NK framework, and their vol implications differ fundamentally from demand shocks. An oil price spike (e.g., from Middle East escalation) would:
- Shift the NKPC upward (cost-push inflation), forcing the Fed into a growth-inflation tradeoff.
- Increase the probability of Downside 1 (services inflation re-acceleration) by adding headline inflation pressure that feeds into inflation expectations.
- Produce VIX-MOVE decorrelation (supply shock regime, as per the KB) because rates rise (inflation) while equities fall (growth hit).

This is distinct from the demand-shock channel where VIX and MOVE co-move positively.

## Open Questions

1. **Is the effective Taylor Rule inflation coefficient currently above or below 1.0?** This is the single most important parameter for vol regime assessment. Below 1.0 implies fiscal dominance and structurally elevated rates vol with no natural anchor. Above 1.0 implies the Fed retains inflation-fighting credibility and rates vol eventually normalizes. I assess ~1.0-1.2 currently (below the standard 1.5), but the uncertainty around this estimate is enormous.

2. **What is the current r-star?** The Laubach-Williams vs. Holston-Laubach-Williams vs. market-implied estimates diverge by 100-150bp. If r-star has genuinely shifted upward (to 1.5-2.0% as suggested by the productivity/AI thesis), the current policy stance is much less restrictive than it appears, and the probability of Downside 1 (inflation re-acceleration) rises materially. Conversely, if r-star is still ~0.5-1.0%, policy is quite restrictive and the soft landing base case is well-supported.

3. **Can the monetary-fiscal tug-of-war persist as a stable equilibrium?** The Sargent-Wallace (1981) "unpleasant monetarist arithmetic" suggests it cannot indefinitely — eventually one policy must dominate. But the timescale is unknown. If the fiscal trajectory forces monetary accommodation within 12-18 months, the Tail scenario probability rises from 5% toward 10-15%.

4. **How does the 0DTE microstructure interact with the NKPC convexity channel?** If a macro shock (e.g., hot CPI print) triggers a rate spike that the swaption market prices asymmetrically (Claim 3), does the 0DTE gamma flip amplify the equity response? The interaction between macro vol transmission and microstructure amplification is theoretically important but empirically uncharacterized.

5. **Is the private credit hidden vol reservoir large enough to produce systemic stress?** At $1.7T+ (roughly 6-7% of GDP), private credit is significant but not obviously systemic by itself. The question is whether it acts as a force multiplier through the financial accelerator when combined with the maturity wall and CLO arbitrage collapse channels. The NK financial accelerator (Bernanke-Gertler-Gilchrist 1999) is convex in leverage — if private credit losses impair intermediary capital, the amplification could be disproportionate to the direct losses.

6. **What is the appropriate discount for the "telegraphed" nature of current risks?** My assessment applies a ~65-75% discount to the rates vol underpricing thesis (positive directional call but low Sharpe). However, telegraphed risks can still surprise in timing and magnitude — the taper tantrum was a "telegraphed" risk that nevertheless generated significant realized vol because the market mispriced the speed of implementation. The discount factor itself is uncertain.

7. **Where exactly is the reserve scarcity threshold for the QT jump risk channel?** The September 2019 repo spike occurred at ~$1.4T in reserves. Current reserves are ~$3.3-3.5T but the banking system's minimum comfortable level may have risen due to liquidity regulations and the post-SVB environment. The threshold is unknown and unknowable ex ante — it is only revealed by breaching it, which makes it a genuinely irreducible source of uncertainty.

8. **Does the VRP-rate level relationship hold symmetrically on the way down?** If the Fed cuts aggressively (Downside 2 scenario), do we re-enter a low-VRP regime that makes vol-selling attractive again, or has the distribution permanently widened due to structural fiscal uncertainty? The answer determines whether the VRP regime is cyclical (tied to rate levels) or secular (tied to fiscal dominance).
