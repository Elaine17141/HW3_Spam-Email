## 1. Implementation (Phase 3 - Restore Precision with High Recall)
- [ ] 1.1 Add `ml/experiments/threshold_sweep.py` to sweep classification thresholds and compute precision/recall/F1 across thresholds.
- [ ] 1.2 Add probability calibration utilities (`ml/experiments/calibrate.py`) if needed (Platt scaling or isotonic) to produce reliable probabilities.
- [ ] 1.3 Implement a script to recommend operating points given a target recall (e.g., `ml/experiments/recommend_settings.py`) that combines tuned hyperparameters with threshold selection.
- [ ] 1.4 Produce `reports/phase3-precision.md` with recommended settings, confusion matrices, and trade-off analysis.
- [ ] 1.5 Add reproducibility artifacts: seeds, parameter snapshots, and example inference code showing how to apply threshold in inference.
- [ ] 1.6 Add minimal tests/smoke checks for threshold sweep and calibration (small sample run) that can execute in CI as a lightweight job.
- [ ] 1.7 Update `ml/train.py` or pipeline to persist probability calibration and recommended threshold with the saved model artifact.
- [ ] 1.8 Request review and iterate

## 2. Validation
- [ ] 2.1 Verify that recommended settings achieve the target recall on the validation set and report resulting precision.
- [ ] 2.2 Document any remaining trade-offs and recommend whether the configuration is suitable for production or requires further tuning.
