# Intelligent Sales Analytics & Customer Churn Prediction

An end-to-end machine learning application that analyzes customer purchasing behavior and predicts the likelihood of customer churn.

The project combines **Python, Pandas, Scikit-learn, Machine Learning, FastAPI, HTML, CSS, and JavaScript** to create a complete analytics and prediction system.

---

## Project Overview

Customer retention is an important business problem for online retailers.

This project uses historical transaction data to:

- Analyze customer purchasing behavior
- Create customer-level features
- Identify customers at risk of churn
- Train and evaluate machine learning models
- Generate churn probability
- Classify customers into Low, Medium, and High risk
- Expose the trained model through a REST API
- Provide a web-based dashboard for predictions

---

## Business Problem

Online retailers have thousands of customers, making it difficult to manually identify customers who may stop purchasing.

The objective of this project is to answer:

> **"Which customers are likely to churn, and how can we identify them early?"**

The prediction system can help businesses prioritize customers for retention campaigns and personalized offers.

---

## Dataset

The project uses the **Online Retail dataset**, containing transaction-level information such as:

- Invoice Number
- Stock Code
- Product Description
- Quantity
- Invoice Date
- Unit Price
- Customer ID
- Country

The original transaction data was transformed into customer-level features for machine learning.

---

## Data Processing

The data processing pipeline includes:

1. Loading the transaction dataset
2. Removing invalid records
3. Handling missing customer IDs
4. Removing cancelled transactions
5. Creating revenue values
6. Converting invoice dates
7. Extracting year, month, quarter and day-of-week
8. Aggregating transactions at customer level
9. Creating customer behavior features
10. Creating the churn target

---

## Customer Features

The final model uses seven features:

| Feature | Description |
|---|---|
| TotalSpent | Total amount spent by the customer |
| TotalOrders | Number of orders placed |
| TotalQuantity | Total number of products purchased |
| AverageOrderValue | Average spending per order |
| CustomerLifetime | Duration of customer activity |
| Recency | Days since the customer's last purchase |
| Frequency | Customer purchase frequency |

These features capture different aspects of customer purchasing behavior.

---

## Churn Definition

The project defines churn based on future customer purchasing behavior.

Historical customer activity is used to predict whether a customer is likely to stop purchasing during the defined future period.

The target variable is:

```text
0 → Not Churned
1 → Churned

## 🤖 Machine Learning

The following models were evaluated:

- Logistic Regression
- Random Forest
- XGBoost

Evaluation metrics:

**Accuracy, Precision, Recall, F1 Score**

### Final Model Performance

The final Logistic Regression model achieved:

| Metric | Score |
|---|---:|
| Accuracy | 65.81% |
| Precision | 60.39% |
| Recall | 63.92% |
| F1 Score | 62.10% |

The model uses 7 customer behavioral features.

## 🌐 FastAPI

The trained model is deployed using **FastAPI**.

### Endpoint

```text
POST /predict
Example Request
{
  "TotalSpent": 500,
  "TotalOrders": 3,
  "TotalQuantity": 20,
  "AverageOrderValue": 166.67,
  "CustomerLifetime": 100,
  "Recency": 80,
  "Frequency": 3
}
Example Response
{
  "churn_prediction": 0,
  "churn_probability": 0.3921,
  "risk_level": "LOW"
}
💻 Web Dashboard

The frontend was developed using:

HTML
CSS
JavaScript

The dashboard sends customer information to the FastAPI backend and displays the prediction, churn probability, and risk level.

Application Architecture
              Customer Data
                   ↓
             Web Dashboard
                   ↓
              FastAPI API
                   ↓
          Trained ML Model
                   ↓
        ┌──────────┴──────────┐
        ↓                     ↓
 Churn Prediction       Churn Probability
                              ↓
                         Risk Level
🛠️ Technologies

Programming: Python, JavaScript, SQL, HTML, CSS

Data Analysis: Pandas, NumPy, Matplotlib, Seaborn

Machine Learning: Scikit-learn, Logistic Regression, Random Forest, XGBoost

Backend: FastAPI, Uvicorn, Pydantic

Development: Jupyter Notebook, Git, GitHub

📁 Project Structure
Intelligent-Sales-Analytics/
│
├── backend/
├── data/
├── frontendtype/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── ml-api/
│   ├── main.py
│   ├── churn_model.pkl
│   ├── scaler.pkl
│   ├── features.pkl
│   └── requirements.txt
├── notebooks/
│   └── 01_data_exploration.ipynb
├── python/
│   ├── data_cleaning.py
│   ├── eda.py
│   ├── feature_engineering.py
│   └── train_model.py
├── sql/
│   ├── schema.sql
│   └── analysis_queries.sql
├── .gitignore
└── README.md
▶️ How to Run
1. Clone
git clone https://github.com/Gaurang-S-Hegde/intelligent-sales-analytics.git
cd intelligent-sales-analytics
2. Create Environment
python -m venv venv

Windows:

venv\Scripts\activate
3. Install Dependencies
pip install -r ml-api/requirements.txt
4. Start FastAPI
cd ml-api
uvicorn main:app --reload

API:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs
5. Start Frontend

Open another terminal:

cd frontendtype
python -m http.server 5500

Open:

http://127.0.0.1:5500
🔮 Future Improvements
Customer segmentation
SHAP model explainability
Advanced model tuning
Interactive analytics charts
Automated retention recommendations
Database integration
Cloud deployment
Model monitoring and automated retraining
👨‍💻 Author

Gaurang S. Hegde
B.Tech Information Technology

Interests: Data Analytics • Machine Learning • AI • Full Stack Development

📌 Project

Intelligent Sales Analytics & Customer Churn Prediction

Built as an end-to-end portfolio project demonstrating Data Analytics + Machine Learning + API Development + Frontend Integration.


### After replacing the README

Run these **three commands** in PowerShell:

```powershell
git add README.md
git commit -m "Add professional project README"
git push
