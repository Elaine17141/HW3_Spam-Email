# 垃圾簡訊分類系統

這是一個基於機器學習的垃圾簡訊（Spam）分類系統，使用 TF-IDF 和邏輯迴歸模型來識別垃圾簡訊。該系統包含完整的訓練流程、互動式儀表板，以及即時預測功能。

## 功能特點

- 文本預處理和清理
- 使用 TF-IDF 進行文本特徵提取
- 使用邏輯迴歸進行分類
- 互動式 Streamlit 儀表板，包含：
  - 資料分布視覺化
  - 模型性能評估
  - 即時預測介面
- 可調整的分類閾值
- 完整的評估指標（準確率、精確率、召回率、F1分數）

## 系統需求

- Python 3.6+
- 相依套件列表請見 `requirements.txt`

## 專案結構

```
.
├── app/                    # Streamlit 應用程式
│   └── streamlit_app.py    # 互動式儀表板
├── datasets/              # 資料集
│   ├── processed/         # 處理後的資料
│   └── sms_spam_no_header.csv  # 原始資料
├── ml/                   # 機器學習相關程式碼
├── models/               # 訓練好的模型
├── reports/              # 訓練報告和視覺化
│   └── visualizations/   # 視覺化圖表
└── scripts/              # 訓練和評估腳本
```

## 安裝說明

1. 克隆專案：
```bash
git clone [專案網址]
cd [專案資料夾]
```

2. 安裝相依套件：
```bash
pip install -r requirements.txt
```

## 使用說明

### 訓練模型

運行訓練腳本：
```bash
python scripts/train_spam_classifier.py
```

可選參數：
- `--input`: 輸入CSV檔案路徑
- `--test-size`: 測試集比例 (預設: 0.2)
- `--seed`: 隨機種子 (預設: 42)
- `--C`: 邏輯迴歸正則化參數 (預設: 1.0)

### 啟動儀表板

運行 Streamlit 應用程式：
```bash
streamlit run app/streamlit_app.py
```

儀表板功能：
- 資料分布視覺化
- 常見詞彙分析
- 模型性能評估
- 即時預測介面

## 主要特色

- 文本預處理：自動處理 URL、電子郵件、電話號碼等特殊文本
- 可調整的分類閾值：根據需求平衡精確率和召回率
- 視覺化工具：提供完整的模型性能視覺化
- 即時預測：支援單條訊息的即時分類預測
