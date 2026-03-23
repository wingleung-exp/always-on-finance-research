# Global Sovereign Debt Sustainability — Behavioral Finance Critic & Historical Falsifier Analysis

## Key Claims

1. **The concept of "sovereign debt sustainability" is itself analytically unstable: its definition shifts between solvency (can the government pay?), liquidity (can it roll over?), and political willingness (will it choose to pay?) — and most analysis conflates these three distinct failure modes, producing systematically miscalibrated risk assessments.** For own-currency issuers, solvency in the traditional sense is a category error (they can always create currency to pay), making "sustainability" primarily a question of inflation tolerance and political economy, not arithmetic. Applying the same "sustainability" framework to the US (own-currency, reserve issuer) and Sri Lanka (foreign-currency-denominated debt, limited reserves) treats fundamentally different risk structures as commensurable.

2. **The Reinhart-Rogoff "90% debt/GDP threshold" has been debunked (correctly recognized in KB concept `debt_gdp_threshold_debunked`), but the threshold-seeking impulse persists in subtler forms throughout sovereign debt analysis — including the 5-signal fiscal dominance sequence, the "r>g activation point," and the "net private-sector absorption >4% GDP" trigger — all of which are threshold models fitted to small samples and suffer from the same fundamental problem: the search for a clean break in what is actually a continuous, state-dependent relationship.** The desire for thresholds is driven by anchoring bias (needing a reference number) and the availability heuristic (dramatic threshold-crossing narratives are more memorable than gradual deterioration stories).

3. **Standard sovereign debt sustainability analysis exhibits a systematic DM-EM asymmetry bias: DM sovereign risk is almost exclusively analyzed through a "slow deterioration" lens, while EM sovereign risk is analyzed through a "sudden stop" lens — but the historical record shows that DM sovereigns CAN experience sudden stops (UK 2022, Italy 2011) and EM sovereigns CAN persist with "unsustainable" metrics for decades (India, Brazil).** This asymmetry produces overconfidence about DM resilience timelines and overconfidence about EM vulnerability timelines.

4. **The base rate for sovereign default among own-currency issuers with domestic-law debt is near zero in the modern era, making "sovereign default risk" a misleading frame for countries like the US, UK, or Japan. The actual risk is not default but REAL VALUE EROSION through inflation, financial repression, and currency depreciation — which is a different risk with different dynamics, different hedges, and different distributional consequences.** Framing the risk as "default risk" activates the wrong mental models (binary outcomes, sudden events, legal proceedings) rather than the correct ones (gradual erosion, regime shifts, portfolio rebalancing).

5. **Japan's 250%+ debt/GDP without crisis is not an "outlier" or "special case" — it is the single most informative data point for sovereign debt sustainability analysis in advanced economies, and the persistent framing of Japan as an exception rather than the central case reveals confirmation bias toward the crisis narrative.** Every theory of sovereign debt sustainability must FIRST explain Japan before making predictions about other advanced economies. The standard modifiers ("domestic ownership," "current account surplus," "cultural savings propensity") are ad hoc rescue hypotheses — they were not predicted by the theories in advance, they were invoked after Japan failed to conform.

6. **The "contagion" framing for EM sovereign stress (identified as a knowledge gap: "EM sovereign stress contagion mechanisms") imports an epidemiological metaphor that mischaracterizes the actual transmission mechanism. EM sovereign crises are not contagious in the biological sense — they co-occur because they share common causes (DM tightening cycles, dollar strength, commodity price collapses, risk appetite withdrawal).** The contagion metaphor encourages the narrative fallacy (Argentina "infected" Turkey) rather than the correct causal model (both were vulnerable to the same external shock). This distinction matters for risk assessment: the contagion frame suggests the crisis spreads FROM weak EMs TO strong ones, while the common-cause frame suggests ALL vulnerable EMs are hit simultaneously by the external shock, but strong EMs are largely unaffected regardless of "proximity" to the crisis.

