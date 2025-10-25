## MODIFIED Requirements

### Requirement: Spam classification ¡X baseline, recall improvement, and precision restoration (Phases 1-3)
The system SHALL provide a spam classification capability that: establishes a baseline model (Phase 1), offers hyperparameter tuning to improve recall (Phase 2), and provides threshold-sweep and recommendation tooling to restore precision while maintaining high recall (Phase 3).

#### Scenario: Download and prepare dataset
- **GIVEN** the dataset is available at `https://github.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity/blob/master/Chapter03/datasets/sms_spam_no_header.csv`
- **WHEN** the developer runs the data ingestion/preparation script
- **THEN** a cleaned dataset suitable for training is produced in `data/` and documented steps are available in the repository

#### Scenario: Train baseline SVM and evaluate (Phase 1)
- **GIVEN** the prepared dataset is available
- **WHEN** the developer runs the baseline training script
- **THEN** the training completes, a model artifact is saved, and evaluation metrics (accuracy, precision, recall, F1) are produced and stored in `reports/`

#### Scenario: Tune parameters to improve recall (Phase 2)
- **GIVEN** the prepared dataset and baseline metrics are available
- **WHEN** the developer runs the Phase 2 experiment runner with search ranges for `class_weight`, `ngram_range`, and `min_df`
- **THEN** the experiment runner returns a ranked list of parameter sets with their metrics, the best-performing set (by recall for the spam class) is recorded in `experiments/`, and a summary report is written to `reports/phase2-recall.md` describing improvements and trade-offs (precision vs recall)

#### Scenario: Threshold sweep and recommended settings to restore precision (Phase 3)
- **GIVEN** a trained model (with optional calibration) and Phase 2 results
- **WHEN** the developer runs the Phase 3 threshold sweep with a target recall level
- **THEN** the tool produces a ranked list of thresholds and parameter combinations showing precision/recall/F1 at each point, selects a recommended operating point that meets the target recall while maximizing precision, saves the recommendation and calibration artifacts in `experiments/`, and writes `reports/phase3-precision.md` summarizing results and trade-offs

#### Scenario: Sanity tests pass for experiments
- **GIVEN** a CI or local smoke test runs a reduced experiment
- **WHEN** the smoke test completes
- **THEN** scripts execute successfully and produce expected outputs or CI logs a failure for investigation
