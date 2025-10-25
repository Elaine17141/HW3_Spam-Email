## MODIFIED Requirements

### Requirement: Spam classification baseline (Phase 1) and recall improvement (Phase 2)
The system SHALL provide a baseline spam classification capability that trains a classical ML model on a public SMS spam dataset and reports evaluation metrics. In Phase 2 the system SHALL provide experimental tooling to improve recall for the spam class by tuning training and feature-extraction parameters.

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

#### Scenario: Sanity tests pass for experiments
- **GIVEN** a CI or local smoke test runs a small experiment (subset or reduced search)
- **WHEN** the smoke test completes
- **THEN** scripts execute successfully and produce expected outputs or CI logs a failure for investigation