7. **CBO-style fiscal trajectory projections, which underpin most US sovereign debt sustainability analysis, have a systematic bias: they assume current law (not current policy) and project forward mechanically, producing alarming debt paths that have NEVER materialized as projected because political responses (revenue increases, spending cuts, or inflation) intervene before the projected trajectory is realized.** CBO's 10-year deficit projections have overstated realized cumulative deficits by an average of ~15-25% over the past three decades (excluding recession years), but analysts treat these projections as base cases rather than the upper-bound scenarios they empirically represent.

8. **The "r-g" framework for sovereign debt sustainability (Blanchard 2019), while theoretically elegant, is being applied with false precision: the current KB concept (`r_g_transition_sustainability`) states r≈g implies "35-40% probability of fiscal stress within 10 years," but this base rate is derived from a heterogeneous cross-country panel that includes countries with fundamentally different monetary architectures, and "fiscal stress" is defined loosely enough to encompass everything from austerity programs to sovereign restructurings.** The framework is useful directionally (r>g makes sustainability harder) but the quantitative precision is illusory.

## Evidence & Reasoning

### BIAS AUDIT

**Bias 1: Category Error in "Sustainability" — Framing Effect**

The word "sustainability" in sovereign debt analysis triggers a mental model borrowed from household or corporate finance: an entity that borrows more than it can repay will eventually go bankrupt. This framing is appropriate for entities that cannot create the currency in which they borrow. For own-currency issuers, the constraint is not solvency but inflation tolerance — a fundamentally different question.

Evidence this framing distorts analysis:
- The KB concept `deficit_term_premium_doom_loop` describes the loop "activating" when r>g, using language borrowed from corporate distress analysis. But for the US, r>g doesn't create a solvency problem — it creates a political problem (interest expense crowds other spending) and potentially an inflation problem (if monetized). The "activation" metaphor implies a discrete failure event when the actual dynamic is continuous and political.
- CDS markets price US sovereign default risk at ~30-40bp, implying <2% 5-year cumulative default probability. Markets clearly distinguish between US sovereign risk and actual default candidates. The analytical frameworks used in this research project should reflect the same distinction rather than lumping them into a common "sustainability" bucket.
- The IMF's Debt Sustainability Analysis (DSA) framework, designed primarily for countries that CAN default on foreign-currency debt, is frequently applied to own-currency issuers. When the IMF applies the DSA to the US or Japan, it produces alarming charts that look similar to pre-default EM DSAs — but the transmission mechanism is entirely different.

**Bias 2: Threshold-Seeking as Anchoring**

After Reinhart-Rogoff's 90% threshold was debunked, the field shifted to more sophisticated thresholds: the 5-signal sequence, the r>g crossing, the "4% of GDP net private-sector absorption" trigger, the "interest expense > defense spending" milestone. These are all threshold models with the same epistemological problem as the original: they impose a discontinuity on a continuous process.

Why analysts seek thresholds:
- **Anchoring**: Without a threshold, analysts cannot produce a clear "watch level" or "risk level," which is uncomfortable for both the analyst and the consumer of the analysis.
- **Narrative convenience**: "The US has crossed 3 of 5 signals" is a more compelling story than "the US has gradually increasing fiscal pressures that may or may not produce negative outcomes over an indeterminate time horizon."
- **Action bias**: Thresholds create urgency. Continuous deterioration doesn't.

The empirical problem: in the KB's own evidence, the 5-signal sequence has N=3-4 cases with 4 different pathways (as documented in my iter_0016 analysis). The "4% absorption" threshold has N=7. The r>g panel has modest sample size with substantial heterogeneity. None of these samples is large enough to identify a genuine discontinuity.

**Bias 3: Asymmetric Temporal Framing (DM vs. EM)**

DM sovereign debt analysis emphasizes slow-moving variables: debt/GDP trends, structural deficit trajectories, demographic pressures, entitlement growth. The implicit time horizon is 5-20 years.

EM sovereign debt analysis emphasizes fast-moving variables: reserve coverage, current account dynamics, capital flow reversals, FX pressure. The implicit time horizon is 6-24 months.

