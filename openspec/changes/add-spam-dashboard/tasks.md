## 1. Implementation (Phase 4 - Visualization & Streamlit Dashboard)
- [ ] 1.1 Create `apps/streamlit/` with `app.py` that can load a saved model artifact and evaluation data
- [ ] 1.2 Implement visualization utilities (`ml/utils/visualize.py`) for ROC curve, PR curve, confusion matrix, and class distribution plots
- [ ] 1.3 Add interactive controls in the Streamlit app: threshold slider, metric targets, sample inspection (view raw text and prediction probability)
- [ ] 1.4 Implement export/save feature to write recommended thresholds/settings to `experiments/` and `reports/`
- [ ] 1.5 Add a minimal `requirements-streamlit.txt` and update docs with run instructions
- [ ] 1.6 Add a CI smoke test that starts the Streamlit app in headless mode and checks an endpoint or logs for successful start
- [ ] 1.7 Add sample dataset snapshot (`data/sample_for_dashboard.csv`) for demo runs
- [ ] 1.8 Write README/docs for the dashboard usage and interpretation guidance
- [ ] 1.9 Request review and iterate

## 2. Optional
- [ ] 2.1 Package the dashboard as a Docker image for easy sharing
