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