This asymmetry is partially justified by structural differences (EM foreign currency debt, thinner markets, weaker institutions) but introduces two systematic biases:

- **For DM**: The slow-moving framing creates complacency about tail risks. Italy 2011 and UK 2022 showed that DM sovereigns CAN face sudden liquidity crises. The comfortable "we have years to address this" timeline can collapse to days.
- **For EM**: The sudden-stop framing creates excessive alarm about countries that have successfully carried high debt for decades. India (government debt ~80-85% of GDP, persistent fiscal deficits of 6-9% including state governments) has never experienced a sovereign debt crisis despite violating every "sustainability" threshold. Brazil has run primary deficits and high debt with only moderate stress events.

**Bias 4: Survivorship Bias in Default Studies**

Studies of sovereign default (Reinhart & Rogoff "This Time Is Different," Sturzenegger & Zettelmeyer "Debt Defaults and Lessons from a Decade of Crises") systematically study countries that defaulted. This generates a biased picture of what happens at high debt levels. Countries that had high debt and DIDN'T default include:

- **Belgium** (debt/GDP peaked ~140% in 1993, never defaulted, deleveraged over 20 years)
- **Italy** (debt/GDP ~120-150% for 30+ years, never defaulted, repeated near-misses resolved by ECB)
- **Japan** (250%+, 30+ years, no default)
- **Canada** (peaked ~100% in mid-1990s, successfully consolidated)
- **US post-WWII** (120%+, deleveraged over 35 years through repression + growth)
- **India** (80-85%+ with state governments, persistent deficits, no sovereign crisis)

If the base rate includes non-defaulters, the probability of default at any given debt level drops substantially. The literature's focus on defaults is analogous to studying plane crashes to estimate the safety of air travel without counting successful flights.

**Bias 5: Recency Bias in Contagion Narratives**

The knowledge gap "EM sovereign stress contagion mechanisms" frames the question as if contagion is a primary transmission mechanism. This framing is heavily influenced by the most memorable EM crises:

- **1997-98 Asian crisis**: Often narrated as contagion (Thailand → Indonesia → Korea → Russia → Brazil). But the common causes were: pegged exchange rates + current account deficits + short-term foreign currency debt + DM capital withdrawal. The countries that were NOT affected (China, India) lacked these vulnerabilities — they didn't resist contagion, they simply weren't exposed to the common cause.
- **2013 Taper Tantrum**: Simultaneously hit the "Fragile Five" (Brazil, India, Indonesia, Turkey, South Africa). Not contagion — common vulnerability to Fed tightening expectations, with the magnitude proportional to each country's current account deficit and foreign positioning in local bonds.
- **2022**: Turkey and Sri Lanka experienced sovereign stress in the same year. No analyst seriously argues contagion — the causes were entirely idiosyncratic (Turkish monetary policy heterodoxy, Sri Lankan political/fiscal collapse).

The actual mechanism is common-factor exposure, not contagion. The distinction matters: contagion models predict cascading failures (weak → strong), common-factor models predict simultaneous failures (all weak hit at once, strong unaffected).

### LOGICAL CONSISTENCY CHECK

**Contradiction 1: "Unprecedented" + "Base Rates"**

The KB correctly identifies the US fiscal configuration as "unprecedented" (`us_fiscal_unprecedented_configuration`, confidence 9). Simultaneously, multiple concepts apply historical base rates to forecast US outcomes (`r_g_transition_sustainability`: 35-40% stress probability; `fiscal_consolidation_difficulty`: 30% success rate). These are logically incompatible: if the situation is truly unprecedented, historical base rates are, by definition, drawn from a different population. The base rates provide a starting point but their applicability discount should be much larger than is currently reflected.

This contradiction was flagged in my iter_0016 analysis (Internal Contradiction 1) and remains structurally unresolved. It is not enough to acknowledge unprecedented conditions and then proceed to apply historical base rates with modest confidence adjustments — the unprecedented nature should fundamentally change how we estimate probabilities.

