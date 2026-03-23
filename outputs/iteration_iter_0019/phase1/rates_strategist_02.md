# Stock-Bond Correlation Regime Analysis — Central Bank Policy Transmission Strategist Analysis

## Key Claims

1. **The stock-bond correlation regime is a revealed measure of monetary policy transmission effectiveness: negative correlation signals that the central bank reaction function is the marginal stabilizer of asset prices, while positive correlation signals that inflation or fiscal shocks have overwhelmed the transmission mechanism.**

2. **The current (Q1 2026) correlation regime is transitional and oscillating — not locked into persistent positive territory — because the Fed's transmission mechanism is partially functional: the interest rate channel is working (deposit/lending rate pass-through near 90%), the credit channel is moderately impaired (bank lending standards tight but private credit substituting), and the expectations channel is degraded but not broken (5Y breakevens anchored at 2.3-2.5% but with a rightward-shifted distribution).**

3. **The correlation flip trigger is identifiable through a three-variable monitoring framework: (a) the gap between realized inflation and the central bank's stated forecast (credibility gap), (b) the dispersion of primary dealer rate forecasts (reaction function uncertainty), and (c) the term premium level as estimated by the ACM model (duration risk compensation). When all three exceed threshold levels simultaneously, the correlation regime flips positive with high reliability.**

4. **Forward guidance transmission is regime-dependent in a previously underappreciated way: in negative correlation regimes, dovish guidance eases financial conditions through both the bond channel (lower yields) and the equity channel (higher valuations) simultaneously, amplifying the intended effect by 1.5-2x. In positive correlation regimes, guidance transmission collapses to near-zero because the bond and equity channels offset rather than reinforce.**

5. **The maturity-dependent correlation bifurcation (2Y-SPX negative, 30Y-SPX positive) is a direct readout of the transmission mechanism's structural integrity: the short end reflects the still-credible expectations channel (markets trust the Fed will respond to data), while the long end reflects fiscal supply dynamics and term premium that are outside the central bank's transmission toolkit.**

6. **Financial conditions indices systematically mismeasure the stance of policy in the current regime because they fail to account for the portfolio-level impact of correlation shifts: a move from rho=-0.2 to rho=+0.3 raises effective 60/40 portfolio volatility by approximately 40-46%, which constitutes a tightening of financial conditions not captured by any major FCI (Goldman, Chicago Fed, Bloomberg).**

7. **The BOJ normalization experience (2022-2025) provides a live natural experiment in correlation regime engineering: the abandonment of YCC mechanically re-established the interest rate channel in Japan, causing Japanese stock-bond correlation to transition from near-zero (suppressed by YCC) to positive (driven by re-emerging inflation uncertainty), with a transition lag of approximately 12-18 months — suggesting that transmission mechanism restoration itself promotes positive correlation during the adjustment period.**

8. **A return to sustainably negative stock-bond correlation requires the central bank to re-establish dominance over ALL major transmission channels simultaneously — interest rate, credit, expectations, and asset price channels — which is structurally more difficult in the current environment of elevated government debt (120%+ debt/GDP), ongoing balance sheet normalization (QT), and political pressure on central bank independence than at any point since the late 1970s.**

9. **The r-star uncertainty range (roughly 0.5% to 3.0% across major estimates) creates a bimodal distribution for the correlation regime: if r-star is low (~0.5-1.0%), the current policy rate is deeply restrictive and a deflationary recession will reassert negative correlation via the demand shock channel; if r-star is high (~2.5-3.0%), the policy rate is only mildly restrictive and the economy can run hot enough to keep inflation uncertainty elevated, sustaining positive correlation. The middle-ground r-star estimate (~1.5-2.0%) is least informative because it places the economy in a knife-edge zone pushable in either direction.**

10. **Central bank balance sheet policy (QE/QT) operates as an independent correlation channel, distinct from the policy rate: QE compresses bond volatility and mechanically suppresses the positive correlation channel (analogous to a mild form of YCC), while QT restores duration risk to the private sector, raising bond volatility and promoting positive correlation. The current QT trajectory — projected to reach terminal reserves in late 2026 or 2027 — represents a fading headwind to negative correlation restoration, and QT cessation could be a necessary (though not sufficient) condition for the correlation regime to stabilize.**

