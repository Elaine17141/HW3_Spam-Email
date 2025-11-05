# Spam Email Classifier (AIoT-DA2025 HW3)


A simple, reproducible pipeline to classify messages/emails as spam or ham using scikit-learn and OpenSpec. This project emphasizes extensible preprocessing, experimentation, and visualization.

---

## Key Features

- Text preprocessing and cleaning (handles URLs, emails, phone numbers, etc.)  
- TF-IDF feature extraction  
- Logistic regression classification  
- Interactive Streamlit dashboard:  
  - Dataset and column pickers  
  - Class distribution visualization and top tokens per class  
  - Confusion matrix, ROC, and PR curves  
  - Threshold slider for live precision/recall/F1 adjustment  
  - **Live inference:** type a message to see predicted label and spam probability  
- Adjustable classification threshold  
- Full evaluation metrics: accuracy, precision, recall, F1 score  


## Demo Site

- (https://hw3spam-email-8iqzxwggjhjpygnadkppnv.streamlit.app/) 

---

## Setup

Recommended: use a fresh virtual environment.

```bash
pip install -r requirements.txt
```

---

## Project Structure
```bash
├── app/ # Streamlit application
│ └── streamlit_app.py # Interactive dashboard
├── datasets/ # Datasets
│ ├── processed/ # Preprocessed data
│ └── sms_spam_no_header.csv # Raw dataset
├── ml/ # Machine learning scripts
├── models/ # Trained model artifacts
├── reports/ # Training reports and visualizations
│ └── visualizations/ # Visualization charts
└── scripts/ # Training and evaluation scripts
```


## Data

- **Raw dataset (headerless, 2-column CSV):** [`datasets/sms_spam_no_header.csv`](datasets/sms_spam_no_header.csv)
- **Cleaned dataset (generated):** [`datasets/processed/sms_spam_clean.csv`](datasets/processed/sms_spam_clean.csv)

---

## Commands

### Preprocess (saves per-step outputs, optional)

```bash
python scripts/preprocess_emails.py \
  --input datasets/sms_spam_no_header.csv \
  --output datasets/processed/sms_spam_clean.csv \
  --no-header --label-col-index 0 --text-col-index 1 \
  --output-text-col text_clean \
  --save-step-columns \
  --steps-out-dir datasets/processed/steps
```

### Train

```bash
python scripts/train_spam_classifier.py \
  --input datasets/processed/sms_spam_clean.csv \
  --label-col col_0 --text-col text_clean
```

### Predict (single text)

```bash
python scripts/predict_spam.py --text "Free entry in 2 a wkly comp to win cash"
```

### Predict (batch CSV)

```bash
python scripts/predict_spam.py \
  --input datasets/processed/sms_spam_clean.csv \
  --text-col text_clean \
  --output predictions.csv
```

---

## Notes

- Trained artifacts (vectorizer, model, label mapping) are saved to [`models/`](models/) for reuse
- See [`docs/PREPROCESSING.md`](docs/PREPROCESSING.md) for detailed step-by-step preprocessing with examples
- OpenSpec usage: 
  ```bash
  openspec validate add-spam-email-classifier --strict
  ```
- Recommended Setting: Aim for Precision ≥ 0.90, Recall ≥ 0.93

### Training with recommended flags

```bash
python scripts/train_spam_classifier.py \
  --input datasets/processed/sms_spam_clean.csv \
  --label-col col_0 --text-col text_clean \
  --class-weight balanced \
  --ngram-range 1,2 \
  --min-df 2 \
  --sublinear-tf \
  --C 2.0 \
  --eval-threshold 0.50
```
**Observed (held-out):** Precision ≈ 0.923, Recall ≈ 0.966, F1 ≈ 0.944.

---

## Visualization

Visual reports are saved under [`reports/visualizations/`](reports/visualizations/).

#### Class Distribution
```bash
python scripts/visualize_spam.py \
  --input datasets/processed/sms_spam_clean.csv \
  --label-col col_0 \
  --class-dist
```

#### Token Frequency (top 20 per class)
```bash
python scripts/visualize_spam.py \
  --input datasets/processed/sms_spam_clean.csv \
  --label-col col_0 --text-col text_clean \
  --token-freq --topn 20
```

#### Confusion Matrix, ROC, PR Curves  
*(requires trained artifacts in `models/`)*
```bash
python scripts/visualize_spam.py \
  --input datasets/processed/sms_spam_clean.csv \
  --label-col col_0 --text-col text_clean \
  --models-dir models \
  --confusion-matrix --roc --pr
```

#### Threshold Sweep (CSV + plot)
```bash
python scripts/visualize_spam.py \
  --input datasets/processed/sms_spam_clean.csv \
  --label-col col_0 --text-col text_clean \
  --models-dir models \
  --threshold-sweep
```

---

## Streamlit App

Launch the interactive dashboard:

```bash
streamlit run app/streamlit_app.py
```

### Features

- Dataset and column pickers
- Class distribution and top tokens by class
- Confusion matrix, ROC/PR curves (requires trained artifacts in models/)
- Threshold slider with live precision/recall/f1
- **Live Inference:** Type a message to see predicted label and spam probability (shown with a probability bar and threshold marker)
- Quick test buttons ("Use spam example" / "Use ham example")
  - Auto-fill input and try prediction instantly

---

## Deploy to Streamlit Cloud

1. Push this repo to GitHub *(done)*.
2. Go to [Streamlit Cloud](https://share.streamlit.io), click “New app,” and select:
   - Repository: `Elaine17141/HW3_Spam-Email`
   - Branch: `main`
   - Main file: `app/streamlit_app.py`
3. Wait for build to finish.  
   The app uses prebuilt artifacts in `models/`, enabling instant use.

---

## Project Status

Phases 1–4 are complete and archived.  
See the final summary: [`docs/FinalReport.md`](docs/FinalReport.md).

---

## References

- [Hands-On-Artificial-Intelligence-for-Cybersecurity (Packt)](https://github.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity.git)
- UCI & Kaggle SMS Spam datasets (see data source files above)
- scikit-learn, Streamlit documentation

---

## License

MIT License (see [`LICENSE`](LICENSE) for details)