**Contradiction 2: Sustainability Arithmetic vs. Political Economy**

The r-g framework is a mechanical accounting identity: if r>g persistently, debt/GDP rises without primary surpluses. But the policy response to rising debt service is NOT mechanical — it is political. The US has historically responded to rising interest costs with fiscal adjustment (1990, 1993, 1997, 2011). These adjustments were messy, incomplete, and politically painful, but they happened.

The contradiction: sustainability models project forward mechanically (CBO-style), but the political response function is non-linear and state-dependent. The very projections that generate alarm (e.g., "interest costs will reach 5% of GDP by 2035") change the political calculus and make adjustment more likely. This is a classic Lucas Critique problem — the model assumes behaviors don't change in response to the model's own implications.

**Contradiction 3: Japan as Both Warning and Counterexample**

This carries over from my iter_0016 analysis but is even more central to the sovereign debt sustainability topic:

- Japan's debt/GDP exceeds any threshold ever proposed
- Japan has experienced all 5 fiscal dominance signals
- Japan has NOT experienced: sovereign default, hyperinflation, currency collapse, bond market crisis
- Japan HAS experienced: stagnation, deflation/disinflation, demographic decline, and (recently) moderate inflation

If Japan is an analogue for US sovereign debt trajectory, the most likely outcome is 1-2 decades of sub-optimal growth with moderate financial repression — NOT crisis. If Japan is NOT an analogue, then the analyst must specify WHY, and the reasons given ("domestic ownership," "current account surplus") need to be tested as predictive variables, not invoked as post-hoc explanations.

**Unstated Assumption: Markets Price Sovereign Risk Correctly**

Much sovereign debt analysis treats market indicators (CDS spreads, term premia, yield curve shape) as revealing "the market's view" of sustainability. But sovereign bond markets have demonstrated systematic failures of risk pricing:

- Greek 10Y yields traded within 30bp of German Bunds throughout 2001-2007, despite Greece running persistent deficits with falsified statistics. The market was not pricing sovereign risk; it was pricing the implicit ECB guarantee — which turned out to be partially correct (Greece was eventually bailed out, though with restructuring).
- Argentine bonds rallied in 2017-18 on Macri's reform agenda, then collapsed. The market was pricing a political narrative, not a fiscal fundamental.
- US Treasuries rallied during periods of rising deficits (2020-2021) because the Fed was buying. The market price reflected the buyer of last resort, not sustainability fundamentals.

If markets can be systematically wrong about sovereign risk for years (Greece), treating market prices as informative signals about sustainability introduces a circularity: the analysis uses market prices to validate sustainability concerns, but the market prices may reflect positioning, liquidity, and policy rather than fundamental risk assessment.

### HISTORICAL FALSIFICATION

**Test 1: "High debt/GDP leads to sovereign crises in advanced economies."**

Advanced economies with peak debt/GDP >100% since 1945:

| Country | Peak Debt/GDP | Year of Peak | Sovereign Crisis? | Outcome |
|---------|--------------|-------------|-------------------|---------|
| US | ~120% | 1946 | No | Deleveraged to 30% over 35 years via repression + growth |
| UK | ~270% | 1946 | No | Deleveraged over 40 years; sterling devaluation 1967 |
| Japan | ~250%+ | Ongoing | No | Stagnation, not crisis; 30+ years |
| Italy | ~155% | 2020 | Near-miss | ECB backstop resolved; no default |
| Belgium | ~140% | 1993 | No | Gradual consolidation over 20 years |
| Canada | ~100% | 1995 | No | Successful consolidation; surplus by 1997 |
| Greece | ~180% | 2011 | YES | Restructuring 2012; BUT foreign-currency-equivalent (Euro, no monetary sovereignty) |
| Ireland | ~120% | 2012 | Near-miss | Bailout + austerity; BUT banking crisis, not fiscal |