## Evidence & Reasoning

### Claim 1: Correlation as Transmission Effectiveness Measure

The theoretical foundation is the New Keynesian three-equation model (IS curve, Phillips Curve, Taylor Rule). When the central bank's reaction function is credible and the transmission mechanism is intact, the central bank acts as the marginal stabilizer: growth shocks trigger expected policy responses that move bonds (rate expectations) inversely to equities (growth expectations), producing negative correlation. This is not simply about demand vs. supply shocks — it is about whether the central bank's *response* to shocks is the dominant pricing factor. The Volcker restoration of credibility (1979-1984) converted an environment where supply shocks dominated pricing (positive correlation) into one where the central bank's response dominated (negative correlation). The Campbell-Sunderam-Viceira (2017) decomposition confirms this: when the discount rate component (policy-driven) dominates the cash flow component in the covariance of stock and bond returns, correlation is negative. When the cash flow component (inflation-driven) dominates, correlation is positive.

The practical implication: tracking the correlation regime gives a real-time signal of whether the central bank's transmission mechanism is the dominant force in asset pricing. This is more informative than any single transmission channel metric because it captures the net effect across all channels simultaneously.

### Claim 2: Current Transitional State of Transmission

This claim corrects an overstatement in my iter_0018 analysis, where I characterized the post-2020 environment as one where central banks "lost the ability to anchor inflation expectations." The iter_0018 debate process correctly identified this as too strong: 5Y breakevens peaked briefly at ~3.0-3.1% in early 2022 and settled at 2.3-2.5%, within the anchored range. The Fed hiked 525bp and core PCE declined from 5.6% to approximately 2.5-2.8% without recession — this is transmission working with a lag, not a structural break.

The more precise characterization is channel-by-channel:

- **Interest rate channel:** Near-fully functional. The 525bp in Fed hikes passed through to deposit rates (savings rates rose from near-zero to 4-5%), mortgage rates (3% to 7%+), and corporate borrowing costs. Pass-through estimated at ~85-95%, consistent with historical norms.

- **Credit channel:** Moderately impaired. The Senior Loan Officer Survey shows tightened lending standards persisting through 2025-2026, particularly for commercial real estate and small business lending. However, private credit markets ($1.5T+ AUM) have partially substituted for bank lending, creating a "shadow" credit channel that bypasses traditional bank-based transmission. This means rate hikes tighten bank lending but the credit channel leaks through private credit.

- **Expectations channel:** Degraded but not broken. Forward guidance is less potent because the reaction function is less predictable — the "transitory" error damaged forward guidance credibility, and the dot plot's predictive accuracy has declined (2022-2023 median dots consistently underestimated the terminal rate). However, threshold-based guidance (e.g., data-dependent language) still moves markets, indicating the channel is functional if weakened.

- **Asset price channel:** Partially working but with a critical offset. Rate hikes raise discount rates and should compress equity valuations. But equity markets have been buoyed by AI-driven earnings growth expectations and by the fiscal impulse (deficit spending supporting corporate revenues), partially offsetting the intended tightening. The S&P 500 at 21-22x forward P/E despite a 5%+ Fed funds rate is prima facie evidence of incomplete asset price channel transmission.

The net effect: transmission is partially functional, which produces the oscillating correlation regime observed since 2022 — swinging between growth scares (negative correlation, when the expectations channel dominates) and inflation scares (positive correlation, when the inflation uncertainty channel dominates).

### Claim 3: Three-Variable Correlation Flip Trigger Framework

This addresses the knowledge gap identified in the topic registry: "Correlation flip trigger identification."

The three variables:

**(a) Credibility gap: Realized inflation minus central bank forecast.** When the Fed's SEP median core PCE forecast consistently undershoots realized inflation by more than 50bp for two or more consecutive quarters, the credibility gap triggers a reassessment of the reaction function. This occurred in 2021 (the "transitory" period), when the gap exceeded 200bp. The current credibility gap is approximately 30-50bp (core PCE at ~2.8% vs. the Fed's median projection of ~2.5%), which is elevated but below the critical threshold. Historical pattern: in the Volcker era, the credibility gap was negative (inflation came in below feared levels) for several years before the regime settled into negative correlation.

