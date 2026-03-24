# Growth Models — Central Bank Policy Transmission Strategist Analysis

## Key Claims

1. **The monetary policy transmission mechanism is structurally impaired across at least three of five channels, making the Fed's effective policy stance significantly easier than the policy rate implies.** Private credit rate insensitivity ($200-300B/yr deployed from committed capital regardless of Fed funds), fiscal dominance (6-7% GDP deficit overwhelming the interest rate channel), and asset price channel leakage (equity rallies loosening financial conditions even as the Fed holds restrictive) combine to create a wedge between the policy rate and actual financial conditions. The Goldman Sachs FCI has frequently loosened during periods the Fed intended restrictive stance.

2. **The Fed's reaction function has shifted from a symmetric dual mandate to an asymmetric loss function with greater sensitivity to labor market deterioration than inflation overshoot, but markets have not fully priced this asymmetry.** The Sahm Rule false positive in July 2024 and the subsequent policy response revealed the Fed's true loss function — they cut despite inflation above target because labor market deterioration triggers a faster response than inflation persistence. Front-end rates pricing symmetric risk around the policy path are mispriced.

3. **Financial conditions, not the policy rate, are the operationally relevant measure of monetary policy stance — and these two have diverged by the equivalent of 100-200bp in this cycle.** The cross-asset growth rate divergence (equities pricing 5-6% NGDP, rates pricing 3-4%) is itself evidence that the transmission mechanism is not operating as intended. If policy were transmitting cleanly, asset classes would converge toward a common growth expectation.

4. **The term premium steepener is a direct consequence of impaired fiscal-monetary coordination, not a growth signal, and central banks cannot steepen or flatten the curve through conventional tools when fiscal supply dominates duration pricing.** The ACM/Kim-Wright decomposition showing term premium driving the 2s10s slope means the yield curve's signal content for growth has degraded. Central bank forward guidance about the short rate has limited ability to control the long end when Treasury supply at 6-7% GDP deficit drives term premium.

5. **The maturity wall creates an endogenous tightening mechanism that operates independently of Fed policy — a shadow monetary policy transmission channel that the Fed cannot directly control or offset.** The $900B-$1.1T in maturities with 300-500bp coupon step-ups functions as an automatic tightening of credit conditions for leveraged borrowers regardless of the Fed's rate decisions. Even if the Fed cuts 150bp, borrowers refinancing from 2020-2021 vintage fixed-rate debt face materially higher costs.

6. **Private credit's rate insensitivity is not merely a credit market observation but represents a fundamental structural break in the IS curve that permanently reduces the interest rate elasticity of aggregate demand, requiring the Fed to move rates further to achieve the same macro effect.** The $200-300B/yr deployed from committed capital pools with 5-7 year fund lifecycles means a rising share of credit creation is disconnected from the policy rate. This flattens the IS curve, meaning the same policy rate change produces a smaller output response.

7. **The NKPC convexity near potential creates a policy trap: the Fed cannot achieve the last mile of disinflation without either engineering a recession (output sacrifice ratio of 4-5 for the last mile) or receiving an exogenous favorable supply shock — and the fiscal deficit prevents the output gap from opening sufficiently to deliver disinflation through the conventional channel.** The fiscal-monetary conflict is structural: fiscal keeps the economy near potential while the Fed needs slack to finish disinflation. This is the textbook definition of fiscal dominance.

8. **Forward guidance credibility has deteriorated to the point where the expectations channel — historically the most powerful transmission mechanism — is operating at reduced capacity, as evidenced by the persistent divergence between dot plots and market pricing.** When 5Y5Y inflation expectations sit at 2.3% and Michigan 5-10Y at 2.5% rather than the 2.0% target, the expectations channel is failing to anchor the nominal economy where the central bank intends.

## Evidence & Reasoning

**Claim 1 (Transmission impairment):** Three specific channels are demonstrably impaired:
- *Interest rate channel:* Private credit deploys ~$200-300B/yr from committed capital regardless of Fed funds (KB: `private_credit_rate_insensitivity`). A 150bp hike does not stop a fund with $5B dry powder and a 3-year deployment window.
- *Credit channel:* Covenant-lite structures (>90% of leveraged loans) delay default recognition 12-24 months, meaning the credit channel's feedback loop from tightening → defaults → further tightening is structurally lagged (KB: `covenant_lite_default_delay`).
- *Asset price channel:* Equities price 5-6% NGDP while rates price 3-4% (KB: `cross_asset_growth_rate_divergence`). The wealth effect from sustained equity valuations (S&P ~21x fwd P/E) loosens financial conditions even as front-end rates remain restrictive.
- The fiscal channel (6-7% GDP deficit) directly offsets the intended contractionary effect of monetary policy through the Kalecki identity, making the effective stance far easier than the rate level implies.

