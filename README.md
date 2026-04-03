🛡️ FraudShield AI: Vehicle Insurance Fraud Detection SystemFraudShield AI is a comprehensive end-to-end Machine Learning solution designed to detect fraudulent insurance claims. This project integrates data science, machine learning, and web development to provide a real-time prediction system.🚀 Project OverviewInsurance fraud costs companies billions annually. This project aims to automate the detection process using advanced gradient boosting algorithms. The system consists of:Machine Learning Pipeline: Data preprocessing, handling imbalance (SMOTE), and model selection.Backend API: A high-performance API built with FastAPI.Frontend Dashboard: An interactive user interface built with Streamlit.📊 Model PerformanceAfter evaluating 7 different classification models (Logistic Regression, KNN, SVM, Decision Tree, Random Forest, Naive Bayes, and XGBoost), XGBoost was selected as the champion model based on its superior F1-Score and ROC-AUC metrics, effectively handling the imbalanced nature of the dataset.ModelAccuracyF1-ScoreROC-AUCXGBoost0.8630.2230.678Random Forest0.8310.1220.593Logistic Regression0.6770.2190.577🛠️ Tech StackLanguage: Python 3.11Libraries: Pandas, NumPy, Scikit-learn, XGBoost, Imbalanced-learn (SMOTE).API Framework: FastAPI & Uvicorn.Frontend: Streamlit.Data Visualization: Seaborn & Matplotlib.📂 Project StructurePlaintext├── app.py                # Streamlit Web Interface
├── main.py               # FastAPI Backend Server
├── xgboost_fraud_model.pkl # Trained XGBoost Model
├── scaler.pkl            # Standard Scaler for preprocessing
├── requirements.txt      # Project Dependencies
└── Notebook.ipynb        # Data Analysis & Model Training History
⚙️ How to RunClone the repository:Bashgit clone https://github.com/Abdullahkamell/vehicle-fraud-detection.git
cd vehicle-fraud-detection
Install dependencies:Bashpip install -r requirements.txt
Start the FastAPI server:Bashuvicorn main:app --reload
Start the Streamlit dashboard: (In a new terminal)Bashstreamlit run app.py
👤 AuthorAbdullah - IT Student at Tanta UniversityDeveloped as part of the Digital Egypt Pioneers Initiative (DEPI).