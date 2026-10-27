# Bank Marketing Capstone — Day 41

## Problem Framing

- **Problem:** Help the bank use its marketing resources more effectively.
- **Decision:** Prioritize customers for telephone outreach.
- **User:** Bank marketing team.
- **Target:** `y` — whether the client subscribed to a term deposit.
- **Unit:** One recorded campaign observation.
- **Metric:** Average Precision (AP).
- **Baseline:** Assign every customer the training-set subscription rate as the score.
- **Good Enough:** Provisional AP of at least 0.20.
- **Failure:** Inputs are unavailable before outreach, the target is unreliable, or performance does not meaningfully improve beyond the baseline.

## Dataset

- **File:** bank-full.csv
- **Purpose:** Explore term-deposit marketing outcomes.
- **Limitations:** Possible repeated observations, unknown values, selection bias, and leakage from post-call information.

# Bank Marketing Capstone

## Day 41 — Project Scope

### Problem Statement
The goal is to help the bank prioritize customers for telephone marketing campaigns and improve the use of marketing resources.

### Dataset
- Dataset: Bank Marketing (`bank-full.csv`)
- Target column: `y`
- Target values: `yes` and `no`
- Unit of analysis: One recorded campaign observation.

### Evaluation Metric
Average Precision (AP) is used to evaluate how well the model ranks customers who subscribe to a term deposit.

### Baseline
The baseline assigns every customer the same score, calculated using the positive subscription rate in the training set.

- Training rows: 36,168
- Test rows: 9,043 - Training positive rate: 0.0673
- Baseline Average Precision: To be verified using the correct test labels and predictions.

# Decision Log — Bank Marketing Capstone

| Date | Decision | Why | What I gave up |
|---|---|---|---|
| 15/10/2026 | Selected the Bank Marketing dataset (`bank-full.csv`) | It provides customer and campaign information with a binary subscription target | Other datasets and problem domains |
| 15/10/2026 | Selected `y` as the target | The project aims to prioritize customers likely to subscribe to a term deposit | Predicting other business outcomes |
| 15/10/2026 | Selected Average Precision (AP) | It evaluates ranking quality when positive subscriptions are relatively uncommon | Simpler accuracy-based reporting |
| 15/10/2026 | Set the provisional GOOD ENOUGH target to AP ≥ 0.20 | Establishes a measurable improvement goal | Flexibility to choose a target after seeing results |
| 15/10/2026 | Planned an 80/20 train/test split | Keeps a separate evaluation set | Training on every available observation |
| 21/10/2026 | Investigated the reported test prevalence before accepting the baseline | The reported test rate of 0.3158 needs verification against the overall prevalence and split procedure | Immediate reliance on the original score |
| 21/10/2026 | Chose Logistic Regression on six obvious features as the strong baseline | It is interpretable, quick to train, and uses available pre-outreach information | Potential nonlinear relationships and more complex interactions |
| 21/10/2026 | Chose an untuned Random Forest as the first real model | It can learn nonlinear relationships using the available predictors | Interpretability and time spent comparing several model classes |
| 21/10/2026 | Used a preprocessing Pipeline | Keeps preprocessing fitted within each training split | A little extra setup compared with manual preprocessing |
| 21/10/2026 | Used five-fold stratified cross-validation | Measures how AP varies across validation folds | Some additional computation time |
| 21/10/2026 | Deferred hyperparameter tuning | Today's aim is to measure the first model honestly before tuning | Potential immediate gains from optimized settings |



## Day 42 — First Model and Baseline Comparison

### Evaluation setup

- **Target:** `y` — term-deposit subscription.
- **Metric:** Average Precision (AP).
- **GOOD ENOUGH target:** AP ≥ 0.20.
- **Evaluation:** Use the documented Day 41 split, after verifying target prevalence and label alignment.
- **Leakage prevention:** Preprocessing is fitted inside each Pipeline. The `duration` feature is excluded because it is unavailable before outreach.

