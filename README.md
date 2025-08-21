# -Telco-Customer-Churn-Prediction
Customer churn is a major concern in the telecommunications industry, where  retaining existing customers is far more cost-effective than acquiring new ones. This project aims to build a predictive model that helps detect  potential churners using machine learning techniques.
Telco Customer Churn Prediction

📌 Project Overview

Customer churn is one of the biggest challenges in the telecom industry, where retaining existing customers is significantly more cost-effective than acquiring new ones. This project focuses on building a machine learning–based predictive model to identify customers at risk of leaving, enabling telecom providers to take proactive retention measures.

We used the Telco Customer Churn dataset (Kaggle, IBM sample data), which includes customer demographics, service usage, billing details, and churn labels. Our solution applies a structured data science pipeline covering data preprocessing, model development, evaluation, and deployment automation.

🔹 Key Objectives

Analyze historical customer data to uncover churn patterns.

Build predictive models to classify churn vs. non-churn customers.

Handle class imbalance using SMOTE.

Compare models (Logistic Regression, Random Forest, XGBoost).

Automate churn prediction with a reusable Python script.

Generate business-ready outputs in Excel format.

🔹 Methodology
1. Data Preprocessing

Cleaned missing values & inconsistent entries.

Encoded categorical variables (label & one-hot encoding).

Scaled numerical features (StandardScaler).

Applied SMOTE to address churn imbalance (~26% churned).

2. Exploratory Data Analysis (EDA)

Univariate & bivariate analysis for feature insights.

Correlation checks for redundancy and interactions.

Distribution and churn driver analysis.

3. Model Development

Logistic Regression → Baseline model.

Random Forest → Ensemble learning with non-linear relationships.

XGBoost → High-performance gradient boosting.

Hyperparameter tuning with GridSearchCV.

4. Evaluation Metrics

Accuracy, Precision, Recall, F1-score.

ROC–AUC Curve for classification performance.

Cross-validation to ensure generalization.

5. Deployment Automation

Final XGBoost model saved as .pkl.

Python script (predict_using_pkl_file.py) automates predictions:

Accepts new customer data (CSV).

Processes data consistently.

Outputs churn predictions + probabilities to Excel.

🔹 Deliverables

Dataset: telco_customer_churn.csv

Model Training Notebook: Telco_Customer_Churn_Prediction.ipynb

Automated Prediction Script: predict_using_pkl_file.py

Churn Predictions: churn_predictions_output.xlsx

Project Report & Presentation Slides

Recorded Video Walkthrough

🔹 Business Impact

Proactive Retention: Identify high-risk customers early.

Optimized Marketing Spend: Focus retention campaigns on likely churners.

Improved Customer Experience: Tailored offers & service adjustments.

Revenue Growth: Even small churn reduction drives major profit gains.

🔹 Conclusion

This project demonstrates how predictive analytics can transform churn management from reactive to proactive. Among tested models, XGBoost delivered the strongest performance, and automation ensures seamless integration into business workflows.

📈 Future improvements could involve integrating real-time behavioral data and customer feedback to further enhance prediction accuracy.

🔹 References

Kaggle Dataset: Telco Customer Churn 

Key Research: Idris et al. (2012), Ahmad et al. (2019), Chen & Guestrin (2016)

Methodology: CRISP-DM Framework (IBM Analytics)