Base rate for sovereign crisis at >100% debt/GDP among advanced economies with own-currency debt: **0 out of 6** (excluding Greece/Ireland as Eurozone/banking-specific). This is the most important empirical fact in sovereign debt sustainability analysis, and it is systematically underweighted because it makes for a boring conclusion.

**Test 2: "r>g produces fiscal stress within 10 years with 35-40% probability."**

The KB cites this base rate from cross-country panels. But sample composition matters enormously:

- **Full panel (all advanced economies)**: Includes Eurozone members who face genuine external constraints (no own monetary policy, no own currency, no lender of last resort until 2012). These countries SHOULD have higher fiscal stress rates at r>g because they face real solvency constraints.
- **Own-currency issuers only (US, UK, Japan, Canada, Australia, Sweden, Norway)**: Among this group, episodes of r>g that produced "fiscal stress" in the 10-year window are substantially rarer. The US had r>g through much of the 1980s-90s; the outcome was political adjustment (deficit reduction deals), not fiscal stress. The UK had r>g periodically; the outcomes were austerity programs, not sovereign crises.
- **Definition of "fiscal stress"**: If it includes IMF programs, market-forced austerity, and sovereign restructuring, the base rate is much lower for own-currency issuers. If it includes any period of politically painful fiscal adjustment, the base rate is meaninglessly high (every country has done this).

The 35-40% figure likely reflects the full panel including Eurozone and EM economies. For the US specifically, the historical base rate is probably closer to 10-20% if "fiscal stress" means market-driven crisis, and 50-60% if it means "politically painful but manageable adjustment."

**Test 3: "EM sovereign crises spread through contagion."**

Testing the contagion vs. common-cause hypothesis across major EM episodes:

- **1994-95 Tequila Crisis**: Mexico devalued; Argentina, Brazil experienced pressure. BUT: Argentina had a currency board with real overvaluation; Brazil had ongoing inflation concerns. Both were independently vulnerable. The Philippines, Chile, and Colombia — which had flexible exchange rates and lower external debt — experienced minimal spillover.
- **1997-98 Asian Crisis**: Thailand → Indonesia → Korea sequential timing suggests contagion. BUT: All three had pegged exchange rates, current account deficits, and short-term foreign currency borrowing. China, India (both with capital controls) were largely unaffected. The "contagion" was information revelation (investors realized the vulnerabilities were common) plus common creditor withdrawal (Japanese banks pulled from all of Asia simultaneously).
- **2001-02 Argentina**: Argentina defaulted; no significant contagion to other Latin American sovereigns. Brazil experienced some pressure but this was driven by domestic election uncertainty (Lula's first campaign), not Argentine contagion.
- **2013 Taper Tantrum**: The "Fragile Five" were hit simultaneously — not sequentially. This is inconsistent with contagion (sequential) and consistent with common-cause (simultaneous response to Fed signaling).

The evidence supports common-cause over contagion in 4 of 4 major episodes. The contagion frame persists because it is a more compelling narrative (crisis "spreading" like a virus is vivid and memorable — availability bias).

**Test 4: "CBO projections provide reliable baseline forecasts."**

CBO's track record for 10-year cumulative deficit projections (excluding years where a recession hit that CBO didn't forecast):
- CBO has systematically overestimated deficits during expansion periods (1990s tech boom revenue surprise, 2021-22 inflation-driven revenue surge) and underestimated deficits during recession/crisis periods (2008-09, 2020).
- The projections assume current law, which means they include legislated tax increases and spending caps that Congress routinely waives. This creates a structural downward bias in revenue (when tax cuts are extended) and upward bias in spending relative to projections.
- Net result: CBO 10-year projections are most useful as a "current policy inertia" scenario, not as a forecast. They are directionally informative (debt is rising) but their specific numbers should be discounted by the historical error margin (~15-25% on cumulative deficits).

### CALIBRATION ASSESSMENT

