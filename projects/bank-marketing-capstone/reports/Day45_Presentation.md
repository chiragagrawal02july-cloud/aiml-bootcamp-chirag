# Slide 1 — Problem and user

- User: bank marketing team
- Decision: which customers to prioritize for outreach
- Prediction: probability of term-deposit subscription
- Metric: Average Precision
- Constraint: exclude `duration` because it is unavailable before the call

Speaker note:
The goal is to support a ranking decision, not to guarantee customer
behavior or claim that the model causes subscriptions.

# Slide 2 — Approach

- Established a baseline
- Compared Logistic Regression and Random Forest
- Tested engineered features
- Tuned Random Forest using RandomizedSearchCV
- Saved preprocessing and model together in a pipeline

Speaker note:
The project used measured comparisons rather than keeping a feature or
model merely because it seemed more sophisticated.

# Slide 3 — Results

| Model | Holdout AP |
|---|---:|
| Strong Logistic Regression | 0.2142 |
| Untuned Random Forest | 0.4284 |
| Tuned Random Forest | 0.4580 |

- Tuning gain: 0.0296 AP
- Three-split untuned-model spread: 0.0225 AP
- Day1 target: AP >= 0.20

Speaker note:
The tuning gain exceeded the observed spread in this experiment, but
three splits are not proof that the gain will generalize. Day42's earlier
0.6104 Random Forest result still needs reconciliation with Day44.

# Slide 4 — Key decisions and errors

- Average Precision chosen for an imbalanced target
- `duration` excluded to avoid an unavailable-at-decision-time feature
- Engineered features not retained without convincing evidence
- False positives cost outreach time; false negatives may miss subscribers
- The 0.5 threshold is a demonstration default

Speaker note:
A practical deployment needs an operating threshold tied to campaign
capacity, error costs, and subgroup performance.

# Slide 5 — Handover and next steps

- Saved model: `models/bank_marketing_model.joblib`
- Prediction entry point: `src/predict.py`
- Dependencies pinned in `requirements.txt`
- Prediction CSV successfully generated for 45,211 rows
- Next: fresh-environment test, reconcile evaluation scores, assess
  subgroup performance, calibration, and threshold choice

Speaker note:
The script runs on the supplied dataset, but an independent new-data test
and operational validation remain necessary.
