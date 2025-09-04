# 🔐 Securing Online Payments: AI-based Fraud Detection for E-commerce Platforms

This repository contains the **code, reports, and prototype web application** developed for my **MSc Research Project** at the *National College of Ireland*.  

The project aims to **detect fraudulent online transactions in real-time** using **machine learning** and provide a working prototype via a **Flask web application**.

---

## 📌 Project Overview
- 📊 **Dataset**: [PaySim (Synthetic Mobile Money Transactions)](https://www.kaggle.com/datasets/ealaxi/paysim1)  
- 🧠 **Models Trained**: Logistic Regression, Random Forest, XGBoost  
- ⚖️ **Class Imbalance Handling**: SMOTE oversampling + undersampling  
- 🔎 **Best Performing Model**: **XGBoost** (Accuracy: 96.6%, ROC-AUC: 0.9958)  
- 🖥 **Prototype**: Flask-based web app that classifies transactions as `Fraudulent` or `Not Fraudulent`  

---

## 📂 Repository Structure
fraud-detection-ai/
│── app.py # Flask web application
│── Code.ipynb # Jupyter notebook with training workflow
│── requirements.txt # Python dependencies
│── dataset-link.txt # Kaggle dataset link
│── README.md # Project documentation
│
├── reports/
│ ├── Research Report.pdf
│ ├── Configuration Manual.pdf
│ └── Presentation.pptx
│
├── images/
│ ├── plot.png
│ └── newplot.png


---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/fraud-detection-ai.git
cd fraud-detection-ai

2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Run the Application
python app.py


The app will start at: http://127.0.0.1:5000

🧪 Methodology

Exploratory Data Analysis (EDA) – statistical insights, fraud distribution, transaction patterns

Feature Engineering – added:

balance_change_org

balance_change_dest

amount_to_oldbalanceOrg_ratio

amount_to_oldbalanceDest_ratio

Data Balancing – applied SMOTE oversampling and undersampling

Scaling & PCA – standardized features and reduced dimensionality

Model Training – compared Logistic Regression, Random Forest, XGBoost

Evaluation Metrics – Accuracy, Precision, Recall, F1-score, ROC-AUC

📊 Results

XGBoost was the most effective model:

✅ Accuracy: 96.6%

✅ ROC-AUC: 0.9958

✅ F1-score (Fraud class): 0.97

Balanced performance: lowest false positives (170) and false negatives (175).

🚀 Future Work

Incorporate Explainable AI (XAI) (e.g., SHAP, LIME) for interpretability.

Deploy on cloud infrastructure (AWS/GCP/Azure) for real-time monitoring.

Extend to Graph Neural Networks (GNNs) to detect collusive fraud rings.

Add concept drift monitoring for retraining on new fraud patterns.

📚 References

Research Report & Configuration Manual included in /reports/
Dataset: PaySim on Kaggle

👨‍💻 Author: Anurag Jaipal Rathore
🎓 MSc in Data Analytics, National College of Ireland
📅 Submission Date: August 11, 2025