| Claim | Stated/Implied Confidence | Assessed Calibration | Adjustment Rationale |
|-------|--------------------------|---------------------|----------------------|
| 1. "Sustainability" concept is unstable | N/A (novel claim) | 8/10 | This is a definitional/conceptual point grounded in the well-established distinction between monetary-sovereign and non-sovereign issuers. The Modern Monetary Theory literature, Blanchard's own caveats, and market pricing (CDS) all support the distinction. |
| 2. Threshold-seeking persists | N/A (novel claim) | 8/10 | Follows directly from the documented debunking of R-R and the small-N problem already established in the KB. The psychological mechanism (anchoring) is well-documented in Kahneman's work. |
| 3. DM-EM asymmetry bias | N/A (novel claim) | 7/10 | Directionally confident but the degree of bias is hard to quantify. India/Brazil as counterexamples are strong; the DM sudden-stop cases (UK, Italy) are somewhat special circumstances. |
| 4. Default risk is wrong frame for own-currency issuers | High in literature | 9/10 | Near-tautological for own-currency domestic-law debt. The only counterexample would be a voluntary default by an own-currency issuer, which has essentially no modern precedent. |
| 5. Japan is central case, not outlier | Implicit low (treated as exception) | 7/10 | Confidence is moderated by the genuine possibility that Japan's specific structural features (savings culture, domestic ownership, current account surplus, demographic dynamics) may be load-bearing rather than coincidental. But the burden of proof should be on those claiming Japan is special, not on those treating it as the base case. |
| 6. Contagion is misframed | Moderate (KB gaps) | 8/10 | Historical falsification strongly supports common-cause over contagion across all major episodes examined. The academic literature (Forbes & Rigobon 2002, "No Contagion, Only Interdependence") supports this reframing. |
| 7. CBO projections are biased upward | Moderate | 6/10 | Directionally confident that CBO projects higher deficits than materialize during expansions, but the current configuration (unprecedented deficits at full employment, potential structural spending increases) may reduce the historical overstatement bias. The error margin estimate (15-25%) is rougher than I would like. |
| 8. r-g base rate has false precision | 7/10 (KB) | 5/10 for US-specific application | The theoretical framework is sound; the quantitative application to the US specifically is compromised by sample composition issues and the distinction between "fiscal stress" definitions. |

**Meta-calibration**: The sovereign debt sustainability literature has a demonstrated track record of excessive alarm. The "fiscal crisis" that was widely predicted after 2010 (when US debt/GDP crossed 100%) has not materialized in 16 years. The "Japanese sovereign crisis" predicted since the mid-1990s has not materialized in 30+ years. The "Italian sovereign crisis" has been repeatedly predicted and repeatedly resolved by institutional responses. A well-calibrated sovereign debt analyst should update toward longer timelines and milder outcomes than the standard frameworks suggest — not because the risks are zero, but because the modal outcome for advanced economy fiscal stress is slow erosion, not crisis.

### IMPROVED FRAMING

**Instead of**: "Sovereign debt sustainability analysis"
**Better**: "Sovereign fiscal regime analysis" — because the question for own-currency issuers is not "can they pay?" but "what fiscal regime will emerge?" (financial repression, moderate inflation, austerity, stagnation, or some combination).

**Instead of**: "Japan is an outlier with debt/GDP of 250%+"
**Better**: "Japan is the best-documented case of what happens when an advanced economy with monetary sovereignty runs debt/GDP far beyond any proposed threshold. The outcome — decades of stagnation with low rates, not crisis — should be the prior for similar economies until there is affirmative evidence of different dynamics."

**Instead of**: "EM sovereign stress contagion mechanisms"
**Better**: "Common-factor vulnerability framework for EM sovereign stress — identifying which EMs share exposure to specific external shocks (DM tightening, dollar strength, commodity collapse) rather than modeling 'contagion' from one EM to another."

**Instead of**: "The US has a 35-40% probability of fiscal stress within 10 years"
**Better**: "Cross-country panels suggest a 35-40% base rate for some form of fiscal adjustment when r≈g, but this includes Eurozone countries with genuine solvency constraints. For own-currency reserve-issuer nations, the base rate for MARKET-FORCED adjustment is probably 10-20%, while the base rate for POLITICALLY-DRIVEN adjustment (deficit reduction deals, spending sequestration) is 50-60%. The latter is unpleasant but not a crisis."

