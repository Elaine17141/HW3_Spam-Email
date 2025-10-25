## Why
The baseline spam-classification model may prioritize overall accuracy but underperform on recall (missing spam). Phase 2 focuses on improving recall for the spam class by tuning model training parameters and text feature extraction hyperparameters.

## What Changes
- MODIFIED: `spam-classification` capability to include Phase 2 requirements for improving recall.
- ADDED: Experimental scripts and tooling to run hyperparameter searches over `class_weight`, `ngram_range`, and `min_df`.
- ADDED: Documentation of experiment results and a reproducible pipeline for comparing models.

## Scope (Phase 2)
- Explore parameter adjustments and grid/random search for:
  - `class_weight` (to handle class imbalance)
  - `ngram_range` (unigrams, bigrams, etc.)
  - `min_df` (min document frequency to filter rare tokens)
- Evaluate models by focusing on recall for the spam class while reporting precision and F1.
- Produce a recommended parameter set and document trade-offs (e.g., precision vs recall).

## Impact
- Affected specs: `spam-classification` (MODIFIED)
- Affected code: `ml/` scripts for training/experiments, `reports/` for results, optional CI job for a lightweight experiment smoke-test.

## Migration
- No data migration required. Existing baseline artifacts remain; Phase 2 will produce new artifacts and reports.

## Non-Goals
- Large-scale deployment/serving of the tuned model.
- Extensive model architecture changes (this phase focuses on feature/hyperparameter tuning only).
