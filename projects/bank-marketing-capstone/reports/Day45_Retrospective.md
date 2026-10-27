# Peer Review Questions

1. Can a new user follow the README to install the dependencies and run
   the project without asking the author for help?

2. Are the baseline and final Average Precision results reported under
   comparable evaluation conditions, and is the earlier Day42 result
   explained?

3. Is preprocessing fitted only on training data and then reused
   unchanged on validation, holdout, and new prediction data?

# Day45 Retrospective

## Biggest time sink and whether it was worth it
The project involved repeated debugging of notebook paths, preprocessing,
model comparison, and environment setup. These steps were necessary to
make the workflow reproducible, although a clearer project structure
earlier would likely have reduced rework.

## Decision that shaped the result
Using Average Precision and excluding `duration` shaped the evaluation
and kept the intended pre-call prediction task realistic.

## Day1 belief that changed
A more complex model or more engineered features do not automatically
produce a better result. Improvements must be measured against a baseline
and compared with observed variation.

## What should change in Phase 3
Start each task with explicit input/output paths, a reproducible split,
a baseline, and a written decision rule. Save experiment results and
environment versions. Verify that the same preprocessing is used during
training and prediction.

## Remaining unknowns
The difference between Day42 AP 0.6104 and Day44 AP 0.4284 needs
investigation. Performance on genuinely new data, subgroup behavior,
probability calibration, and the best operating threshold also remain
unknown.