**Claim 2 (Asymmetric reaction function):** The Sahm Rule triggered in July 2024 without recession (KB: `leading_indicator_degradation`), yet the Fed's response was to cut — revealing that the reaction function is asymmetric. The Fed treats labor market deterioration as more urgent than inflation persistence at current levels (2.5-3% vs 2% target). This is inconsistent with symmetric Taylor Rule pricing in the front end.

**Claim 3 (FCI-policy rate divergence):** The KB documents equity-implied NGDP of 5-6% vs rates-implied 3-4% (KB: `cross_asset_growth_rate_divergence`). If the transmission mechanism were working, restrictive policy would compress equity valuations and align cross-asset growth expectations. The divergence IS the evidence of impaired transmission.

**Claim 4 (Term premium vs growth signal):** ACM and Kim-Wright decompositions confirm term premium accounts for majority of 2s10s slope (KB: `term_premium_steepener`). This is fiscal-supply-driven ("bad steepening") rather than growth-expectations-driven ("good steepening"). The curve shape is unreliable as a cycle indicator because the Fed cannot control the fiscal supply component.

**Claim 5 (Maturity wall as shadow tightening):** $900B-$1.1T maturing 2025-2027 with 300-500bp coupon step-ups (KB: `maturity_wall`). At true leverage of 7.5-8.5x (after EBITDA addback correction), interest expense consumes 70-80% of cash EBITDA. This tightening operates automatically and cannot be offset by 100-150bp of Fed cuts because the step-up from 2020-2021 vintage rates is 300-500bp.

**Claim 6 (IS curve flattening):** Private credit at $200-300B/yr from committed capital (KB: `private_credit_rate_insensitivity`) against total private credit market of ~$1.7T and growing. As this share of total credit creation increases, the weighted-average interest rate elasticity of credit declines. The Fed must move rates more aggressively to achieve the same demand impact — effectively, the neutral rate concept itself is destabilized.

**Claim 7 (Fiscal-monetary policy trap):** The NKPC convexity (KB: `nkpc_convexity_last_mile`) implies a sacrifice ratio of 4-5 for the last mile. But the fiscal deficit at 6-7% GDP (KB: `fiscal_deficit_kalecki_channel`) mechanically prevents the output gap from opening. Private GDP growth without fiscal is only 1.0-1.5% (KB: `mid_to_late_cycle_expansion`), meaning the fiscal floor prevents the recession needed for conventional disinflation. This is the Sargent-Wallace fiscal dominance problem in practice.

**Claim 8 (Expectations channel degradation):** 5Y5Y at 2.3%, Michigan 5-10Y at 2.5% (KB: `nkpc_convexity_last_mile`). The persistent overshoot of inflation expectations relative to the 2% target indicates the expectations channel is not fully functional. Forward guidance that inflation will return to 2% is not being internalized by price-setters and wage-bargainers.

## Confidence Assessment

| Claim | Confidence | Justification |
|-------|-----------|---------------|
| 1. Transmission impairment | **8/10** | Three distinct impairments documented in KB with quantitative evidence. The direction is clear even if the magnitude of the effective stance wedge is imprecisely estimated. |
| 2. Asymmetric reaction function | **7/10** | Revealed preference from the 2024 cut cycle is strong evidence, but the reaction function shifts with FOMC composition and data. The asymmetry could reverse under a stagflationary scenario. |
| 3. FCI-policy rate divergence | **8/10** | Cross-asset divergence is directly observable. The interpretation that this reflects impaired transmission rather than rational disagreement about growth is analytically sound but not the only explanation. |
| 4. Term premium steepener | **7/10** | ACM/Kim-Wright decompositions are model-dependent (acknowledged in KB as open question). Direction is robust but magnitudes vary across models by 30-50bp. |
| 5. Maturity wall shadow tightening | **8/10** | Maturities are contractual facts. The arithmetic of coupon step-ups is deterministic. Uncertainty is in how much can be defused by amend-and-extend or private credit refinancing. |
| 6. IS curve flattening | **6/10** | Directionally correct but the magnitude depends on private credit's share of total credit creation, which is growing but still a minority. The macro significance is emerging rather than established. |
| 7. Fiscal-monetary trap | **7/10** | The individual components are well-evidenced but the synthesis into a "trap" implies the situation is inescapable, which may overstate the case. A favorable supply shock (immigration, AI) could provide an exit. |
| 8. Expectations channel degradation | **7/10** | Survey-based expectations measures are noisy and may overstate true de-anchoring. Market-based measures (TIPS breakevens) are closer to 2% but contaminated by liquidity premia. |

