## Why
Interactive visualization helps humans understand classifier behavior, choose operating points, and debug failure modes. A Streamlit dashboard enables quick exploration of model predictions, thresholds, and evaluation metrics without building a full web UI.

## What Changes
- ADDED: New capability `spam-dashboard` providing an interactive Streamlit app for model inspection and threshold tuning.
- ADDED: Visualization utilities (ROC/PR curves, confusion matrix, class distributions), example notebooks, and a small demo dataset snapshot.
- ADDED: Documentation for running the dashboard locally and example export of recommended thresholds.

## Scope (Phase 4)
- Build a Streamlit dashboard that loads a trained model artifact and evaluation data, presents metrics and plots, and lets users interactively adjust decision thresholds and view resulting precision/recall/confusion matrices.
- Provide export functionality to save recommended thresholds and settings to `experiments/`.
- Include a minimal CI smoke test to ensure the app starts and sample pages render (headless check).

## Impact
- Affected specs: `spam-classification` (MODIFIED, adds visualization requirement) and new capability `spam-dashboard` (ADDED)
- Affected code: `apps/streamlit/` (dashboard), `ml/` visualization utilities, `reports/` for exported snapshots, and documentation.

## Migration
- No data migration required. This is an additive tooling feature to assist model selection and analysis.

## Non-Goals
- Full production web service for serving predictions is out of scope. The dashboard is for local/ops use and experimentation only.
