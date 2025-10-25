## Why
After improving recall in Phase 2, the model may suffer precision degradation (more false positives). Phase 3 aims to restore precision while maintaining the high recall achieved, by sweeping decision thresholds and recommended parameter settings and selecting operating points that balance precision and recall for production trade-offs.

## What Changes
- MODIFIED: `spam-classification` capability to include Phase 3 requirements for precision restoration and recommended settings.
- ADDED: Experimentation scripts to sweep decision thresholds and evaluate precision at target recall levels.
- ADDED: A recommendation report that prescribes parameter settings and decision thresholds for deployment (with trade-off analysis).

## Scope (Phase 3)
- Run threshold sweeps on calibrated model probabilities to find operating points that satisfy target recall while maximizing precision.
- Evaluate precision@recall-target and choose recommended parameter sets (including tuned `class_weight`, `ngram_range`, `min_df`, and threshold) based on validation and holdout datasets.
- Produce a reproducible `reports/phase3-precision.md` with recommended settings, example confusion matrices, and notes on expected precision/recall trade-offs.

## Impact
- Affected specs: `spam-classification` (MODIFIED)
- Affected code: `ml/experiments/` (new scripts for threshold sweeps), `ml/` training pipeline to accept threshold/params, `reports/` to store recommendations.

## Migration
- No data migration required. Phase 3 produces recommended settings and artifacts; operators may choose to adopt them when deploying.

## Non-Goals
- Full production rollout or continuous model serving; Phase 3 focuses on offline experiments and recommended configurations.
