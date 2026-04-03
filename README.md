# 🛡️ FraudShield AI: Vehicle Insurance Fraud Detection System

**FraudShield AI** is a comprehensive end-to-end Machine Learning solution designed to detect fraudulent insurance claims. This project integrates data science, machine learning, and web development to provide a real-time prediction system.

## 🚀 Project Overview
Insurance fraud costs companies billions annually. This project aims to automate the detection process using advanced gradient boosting algorithms. The system consists of:
1.  **Machine Learning Pipeline:** Data preprocessing, handling imbalance (SMOTE), and model selection.
2.  **Backend API:** A high-performance API built with **FastAPI**.
3.  **Frontend Dashboard:** An interactive user interface built with **Streamlit**.

## 📊 Model Performance
After evaluating 7 different classification models, **XGBoost** was selected as the champion model based on its superior **F1-Score** and **ROC-AUC** metrics.

| Model | Accuracy | F1-Score | ROC-AUC |
| :--- | :--- | :--- | :--- |
| **XGBoost** | **0.863** | **0.223** | **0.678** |
| Random Forest | 0.831 | 0.122 | 0.593 |
| Logistic Regression | 0.677 | 0.219 | 0.577 |

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **Libraries:** Pandas, NumPy, Scikit-learn, XGBoost, Imbalanced-learn (SMOTE).
* **API Framework:** FastAPI & Uvicorn.
* **Frontend:** Streamlit.

## 📂 Project Structure
```plaintext
├── app.py                # Streamlit Web Interface
├── main.py               # FastAPI Backend Server
├── xgboost_fraud_model.pkl # Trained XGBoost Model
├── scaler.pkl            # Standard Scaler for preprocessing
├── requirements.txt      # Project Dependencies
└── Notebook.ipynb        # Data Analysis & Model Training History
⚙️ How to Run
Clone the repository:

Bash
git clone [https://github.com/Abdullahkamell/vehicle-fraud-detection.git](https://github.com/Abdullahkamell/vehicle-fraud-detection.git)
cd vehicle-fraud-detection
Install dependencies:

Bash
pip install -r requirements.txt
Start the FastAPI server:

Bash
uvicorn main:app --reload
Start the Streamlit dashboard:

Bash
streamlit run app.py
👤 Author
Abdullah - IT Student at Tanta University

Developed as part of the Digital Egypt Pioneers Initiative (DEPI).