## Connections to Other Topics

- **Inflation dynamics:** The NKPC convexity claim (Claim 7) is the direct bridge between growth models and inflation. The fiscal-monetary policy trap implies inflation persistence is not a monetary phenomenon alone but a fiscal one — directly connecting to any analysis of the commodity price → inflation transmission mechanism explored in iter_0042.

- **Credit/default cycle:** The maturity wall as shadow tightening (Claim 5) and transmission impairment through covenant-lite structures (Claim 1) connect to credit cycle analysis. The key insight is that the credit cycle is running on a different clock than the monetary policy cycle — defaults are lagged by covenant-lite structures while the maturity wall creates deterministic tightening independent of Fed action.

- **FX/capital flows:** The fiscal-monetary policy divergence creates a strong dollar bias through the Mundell-Fleming channel (high rates + fiscal expansion → capital inflows → currency appreciation). This connects to global monetary policy divergence — the Fed cannot ease as aggressively as other central banks want because fiscal is providing the stimulus, creating persistent interest rate differentials.

- **Central bank balance sheet normalization (iter_0060/0061):** QT (balance sheet reduction) is an additional tightening channel operating alongside rate policy. If the transmission mechanism from rate hikes is impaired, the incremental tightening from QT becomes relatively more important — and potentially more disruptive if it operates through channels (reserve drainage, repo market stress) that are harder to control.

- **Equity valuation:** The asset price channel leakage (Claim 1) means equity valuations are not being disciplined by monetary policy as models assume. This has implications for any equity strategy that depends on a "Fed put" or policy-driven mean reversion in multiples.

## Open Questions

1. **Quantifying the effective stance wedge:** How many basis points of effective easing does the combination of private credit rate insensitivity, fiscal offset, and equity wealth effect create? If the policy rate is 5.0% but effective financial conditions correspond to 3.0-3.5%, the entire discussion about whether policy is "restrictive enough" is misframed. Can we construct a model-free measure of this wedge?

2. **Fiscal dominance threshold:** At what point does fiscal dominance become so severe that the Fed effectively loses control of inflation? The Sargent-Wallace unpleasant arithmetic suggests this happens when the real interest rate on government debt exceeds real GDP growth, forcing monetization. Are we approaching this? The term premium steepener may be the market's early warning signal.

3. **Private credit size threshold:** At what share of total credit creation does private credit's rate insensitivity materially change the Taylor Rule calibration? Currently at ~$200-300B/yr against ~$4-5T total credit creation, the effect is meaningful but not dominant. What happens at $500B-$1T/yr?

4. **Cross-central bank transmission:** If the Fed is constrained by fiscal dominance and impaired transmission, how does this propagate to ECB, BOJ, and BOE policy? Does the Fed's inability to tighten effectively force other central banks to do more, or does it create capital flow dynamics that export U.S. financial conditions globally?

5. **Endogenous vs exogenous resolution of the FCI divergence:** Will financial conditions eventually tighten to match the policy rate (through equity repricing, credit widening) or will the policy rate eventually move to match financial conditions (through cuts)? The historical base rate favoring rates markets ~60-65% of the time suggests the former, but post-COVID rates market track record is poor.

6. **Maturity wall interaction with QT:** Does the Fed's balance sheet runoff exacerbate the maturity wall by reducing demand for corporate bonds (portfolio rebalancing effect in reverse)? If QT widens spreads at the same time the maturity wall forces refinancing, the two tightening mechanisms compound non-linearly.

7. **Can the expectations channel be repaired?** If 5Y5Y expectations remain at 2.3% rather than 2.0%, does the Fed need to explicitly raise the inflation target to restore credibility, or would this further de-anchor expectations? The optimal control problem becomes intractable when the transmission mechanism itself is endogenous to policy credibility.