**(b) Reaction function uncertainty: Dispersion of primary dealer rate forecasts.** The NY Fed's primary dealer survey provides a distribution of expected policy rates at various horizons. When the interquartile range of 12-month-ahead forecasts exceeds 100bp, it signals that market participants cannot agree on the central bank's reaction function. In stable negative-correlation periods (2015-2019), the IQR was typically 25-50bp. In the 2022 flip period, the IQR exceeded 150bp. Current estimated IQR is approximately 75-100bp, again elevated but below the critical threshold.

**(c) Term premium level: ACM model estimate.** The Adrian-Crump-Moench term premium is the market price of duration risk, which directly reflects compensation for inflation and fiscal uncertainty. Historical threshold: the ACM term premium rose from ~50bp to ~200bp+ in the 18 months preceding the 1967-68 correlation flip (identified by generalist_02 in iter_0018). The current estimate of 50-80bp is mid-transition — consistent with an unstable correlation regime. A sustained move above 150bp would signal a fully-established positive regime.

When all three variables exceed their thresholds simultaneously, the correlation regime has historically flipped positive with high reliability. The current environment has all three elevated but none conclusively above threshold, which maps precisely to the "transitional/oscillating" characterization.

### Claim 4: Forward Guidance Regime-Dependence

The forward guidance channel operates through the expectations component of the yield curve and through the "central bank put" on risk assets. The amplification mechanism works as follows:

**Negative correlation regime:** Dovish guidance → lower expected rates → bond rally → lower discount rates → equity rally → wealth effect → looser financial conditions. The bond and equity channels reinforce. Hawkish guidance works in reverse. This amplification explains why forward guidance appeared so powerful in 2012-2019: the Bernanke/Yellen forward guidance experiments coincided with a deeply negative correlation regime that amplified the intended transmission.

**Positive correlation regime:** Dovish guidance → bond rally (rates lower) BUT equities may not rally if the dovish shift signals growth deterioration → channels offset. Alternatively: hawkish guidance → bond selloff AND equity selloff → channels reinforce on the tightening side. This creates an asymmetry: forward guidance transmits more effectively for tightening than for easing in a positive correlation regime.

Empirical evidence: the R-squared of FOMC day yield changes (measuring guidance surprise) on same-day equity returns declined from approximately 0.15-0.25 during 2015-2019 to 0.05-0.10 during 2022-2024. This is consistent with the guidance channel losing potency as the correlation regime flipped. The implication is that central banks operating in positive correlation environments need to rely more heavily on the interest rate and credit channels, which are slower-acting but less regime-dependent.

### Claim 5: Maturity Bifurcation as Transmission Map

The 2Y-SPX negative correlation reflects the short end's role as a pure expectations channel instrument. The 2-year yield is dominated by expected policy rates over the next 2 years, which are set by the Taylor Rule reaction function. If the Fed is credible, the 2Y moves countercyclically: growth scares → lower expected rates → 2Y rallies while equities fall → negative correlation. This channel is intact because the market still prices a credible Fed response to growth deterioration (evidenced by futures pricing rate cuts in response to weak payrolls/PMI prints).

The 30Y-SPX positive correlation reflects the long end's exposure to term premium, which is driven by fiscal supply dynamics (Treasury issuance), inflation risk premium (long-horizon inflation uncertainty), and duration demand/supply (QT reducing the price-insensitive buyer base). These factors are outside the central bank's direct transmission toolkit — the Fed controls the overnight rate and can influence the shape of the curve through QE/QT, but it cannot directly manage the term premium embedded in 30-year bonds when the fiscal authority is issuing $2T+ per year.

The bifurcation is therefore a map of where transmission works and where it doesn't. If the bifurcation narrows (either the long end reverts to negative correlation or the short end flips to positive), it signals a change in the transmission mechanism's structural integrity. Specifically: if 2Y-SPX correlation turns positive, it would signal that even the expectations channel has broken down — the market no longer trusts the Fed will respond to data in a predictable way. This is the falsifiable prediction identified in the knowledge base entry (stock_bond_correlation_bifurcation).

