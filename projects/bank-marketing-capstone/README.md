# Bank Marketing Subscription Prediction

## 1. Project purpose

This project builds a machine-learning model to help a bank prioritize
customers for term-deposit marketing outreach.

The model estimates the probability that a customer will subscribe to
a term deposit. The score can support prioritization, but it should not
be treated as a guarantee that a customer will subscribe.

## 2. Dataset

The project uses the Bank Marketing dataset in `data/bank-full.csv`.
The source file is semicolon-separated.

- Target: `y`
- Positive class: `yes` (customer subscribed)
- Negative class: `no` (customer did not subscribe)
- Rows: 45,211
- Feature `duration` is excluded because call duration is not available
  before the call and could cause target leakage in a pre-call workflow.

The dataset is not included in Git. Place the authorized dataset at
`data/bank-full.csv` before running the project.

## 3. Final model

Selected model: Tuned Random Forest

Holdout Average Precision: 0.4580

Average Precision is used because the subscription target is imbalanced.
It summarizes the precision-recall trade-off across classification
thresholds. It is not the same as accuracy.

The model artifact includes the fitted preprocessing and classifier,
along with the feature-column order.

## 4. Project structure

- `data/` — local dataset, not committed
- `notebooks/` — project experiments and analysis
- `models/bank_marketing_model.joblib` — saved fitted model
- `src/predict.py` — prediction script
- `reports/` — reports and generated prediction outputs
- `requirements.txt` — pinned Python package versions

## 5. Environment setup

Use Python in a virtual environment.

Create and activate one:

    python3 -m venv .venv
    source .venv/bin/activate

Install dependencies:

    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt

The model artifact was created with the pinned package versions.
Use compatible versions when loading the artifact.

## 6. Run predictions

From the repository root, run:

    python src/predict.py --input data/bank-full.csv --output reports/test_predictions.csv

The input must be a CSV with semicolon-separated columns matching
the original Bank Marketing dataset format. It must include all feature
columns used by the saved model.

The output preserves the input columns and adds:
- `subscription_probability`: predicted probability of subscription
- `predicted_subscription`: 1 when probability is at least 0.5,
  otherwise 0

The 0.5 threshold is a demonstration threshold, not a threshold
optimized for campaign capacity or business cost.

## 7. Evaluation and limitations

Day44 reported:
- Strong Logistic Regression: Average Precision 0.2142
- Untuned Random Forest: Average Precision 0.4284
- Tuned Random Forest: Average Precision 0.4580
- Tuning gain over untuned Random Forest: 0.0296
- Observed three-split spread for the untuned Random Forest: 0.0225

The tuning gain is encouraging, but the split-spread comparison is
only a rough variability check. It does not establish statistical
significance or guarantee future performance.

An earlier Day42 Random Forest result was 0.6104. Its difference from
the Day44 untuned result (0.4284) requires checking the split, features,
and evaluation setup before making a direct comparison.

The model should be tested on a genuinely separate, representative
dataset before operational use. Review subgroup performance, calibration,
threshold choice, fairness, data drift, and campaign outcomes before
using scores to make real customer decisions.