**Instead of**: "CBO projects debt/GDP will reach X% by 2035"
**Better**: "Under current-law assumptions with no political response, CBO projects debt/GDP will reach X% by 2035. Historical experience suggests actual deficits will be ~15-25% below these projections due to revenue surprises and political adjustments — but the current configuration is unprecedented, so the historical error margin may not apply."

## Confidence Assessment

| Claim | Confidence | Justification |
|-------|-----------|---------------|
| 1. "Sustainability" concept conflation | 8/10 | Well-established distinction in academic literature (Blanchard, MMT theorists, Bossone); supported by market pricing (CDS near zero for own-currency issuers). Core conceptual point. |
| 2. Threshold-seeking persists despite R-R debunking | 8/10 | Observable in KB concepts. The psychological mechanism is well-documented. Small-N problem confirmed at confidence 9 in KB. |
| 3. DM-EM asymmetry bias | 7/10 | Strong directional case with counterexamples on both sides. Moderated because the asymmetry is partially justified by real structural differences. |
| 4. Default risk is wrong frame | 9/10 | Near-tautological for own-currency domestic-law debt. Zero modern precedents of voluntary own-currency default. |
| 5. Japan is central case | 7/10 | Strong argument but genuinely uncertain whether Japan's structural features are load-bearing. The burden-of-proof argument is epistemically sound but could be wrong if Japanese exceptionalism is real. |
| 6. Contagion is misframed | 8/10 | Historical evidence across 4 major episodes consistently supports common-cause. Academic literature (Forbes & Rigobon) corroborates. |
| 7. CBO bias | 6/10 | Directionally right but magnitude uncertain. Current configuration may break the historical pattern of overestimation. |
| 8. r-g false precision | 7/10 | The precision critique is mathematical/statistical. Uncertainty about the CORRECT base rate for the US specifically. |

**Meta-calibration note**: My confidence levels for process critiques (claims 1, 2, 4, 6) are appropriately higher than for empirical claims (3, 5, 7, 8) because process errors can be identified independently of knowing the correct answer. I can be confident that a model is over-fitted without knowing what the correct model is. I can be confident that a base rate is drawn from the wrong population without knowing the correct population base rate.

## Connections to Other Topics

- **Fiscal Dominance (`fiscal_dominance`)**: Sovereign debt sustainability is the parent question; fiscal dominance is one specific pathway within the sovereign debt regime space. My iter_0016 critique of the fiscal dominance framework carries over directly: the 5-signal sequence is over-fitted, the Japan counterexample is inadequately addressed, and the crisis narrative is overweighted relative to the financial repression/stagnation scenario. The KB's own `financial_repression_modal_outcome` concept (confidence 7) supports the "boring middle" scenario as more probable than crisis — this should be the central organizing insight for sovereign debt sustainability analysis.

- **Yield Curve Dynamics (`yield_curve_dynamics`)**: Term premium is the primary market channel through which sovereign debt concerns are transmitted. The `term_premium_fiscal_supply_nonlinear` concept captures the supply-demand mechanism. My critique: the non-linearity claims are based on small samples and the "4% absorption" threshold is another threshold-seeking exercise. Term premium also reflects duration supply/demand, flight-to-quality flows, and Fed communication — fiscal sustainability is ONE input, not the primary driver.

- **FX Regimes (`fx_regimes`)**: The DM-EM distinction in sovereign debt analysis maps directly onto FX regime analysis. Fixed/pegged exchange rates transform fiscal sustainability from a domestic political question into an external balance-of-payments question — which is WHY EM crises look different from DM crises. The `em_twin_deficit_vulnerability` concept correctly identifies external balance as the key discriminant. Currency regime is the single most important variable in sovereign debt sustainability analysis, yet it is treated as a modifier rather than the primary classifier.

