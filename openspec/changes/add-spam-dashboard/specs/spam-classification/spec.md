## MODIFIED Requirements

### Requirement: Spam classification ¡X baseline, recall, precision, and visualization (Phases 1-4)
The system SHALL provide a spam classification capability that: establishes a baseline model (Phase 1), offers hyperparameter tuning to improve recall (Phase 2), provides threshold-sweep and recommendation tooling to restore precision (Phase 3), and includes an interactive visualization/dashboard (Phase 4) to explore model behavior and choose operating points.

#### Scenario: Start dashboard and view ROC/PR curves
- **GIVEN** a trained model artifact and evaluation dataset
- **WHEN** the developer starts the Streamlit dashboard
- **THEN** the dashboard displays ROC and Precision-Recall curves and summary metrics (AUC, accuracy, precision, recall, F1)

#### Scenario: Interactively adjust threshold and inspect results
- **GIVEN** the dashboard is running with loaded predictions
- **WHEN** the user moves the threshold slider
- **THEN** precision, recall, F1, and confusion matrix update to reflect the selected threshold, and the user can export the selected threshold and parameters to `experiments/`

#### Scenario: Inspect individual samples
- **GIVEN** the dashboard is running
- **WHEN** the user selects a sample from the dataset
- **THEN** the dashboard shows the raw text, predicted probability, predicted label at current threshold, and ground-truth label

#### Scenario: CI smoke test for dashboard
- **GIVEN** a CI job runs a lightweight smoke test
- **WHEN** the test starts the dashboard headless (or verifies startup logs)
- **THEN** the test confirms the app starts and exits cleanly or reports failure for investigation
