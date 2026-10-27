import argparse
from pathlib import Path

import joblib
import pandas as pd


def main():
    parser = argparse.ArgumentParser(
        description="Predict bank term-deposit subscription probabilities."
    )
    parser.add_argument("--input", required=True, help="Input CSV file")
    parser.add_argument("--output", required=True, help="Output CSV file")
    args = parser.parse_args()

    # Load saved model and metadata
    artifact_path = (
        Path(__file__).resolve().parents[1]
        / "models"
        / "bank_marketing_model.joblib"
    )

    artifact = joblib.load(artifact_path)
    model = artifact["model"]
    feature_columns = artifact["feature_columns"]

    # Load new customer data
    data = pd.read_csv(args.input, sep=";")

    # Check required columns
    missing = [
        column for column in feature_columns
        if column not in data.columns
    ]

    if missing:
        raise ValueError(
            f"Input CSV is missing required columns: {missing}"
        )

    # Keep the same features and order used during training
    X_new = data[feature_columns].copy()

    # Predict subscription probabilities
    probabilities = model.predict_proba(X_new)[:, 1]

    # Save probabilities and an explicitly defined 0.5-threshold label
    output = data.copy()
    output["subscription_probability"] = probabilities
    output["predicted_subscription"] = (
        probabilities >= 0.5
    ).astype(int)

    output_path = Path(args.output).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output.to_csv(output_path, index=False)

    print("Prediction completed successfully!")
    print("Model:", artifact["model_name"])
    print("Input rows:", len(data))
    print("Output file:", output_path)


if __name__ == "__main__":
    main()
