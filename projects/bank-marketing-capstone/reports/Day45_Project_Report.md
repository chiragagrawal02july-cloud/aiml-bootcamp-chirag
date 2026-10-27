# Bank Marketing Capstone — Project Report

## 1. Problem and intended user

The intended user is a bank marketing team deciding which customers
to prioritize for term-deposit outreach. The model estimates subscription
probability so the team can rank customers for review.

The model supports prioritization; it does not prove that contacting a
customer will cause a subscription. The main evaluation metric is Average
Precision (AP), which is useful when positive outcomes are relatively rare.

## 2. Data and approach

The project uses the Bank Marketing dataset (`bank-full.csv`), containing
45,211 rows. The target is `y`, with `yes` mapped to the positive class.
The dataset is semicolon-separated.

The workflow included problem scoping, a simple baseline, Logistic
Regression, Random Forest, feature-engineering experiments, hyperparameter
tuning, split-variability checks, and error analysis.

The `duration` feature was excluded because it is not known before a
customer call and would not be suitable for pre-call prioritization.

The fitted preprocessing and selected classifier were saved together in
a scikit-learn pipeline. The selected artifact is a Tuned Random Forest.
The prediction script loads the artifact, checks required input columns,
uses the same preprocessing, and writes probabilities and demonstration
labels to a CSV file.

## 3. Results

Day44 holdout results:

| Model | Holdout Average Precision |
|---|---:|
| Strong Logistic Regression | 0.2142 |
| Untuned Random Forest | 0.4284 |
| Tuned Random Forest | 0.4580 |

The tuning gain over the untuned Random Forest was 0.0296 AP.
The observed spread across three random splits for the untuned model
was 0.0225 AP. The gain exceeded that observed spread and the
precommitted improvement threshold of 0.005. This is encouraging evidence,
but three splits are not a formal statistical significance test.

The project’s initial target was AP >= 0.20. The Day44 selected model
scored 0.4580, which is 0.2580 above that target.

An earlier Day42 experiment recorded Random Forest AP of 0.6104.
Day44 recorded 0.4284 for its untuned Random Forest. These results should
not be treated as directly comparable until their splits, features,
preprocessing, and evaluation conditions have been verified.

## 4. Error analysis and operational risk

The model outputs probabilities rather than certain outcomes. False
positives may cause the team to spend time contacting customers who do
not subscribe; false negatives may cause potential subscribers to be
missed.

A useful next analysis is to compare precision and recall at the number
of customers the campaign team can realistically contact, and to inspect
errors by customer subgroup. Any subgroup analysis should use adequate
sample sizes and be reviewed for fairness and business impact.

The 0.5 label threshold in the prediction script is only a demonstration
default. It has not been established as the best threshold for campaign
capacity or the relative costs of false positives and false negatives.

## 5. Important decisions and alternatives

1. **Metric — Average Precision.** Accuracy alone can hide poor detection
   of the minority positive class. AP was retained to evaluate ranking
   quality across thresholds.

2. **Exclude `duration`.** It may be strongly associated with the outcome,
   but it is not available before a call. Including it would not fit the
   intended pre-call use case.

3. **Do not automatically keep engineered features.** Experiments with
   age decade, balance per age, campaign count, previous contact, and
   month quarter did not show clear gains beyond the observed variation.
   The evidence was insufficient to justify keeping them.

4. **Tune only after establishing a baseline.** RandomizedSearchCV tested
   20 configurations with three-fold Average Precision scoring. Tuning
   was retained because the holdout gain was 0.0296, above the observed
   untuned-model split spread of 0.0225. This is promising, not conclusive.

5. **Save preprocessing with the model.** A single fitted pipeline reduces
   the risk of applying different transformations during prediction.

## 6. Limitations and next steps

The dataset may not represent future campaigns or all customer groups.
Observed split spread is based on only three seeds, and the comparison
with the earlier Day42 result needs reconciliation. The 0.5 threshold
has not been optimized for campaign capacity. The model has not yet been
validated on a genuinely new dataset or monitored in production.

Next steps:
- Verify the Day42 versus Day44 evaluation difference.
- Evaluate precision and recall at realistic outreach capacity.
- Check subgroup performance and probability calibration.
- Test the script with a separate file containing unseen records.
- Establish a threshold with the campaign team.
- Monitor drift and outcomes before any operational deployment.

## 7. Handover verification

The saved model artifact was created successfully. The prediction script
processed 45,211 rows from the supplied dataset and produced an output
CSV with 45,211 rows. This verifies the basic inference workflow on the
available dataset, but it is not an independent validation of model
performance.
