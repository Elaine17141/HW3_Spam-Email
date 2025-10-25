## ADDED Requirements

### Requirement: Spam classification baseline (Phase 1)
The system SHALL provide a baseline spam classification capability that trains a classical ML model (SVM) on a public SMS spam dataset and reports evaluation metrics.

#### Scenario: Download and prepare dataset
- **GIVEN** the dataset is available at `https://github.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity/blob/master/Chapter03/datasets/sms_spam_no_header.csv`
- **WHEN** the developer runs the data ingestion/preparation script
- **THEN** a cleaned dataset suitable for training is produced in `data/` and documented steps are available in the repository

#### Scenario: Train baseline SVM and evaluate
- **GIVEN** the prepared dataset is available
- **WHEN** the developer runs the baseline training script
- **THEN** the training completes, a model artifact is saved, and evaluation metrics (accuracy, precision, recall, F1) are produced and stored in `reports/`

#### Scenario: Sanity tests pass
- **GIVEN** the training pipeline is executed in CI for a small sample or smoke test
- **WHEN** the pipeline runs
- **THEN** basic sanity checks pass (scripts execute, outputs created), or the CI job reports failure with logs