### Model comparison

| What | AP Score | Difference vs Strong Baseline |
|---|---:|---:|
| Trivial baseline | 0.1170 | -0.0972 |
| Strong baseline — Logistic Regression | 0.2142 | 0.0000 |
| First real model — Random Forest | 0.6104 | 0.3962 |
| GOOD ENOUGH target | 0.2000 | -0.0142 |

### Variability check

- Five-fold cross-validation AP scores: [0.5789 0.608  0.621  0.6179 0.6137]
- Lowest AP: 0.5789
- Highest AP: 0.621
- Mean AP: 0.6079
- Spread (highest minus lowest): 0.042

The cross-validation spread indicates how much performance varies across the validation folds. Any claimed improvement must be interpreted relative to this variability.

### Gap to goal

- Current model AP: 0.6104
- Target AP: 0.2000
- Gap (target minus current AP): -0.4104
- Original distance from trivial baseline to target covered: 594.41%

**Assessment:** State whether the target has been reached and whether reaching it appears realistic with the remaining project days. Support the assessment with the observed scores and variability.

### Tomorrow's plan

**Chosen lever:** Feature engineering and predictor analysis, subject to today's results.

**Why:** The next step should address the observed gap rather than assume hyperparameter tuning is the best solution.

**Lever not being pulled:** Hyperparameter tuning is deferred until the baseline, first model, and evaluation variability are understood.

**Day 3 plan:** If the first model clearly beats the strong baseline, investigate the useful predictors. If it loses or the difference is smaller than the observed spread, investigate the signal and evaluation before claiming an improvement.

### Limitations

- Performance on the held-out data may differ from future campaign performance.
- The dataset may contain selection effects or repeated customer observations.
- Predictors must be available at the time the bank makes its outreach decision.
- A better AP score does not by itself demonstrate higher business profit or campaign effectiveness.


## Day 43 — Feature Engineering Results

### Objective

The objective was to test whether engineered features improve the Bank Marketing model's Average Precision (AP) score.

### Evaluation Method

Six candidate features were evaluated individually using cross-validation. Their gains were compared against the Day 42 score spread of `0.042`.

### Results

The individual feature gains were approximately between `-0.0001` and `+0.0002`. These changes are much smaller than the Day 42 score spread.

Therefore, no candidate feature demonstrated a clear improvement beyond the observed variation in model performance. The tested features were classified as inconclusive rather than being treated as proven improvements or meaningful regressions.

### Conclusion

The feature engineering experiments did not establish a reliable improvement over the existing model. The current model remains the reference point, and no engineered feature is considered a confirmed improvement at this stage.

The combined-feature experiment should only be reported if it was actually performed. Further evaluation may be needed before deciding whether any candidate feature should be retained.


## Day 44 — Tuning and Error Analysis

### Model Comparison

| Model | Holdout Average Precision |
|---|---:|
| Strong Logistic Regression | 0.2142 |
| Untuned Random Forest | 0.4284 |
| Tuned Random Forest | 0.4580 |

### Tuning Decision

- Tuning gain: `0.0296` AP.
- Three-split AP spread: `0.0225`.
- The observed tuning gain is greater than the measured split-to-split spread.
- This is encouraging evidence, but three splits do not guarantee that the improvement will generalize.

### Final Model Decision

The Tuned Random Forest was selected as the current final candidate because it achieved the highest reported holdout AP of `0.4580`.

### Trade-offs and Limitations

- Average Precision measures ranking quality, not campaign profit directly.
- A threshold of `0.5` is not automatically the best business threshold.
- False positives and false negatives can have different business costs.
- The `duration` feature was excluded because it is unavailable before the call.
- The model should be validated on future campaign data before deployment.

### Next Step

Complete the project handover by verifying dependencies, documenting run instructions, testing reproducibility, and preparing the final report and presentation.

