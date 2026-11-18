
# Fashion-MNIST Classification Using MLP

## Project Overview

This project classifies clothing images from the Fashion-MNIST dataset
using a Multi-Layer Perceptron (MLP).

Each image has dimensions of 28 x 28 pixels and belongs to one of
10 clothing categories.

## Dataset

- Training images: 60,000
- Test images: 10,000
- Image size: 28 x 28
- Input features: 784
- Classes: 10

## Models

- Logistic Regression baseline
- Plain Multi-Layer Perceptron
- Improved Multi-Layer Perceptron

## Results

- Logistic Regression validation accuracy: 0.8629
- Plain MLP validation accuracy: 0.8947
- Selected experiment: Learning Rate Scheduler
- Final validation accuracy: 0.9013
- Final test accuracy: 0.8900
- Final test accuracy percentage: 89.00%

## Confusion Matrix

![Confusion Matrix](artifacts/confusion_matrix.png)

## Technique Comparison

See `artifacts/technique_comparison.csv`.

## Decision Log

See `decision_log.md`.

## Model

Saved model: `models/fashion_mnist_mlp.pth`

## Important Note

The final test dataset was used only for the final evaluation.
Model selection and tuning were performed using validation data.