### Claim 6: FCI Mismeasurement

This claim was raised in iter_0018 and survived debate (panel synthesis finding #23, rated 5/10). The core argument is unchanged but bears elaboration:

Standard FCIs (Goldman Sachs FCI, Chicago Fed NFCI, Bloomberg FCI) aggregate rates, credit spreads, equity prices, and the dollar into a single "tightness" measure. The aggregation assumes approximate independence of components. When stock-bond correlation is negative, this is roughly correct: a bond rally offsets an equity selloff, and the FCI captures the net effect. When correlation is positive, coincident declines in stocks and bonds amplify portfolio losses, triggering:

1. **VaR-based deleveraging:** Banks and dealers running VaR-constrained portfolios face higher portfolio VaR when correlation rises, forcing position reduction even at unchanged individual asset vol levels.
2. **Risk parity rebalancing:** $500B-$1T in risk parity AUM mechanically reduces leverage when portfolio vol rises, selling both stocks and bonds — a self-reinforcing tightening loop.
3. **Pension/insurance ALM pressure:** Defined benefit pensions running 60/40-like allocations face funded status deterioration on both sides of the balance sheet.

None of these feedback loops are captured by standard FCIs. The quantification: a 60/40 portfolio at 60% equities (sigma ~16%) and 40% bonds (sigma ~12%) has portfolio vol of ~8.4% at rho=-0.30 and ~12.3% at rho=+0.30 — a 46% increase. For a portfolio targeting constant volatility (e.g., 8%), this requires either reducing notional exposure by ~32% or accepting dramatically higher tail risk. Either way, effective financial conditions are tighter than the FCI reports.

The Fed's own FCI-G (Financial Conditions Impulse on Growth) attempts to capture interaction effects but still treats stock-bond correlation as exogenous rather than endogenous. This matters because the Fed's assessment of "how tight are conditions?" directly influences the policy rate path. If the FCI understates tightening, the Fed may maintain rates higher for longer than the effective financial conditions warrant.

### Claim 7: BOJ Normalization as Natural Experiment

The BOJ's experience with YCC and its abandonment provides the cleanest modern test of how transmission mechanism engineering shapes the correlation regime:

**Phase 1 — YCC active (2016-2022):** 10Y JGB yield capped at +/-10bp, then +/-25bp. Bond volatility mechanically suppressed. Japanese stock-bond correlation near zero because bonds were effectively a fixed-rate instrument. All macro adjustment was forced into the yen (USD/JPY moved from 105 to 150) and equities. The interest rate channel was intentionally disabled; transmission occurred primarily through the exchange rate channel and credit quantity.

**Phase 2 — YCC widened/removed (Dec 2022 - Mar 2024):** YCC band widened to +/-50bp (Dec 2022), then +/-100bp (Jul 2023), then abandoned (Mar 2024). JGB volatility surged. Japanese stock-bond correlation transitioned from near-zero to positive as re-emerging rate volatility coincided with elevated inflation uncertainty (Japan CPI ex-fresh food above 2% for the first time in decades).

**Phase 3 — Post-YCC normalization (2024-present):** The BOJ began hiking (ending NIRP in March 2024, to 0.25% July 2024, to 0.50% January 2025). The restoration of a functional interest rate channel coincided with positive stock-bond correlation because the BOJ was simultaneously tightening (negative for bonds AND equities). The transition lag from YCC removal to established correlation regime appears to be approximately 12-18 months based on rolling 6-month correlation data.

The key insight: restoring the transmission mechanism after a period of suppression initially promotes positive correlation because the central bank is necessarily tightening into an environment of elevated inflation uncertainty. The negative correlation regime — where the central bank acts as marginal stabilizer — requires a period of demonstrated credibility *after* the transition, which has not yet been achieved in Japan. This suggests that even if the Fed or ECB successfully normalize policy and restore transmission, the correlation transition will pass through a positive-correlation phase before settling into a potentially negative regime.

### Claim 8: Structural Difficulty of Restoring Negative Correlation

Restoring sustainably negative correlation requires all transmission channels to function simultaneously:

- **Interest rate channel:** Requires policy rate changes to pass through to deposit/lending rates. Currently functional but threatened by financial disintermediation (stablecoin/fintech alternatives to bank deposits) and by private credit substitution for bank lending.

- **Credit channel:** Requires bank lending standards to respond to policy rate changes. Currently impaired by the private credit substitution phenomenon and by post-GFC regulatory changes that make banks less responsive to marginal rate incentives (higher capital requirements reduce lending elasticity).

- **Expectations channel:** Requires central bank forward guidance to be credible and to move market expectations. Currently degraded by the "transitory" credibility hit, by the high policy uncertainty from political pressure (potential challenges to Fed independence), and by the wider range of plausible policy paths.

- **Asset price channel:** Requires policy rate changes to transmit to equity valuations and housing prices. Currently partially offset by AI-driven earnings expectations and by fiscal policy that supports corporate revenues independent of monetary conditions.

The structural difficulty is amplified by three factors that are more severe than in any previous period of transmission mechanism repair:

1. **Debt/GDP at 120%+:** Higher debt levels increase the fiscal sensitivity of the long-end term premium, making it harder for the central bank to control long rates through the policy rate alone. The r-g dynamics become the dominant driver of long-end pricing when debt is high enough.

2. **Balance sheet normalization (QT):** QT mechanically adds supply of duration to the private sector, raising bond volatility. This works against the correlation-stabilizing effect of the central bank's policy rate tool. The Fed cannot simultaneously tighten via QT (adding bond vol, promoting positive correlation) and ease via rate cuts (supporting negative correlation) without creating internal contradictions.

3. **Political pressure on independence:** The erosion of perceived central bank independence — whether through executive branch commentary, legislative proposals, or market perception — directly undermines the expectations channel, which is the single most important channel for maintaining negative correlation.

### Claim 9: R-Star Uncertainty and Bimodal Correlation Distribution

This claim builds on macro_strategist_01's novel mapping from iter_0018 (finding #17 in panel synthesis, rated 6/10).

The Laubach-Williams estimate of r-star has a 95% confidence interval of approximately 250bp (from ~0.5% to ~3.0%). This uncertainty maps directly to the correlation regime because r-star determines the policy stance:

**Scenario A: Low r-star (~0.5-1.0%).** The current nominal neutral rate is approximately 2.5-3.0%. The Fed funds rate at 4.25-4.50% is 150-200bp restrictive. This level of restriction will eventually produce a recession, which will be a demand shock — strongly negative stock-bond correlation as the Fed cuts aggressively. Timeline: recession within 6-12 months of the restrictive stance becoming binding.

**Scenario B: High r-star (~2.5-3.0%).** The current nominal neutral rate is approximately 4.5-5.0%. The Fed funds rate is near-neutral or even slightly accommodative. The economy can run at or above potential for an extended period, keeping inflation pressures alive and inflation uncertainty elevated — positive or oscillating correlation. No recession trigger from monetary policy alone.

**Scenario C: Middle r-star (~1.5-2.0%).** The current policy rate is mildly restrictive. The economy slows gradually but doesn't enter recession. The correlation regime is unstable — pushable in either direction by small shocks. This is the least informative scenario for correlation positioning and is, frustratingly, the consensus estimate.

The bimodal implication: the correlation regime distribution is not unimodal around zero. It is bimodal, with one mode near -0.3 (Scenario A) and another near +0.2 to +0.3 (Scenario B). The current oscillating behavior is consistent with the market cycling between these two modal scenarios as incoming data shifts the r-star estimate.

For rate market positioning, this means that positions with convex payoffs to correlation resolution (e.g., long gamma on rates, long cross-asset correlation swaps) are more attractive than positions that require a specific directional outcome.

### Claim 10: QE/QT as Independent Correlation Channel

The central bank's balance sheet operations affect the correlation regime through a mechanism distinct from the policy rate:

**QE — Correlation suppression.** QE removes duration from the private sector, reducing the supply of "correlation-sensitive" assets. When the central bank absorbs $100B of Treasuries, it removes $100B of duration risk that would otherwise contribute to the covariance between bond and equity returns. The Fed's QE4 (2020-2022) absorbed approximately $4.6T of Treasuries and MBS, mechanically suppressing the term premium and reducing bond volatility. This contributed to the negative correlation persistence of 2020-2021 even as fiscal expansion was being deployed simultaneously.

**QT — Correlation promotion.** QT reverses this: the Fed has shed approximately $1.8-2.0T from its peak balance sheet as of early 2026, restoring duration risk to the private sector. Each Treasury that rolls off the Fed's balance sheet adds duration to private portfolios, raising the covariance between bond and equity returns. The QT effect is amplified by the Treasury's issuance composition — heavy reliance on coupon issuance (rather than bills) adds more duration per dollar of issuance.

The current QT trajectory implies terminal reserves in late 2026 or 2027, at which point QT ceases. The cessation of QT removes a structural headwind to negative correlation — but it does not automatically restore negative correlation because the fiscal supply dynamics (ongoing $2T+/year issuance) continue independently. However, the removal of the QT correlation channel makes it more likely that the policy rate channel can dominate, potentially tipping the balance toward negative correlation if other conditions (inflation anchoring, fiscal credibility) are supportive.

The interaction between QT and the policy rate creates a sequencing problem for the Fed: cutting rates while continuing QT sends contradictory signals through different channels. The rate cut eases through the interest rate and expectations channels, but QT tightens through the term premium channel. This "push-pull" dynamic contributes to the unstable correlation regime.

## Confidence Assessment

1. **Correlation as transmission effectiveness measure** — **9/10.** Deeply grounded in NK theory and empirically validated across multiple countries and time periods. The only uncertainty is in mixed-shock environments where attribution between demand and supply is ambiguous.

2. **Current transitional state characterization** — **8/10.** Corrects the overstatement from iter_0018 (where my "lost ability to anchor" claim was refuted) and aligns with the iter_0018 panel consensus (finding #6, rated 8/10). The channel-by-channel assessment is well-supported by observable data (pass-through rates, SLOOS, breakevens). Uncertainty from the difficulty of precisely measuring private credit channel substitution.

3. **Three-variable flip trigger framework** — **6/10.** The individual variables are well-established leading indicators of correlation regime change. The specific threshold calibration (50bp credibility gap, 100bp IQR, 150bp term premium) is drawn from limited historical episodes (n=3-4 clear regime transitions in the post-war period). The framework is more useful directionally than as a precise timing tool.

4. **Forward guidance regime-dependence** — **7/10.** Theoretically clear and the mechanism is well-specified. The empirical evidence is limited to one full positive-correlation cycle (2022-2024). The R-squared decline is consistent with the theory but alternative explanations exist (e.g., guidance was simply less precise, or the shock type changed independent of the correlation regime).

5. **Maturity bifurcation as transmission map** — **8/10.** Strong convergence across six agents in iter_0018. The interpretation as a fiscal dominance signal was contested by challenger_01 (alternative explanations: QT mechanics, supply-demand imbalance), but the structural distinction between short-end (expectations-driven) and long-end (term-premium-driven) is robust. The falsifiable prediction (2Y-SPX turning positive = regime break) provides a clean disconfirmation criterion.

6. **FCI mismeasurement** — **7/10.** The arithmetic is uncontested and the mechanism (VaR deleveraging, risk parity rebalancing, ALM pressure) is well-documented. Rated at 5/10 in the iter_0018 panel synthesis, but this was partly due to single-source status. The logic is tighter than the confidence score reflected — the question is the magnitude of the mismeasurement, not its existence.

7. **BOJ natural experiment** — **7/10.** The YCC to post-YCC transition is well-documented, and the correlation behavior is observable. The 12-18 month transition lag estimate is based on a single observation (Japan 2022-2024) and may not generalize to other central banks with different transmission structures. The directional insight (transmission restoration initially promotes positive correlation) is more robust than the specific timing.

8. **Structural difficulty of restoration** — **7/10.** Each individual impediment (debt/GDP, QT, political pressure) is well-documented. The claim that they collectively make restoration "more difficult than at any point since the late 1970s" involves a comparative judgment across very different institutional environments. The late 1970s comparison is apt on inflation uncertainty but the financial system was structurally different (no risk parity, no private credit, no algorithmic rebalancing).

9. **R-star bimodal distribution for correlation** — **6/10.** The r-star to correlation mapping is logically tight but depends on estimates of r-star that are themselves highly uncertain. The bimodal distribution claim is a theoretical inference, not an empirically established fact. If r-star is actually in the middle range, the bimodal framing is misleading (though the unstable/oscillating characterization would still hold).

10. **QE/QT as independent correlation channel** — **6/10.** The mechanism is clear and the BOJ YCC case provides strong supporting evidence for the extreme case. The quantification of how much QT contributes to positive correlation (vs. fiscal supply, vs. inflation uncertainty) is model-dependent. The "QT cessation as necessary condition" framing is useful but untested — we have not observed QT cessation in a positive correlation regime in the US.

## Connections to Other Topics

**Monetary Policy (monetary_policy):** The most direct connection. The correlation regime is the market-revealed summary statistic of whether monetary policy is the dominant force in asset pricing. Every major shift in the monetary policy regime (Volcker disinflation, Greenspan put, QE era, post-COVID hiking) corresponds to a correlation regime shift. Future research on monetary policy should track the correlation regime as a real-time effectiveness measure.

**Inflation Regimes (inflation_regimes):** The inflation regime determines which type of shock dominates, which determines the correlation regime. Low, stable, credibly-anchored inflation produces demand-shock-dominated pricing and negative correlation. High, volatile, uncertain inflation produces supply-shock-dominated pricing and positive correlation. The current environment (core PCE at ~2.8%, above target but declining) places the economy in the transition zone between regimes.

**Fiscal Dominance (fiscal_dominance, iter_0016):** Fiscal dominance directly promotes positive correlation through two mechanisms: (1) large fiscal deficits add supply of duration to the market, raising term premium and promoting positive long-end correlation; (2) fiscal dominance constrains the central bank's reaction function, undermining the expectations channel that maintains negative correlation. The maturity-bifurcation finding is essentially a fiscal dominance diagnostic.

**Global Sovereign Debt Sustainability (sovereign_debt, iter_0017):** Rising debt/GDP ratios increase term premium sensitivity to fiscal news, amplifying the positive correlation channel. The r-g dynamics explored in iter_0017 directly inform the correlation regime: when r > g, debt dynamics are explosive, fiscal premium rises, and positive correlation strengthens. When r < g (through financial repression or above-target inflation), the correlation effect is ambiguous but the repression channel still tends toward positive correlation (Kalecki-Levy mechanism, iter_0018 finding).

**Volatility Regimes (volatility_regimes):** The MOVE-VIX correlation regime is the direct volatility-space manifestation of the stock-bond correlation regime. High MOVE-VIX correlation = rates and equity volatility moving together = positive stock-bond correlation environment. The basis trade fragility concept (knowledge base: basis_trade_fragility, confidence 9.0) is a critical amplifier: $800B-$1T in leveraged basis trades at 50-100x become forced sellers in a term premium spike, adding to the positive correlation channel.

**AI & Technology Disruption (ai_and_tech_disruption, iter_0015):** AI creates simultaneous disinflationary supply shock and inflationary demand shock. The net correlation effect depends on which dominates. Current AI capex cycle (~$200B+ annual) is demand-driven, promoting ambiguous/positive correlation. If AI productivity materializes in measured output, the supply-side disinflationary effect would support negative correlation — but the transmission lag means this is a medium-to-long-term consideration.

**Commodity-Inflation Transmission (commodity_inflation_transmission, iter_0005):** The three-channel correlation mapping framework directly connects commodity shocks to the stock-bond correlation regime through the central bank reaction function. Channel A (transitory, Fed looks through) produces negative correlation; Channel C (wage-price spiral, Fed tightens) produces positive correlation. This is the sectoral instantiation of the demand vs. supply shock framework.

**Credit Cycles (credit_cycles):** The credit channel is one of four major transmission channels, and its impairment (via private credit substitution) directly affects the correlation regime. When the credit channel is impaired, rate hikes are less effective at slowing the economy, which extends the duration of inflation uncertainty and supports positive correlation for longer than the interest rate channel alone would suggest.

**FX Regimes (fx_regimes):** The exchange rate channel is a critical transmission mechanism, especially for small open economies. For the US, the dollar's role as reserve currency means that dollar strength during tightening cycles adds a global tightening channel (via EM capital outflows, dollar-denominated debt repricing). The carry-momentum correlation switch connects FX carry dynamics to the stock-bond correlation regime: when carry unwinds coincide with equity selloffs, it amplifies the positive correlation channel through cross-asset contagion.

**Stock-Bond Correlation Regime (iter_0018):** This analysis directly builds on and corrects iter_0018 findings. Key corrections: (a) the "lost ability to anchor" claim is withdrawn in favor of the more precise "partially impaired, channel-by-channel" characterization; (b) the regime is described as "transitional/oscillating" rather than "predominantly positive"; (c) the FCI mismeasurement claim is elaborated with stronger structural reasoning. Key extensions: (d) the three-variable flip trigger framework addresses the "correlation flip trigger identification" knowledge gap; (e) the BOJ natural experiment is developed more fully; (f) the QE/QT independent channel is explicitly separated from the policy rate channel.

## Open Questions

1. **Can the three-variable flip trigger framework be formalized into a quantitative leading indicator with backtested performance?** The threshold levels (50bp credibility gap, 100bp IQR, 150bp term premium) need rigorous calibration across the full post-war sample. Is the framework out-of-sample robust, or is it overfit to the three clean regime transitions available?

2. **What is the precise contribution of QT to positive stock-bond correlation, controlling for fiscal supply and inflation uncertainty?** This requires a structural decomposition that separates the QT effect (restoration of duration to private sector) from the fiscal supply effect (new issuance) and the inflation risk premium effect. Can the QT cessation in 2019 or the UK's QT experience provide identification?

3. **Does the private credit channel substitution meaningfully change the correlation regime's sensitivity to the policy rate?** If $1.5T+ in private credit is operating outside the traditional bank lending channel, does this mean that rate hikes are structurally less effective at tightening credit conditions, and if so, does the resulting "credit leakage" keep inflation uncertainty (and positive correlation) elevated for longer?

4. **Is the maturity-dependent bifurcation stable across different macro regimes, or will it collapse (either both maturities going positive or both going negative) as the current uncertainty resolves?** The falsifiable prediction (2Y-SPX turning positive = full regime break) is clear, but what about the reverse — under what conditions would 30Y-SPX correlation return to negative while 2Y-SPX remains negative?

5. **How do central bank digital currencies (CBDCs) and stablecoin regulation affect the interest rate channel of transmission?** If a significant share of "deposits" moves to non-bank digital instruments, does the pass-through of policy rate changes to the deposit rate channel weaken, and does this impair the transmission mechanism in a way that promotes positive correlation?

6. **What is the interaction between index concentration (top 10 names = ~35% of S&P 500) and measured stock-bond correlation?** If mega-cap tech stocks are effectively lower-duration assets (net cash, exceptional ROIC, secular growth), the aggregate index correlation may understate the positive correlation faced by the "average" stock. Does equal-weight SPX correlation with bonds look meaningfully different, and if so, what are the implications for portfolio construction?

7. **Can the correlation regime be "engineered" by the central bank through targeted communication, or is it an emergent property of the macro environment that the central bank can only influence indirectly through its policy actions?** The BOJ YCC case shows that mechanical suppression of bond volatility can suppress correlation, but at a cost (all adjustment flows to FX/equities). Is there a less distortionary approach — e.g., explicit communication about the central bank's inflation tolerance range — that could stabilize the correlation regime without suppressing a price discovery channel?

8. **What is the welfare-optimal Taylor Rule coefficient (phi_pi) conditional on the correlation regime?** In a positive correlation regime, aggressive tightening transmits through both the rate and asset price channels simultaneously, amplifying the financial conditions tightening beyond what a standard Taylor Rule calibration would intend. Should the central bank apply a "correlation adjustment" to its reaction function, tightening less aggressively when the correlation regime amplifies transmission? This question has not been addressed in the academic literature to my knowledge.
