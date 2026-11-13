
# Fashion-MNIST Decision Log

## 1. Baseline
Logistic Regression validation accuracy: 0.8629

## 2. Plain MLP
Plain MLP validation accuracy: 0.8947

## 3. Learning Rate
Selected learning rate: 0.003

## 4. Final Configuration
Selected experiment: Learning Rate Scheduler
Final configuration: {'hidden': 256, 'depth': 1, 'lr': 0.003, 'epochs': 12, 'use_scheduler': True}

## 5. Stability
Plain MLP average accuracy: 0.8846
Plain MLP spread: 0.0107

Final MLP average accuracy: 0.8895
Final MLP spread: 0.0053

## 6. Final Test
Test accuracy: 0.8900
Test accuracy percentage: 89.00%

## 7. Decision
The final model was selected using validation performance.
The official test set was evaluated only once after model selection.