- **Inflation Regimes**: The `financial_repression_modal_outcome` concept — moderate 3-6% inflation as the resolution mechanism for high DM sovereign debt — connects sovereign debt directly to inflation regime analysis. If financial repression IS the modal outcome, then the investment implication is not "hedge for sovereign default" but "hedge for persistent negative real returns on nominal bonds." This reframing changes the portfolio construction advice dramatically.

- **Central Bank Policy**: The independence of monetary policy from fiscal pressures is the core institutional question. The Treasury-Fed Accord precedent (1951) shows that the boundary between monetary and fiscal policy is negotiated, not fixed. Current tensions (Fed on hold while deficits are 6-7% of GDP) are real but do not yet constitute fiscal dominance by any historical standard — the Fed tightened aggressively in 2022-23 DESPITE fiscal concerns.

- **Credit Markets**: Sovereign debt sustainability connects to credit through the sovereign-bank nexus (bank holdings of government bonds create mutual vulnerability) and through the "risk-free rate" convention (if the risk-free rate is questioned, all credit pricing shifts). The basis trade amplification channel (`basis_trade_fiscal_amplification`) is the most concrete and testable connection between sovereign debt dynamics and broader market stability.

## Open Questions

1. **What is the right analytical framework for sovereign debt when the standard framework (solvency analysis) doesn't apply?** For own-currency issuers, the question is not "can they pay?" but "what will the real cost of their fiscal choices be?" This is fundamentally a political economy question, not a financial one, and our analytical tools are weaker for political economy. Is there a way to formalize the "political willingness to inflate vs. willingness to adjust" trade-off that goes beyond scenario analysis?

2. **Is Japan's experience generalizable or structurally unique?** This is the single most important empirical question in sovereign debt analysis. The answer determines whether the "boring middle" (financial repression, stagnation, gradual erosion) is the base case for all advanced economies or a Japan-specific outcome. Specifically: (a) Is domestic ownership of government debt a necessary condition for stability, and if so, is US domestic ownership (~70% of public debt, declining from ~80%) sufficient? (b) Does the current account surplus matter, and if so, what is the threshold? (c) Is the BoJ's credibility in maintaining low rates a unique institutional feature, or can any own-currency central bank do this?

3. **Can we build a falsifiable model of sovereign debt sustainability?** The current frameworks (5-signal sequence, r-g, doom loop) are not falsifiable in practice because they do not specify timeframes for their predictions, they include ad hoc modifiers for inconvenient cases, and they are compatible with any outcome. A genuinely useful sovereign debt sustainability model should specify: (a) testable predictions with timeframes, (b) explicit conditions under which the model would be considered wrong, (c) probability bounds rather than point estimates.

4. **What is the correct comparison class for US sovereign debt risk?** Is the US best compared to: (a) Japan (own-currency, high debt, deep capital markets, domestic ownership) — suggesting stagnation, not crisis; (b) Post-WWII US itself (high debt, financial repression, strong growth) — suggesting successful deleveraging is possible; (c) The UK 2022 (DM near-miss) — suggesting sudden tail risks; (d) No comparison (truly unprecedented) — suggesting all historical base rates are uninformative? The answer to this question determines whether quantitative forecasting is possible at all.

5. **How should the knowledge base incorporate "nothing happened" as evidence?** The strongest evidence about advanced economy sovereign debt sustainability is NEGATIVE: Japan hasn't had a crisis in 30 years, the US hasn't had a crisis in 80 years, Italy's near-misses have been resolved by institutional responses. But negative evidence is invisible — it doesn't generate memorable narratives, dramatic case studies, or publishable research. How can the analytical framework systematically incorporate the evidential weight of non-events?

6. **What distinguishes EM sovereigns that carry high debt successfully (India, Brazil for extended periods) from those that don't (Sri Lanka, Argentina)?** If the discriminant is not debt/GDP level itself (which it clearly is not), what ARE the key variables? Currency denomination of debt, reserve adequacy, institutional quality, and capital account openness are candidates — but we need a framework that weights these variables rather than listing them as qualitative modifiers.
