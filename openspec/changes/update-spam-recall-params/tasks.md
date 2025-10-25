## 1. Implementation (Phase 2 - Improve Recall)
- [ ] 1.1 Add `ml/experiments/` with an experiment runner that accepts hyperparameter ranges for `class_weight`, `ngram_range`, and `min_df`.
- [ ] 1.2 Implement a grid or randomized search script (`ml/experiments/tune_recall.py`) using cross-validation and focusing on recall for the spam class.
- [ ] 1.3 Add utilities to compare results and produce a `reports/phase2-recall.md` summarizing best parameters and trade-offs.
- [ ] 1.4 Add minimal tests/smoke checks for the experiment runner (sample dataset, small search) to run in CI if desired.
- [ ] 1.5 Update `ml/train.py` to accept recommended parameters and persist the tuned model artifact.
- [ ] 1.6 Document how to reproduce experiments and how to interpret metrics (README / docs/).
- [ ] 1.7 Request review and iterate

## 2. Validation
- [ ] 2.1 Confirm recall improvement over baseline on validation set or document if trade-offs prevent improvement.
- [ ] 2.2 Save reproducible experiment artifacts (parameters, scores, random seeds) in `experiments/` and `reports/`.

## 3. Future (out of scope for Phase 2)
- [ ] 3.1 Deploy tuned model to serving infra
- [ ] 3.2 Production monitoring and drift detection
