# 📊 Customer Churn Prediction (End-to-End Machine Learning Project)

## 🚀 Project Overview

This project aims to predict whether a customer will churn (leave the company) using machine learning techniques. The goal is to help businesses identify high-risk customers and take proactive retention actions.

---

## 🎯 Business Problem

Customer churn leads to revenue loss. Identifying customers likely to churn allows companies to:

* Improve retention strategies
* Reduce customer acquisition costs
* Increase overall profitability

---

## 📁 Dataset

* Telecom Customer Churn Dataset (Kaggle)
* Contains customer demographics, services, and billing information

---

## 🧹 Data Preprocessing

* Removed irrelevant columns (Customer ID, Churn Category, Churn Reason)
* Handled missing values using mean imputation
* Converted categorical variables using one-hot encoding
* Created target variable (`Churn`) from `Customer Status`

---

## 📊 Exploratory Data Analysis (EDA)

Key insights:

* Dataset is imbalanced (more non-churn customers)
* Customers with higher monthly charges churn more
* Month-to-month contract users are more likely to churn
* Customers with low tenure show higher churn rates

---

## 🤖 Models Used

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Random Forest Classifier

---

## 📈 Model Performance

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | ~81%     |
| KNN                 | ~71%     |
| Random Forest       | ~98%     |

---

## 🔍 Final Model Evaluation (Random Forest)

* Accuracy: **98%**
* Precision (Churn): **1.00**
* Recall (Churn): **0.94**
* F1-score: **0.97**

---

## 🧠 Key Insights

* Model effectively identifies churn customers (94% recall)
* High monthly charges strongly influence churn
* Short tenure customers are more likely to leave
* Contract type plays a major role in retention

---

## 💼 Business Recommendations

* Offer discounts or bundles to high-paying customers
* Encourage long-term contracts over month-to-month plans
* Improve onboarding experience for new customers
* Target high-risk customers with retention campaigns

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn

---

## 📌 Project Workflow

1. Data Cleaning
2. Exploratory Data Analysis
3. Feature Engineering
4. Model Building
5. Model Evaluation
6. Business Insights

---

## 📦 Future Improvements

* Hyperparameter tuning
* Feature scaling for better performance
* Deployment using Streamlit
* Handling class imbalance using SMOTE

---

## 🏆 Conclusion

This project demonstrates an end-to-end machine learning pipeline for solving a real-world business problem. The model provides actionable insights that can help reduce customer churn and improve business performance.

---

## 👤 Author

VANSHIKA SHARMA
