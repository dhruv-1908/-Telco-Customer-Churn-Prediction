import pandas as pd
import pickle

# Load the trained XGBoost model
with open('xgboost_tuned_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the top 10 features
top_xgb_features = [
    'PaymentMethod_Electronic check',
    'InternetService_Fiber optic',
    'InternetService_No',
    'Contract_Two year',
    'Dependents',
    'Contract_One year',
    'PhoneService',
    'PaymentMethod_Credit card (automatic)',
    'tenure',
    'MultipleLines_Yes'
]

# Load your CSV data
df = pd.read_csv('telco_customer_churn.csv')

# Preprocess categorical "No internet service"/"No phone service"
replace_cols = ['MultipleLines', 'OnlineSecurity', 'OnlineBackup',
                'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
for col in replace_cols:
    df[col] = df[col].replace({'No internet service': 'No', 'No phone service': 'No'})

# Encode binary columns to 0/1
binary_cols = ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']
for col in binary_cols:
    df[col] = df[col].map({'Yes': 1, 'No': 0})

# One-hot encode categorical variables
df_encoded = pd.get_dummies(df)

# Ensure all top features exist
for feature in top_xgb_features:
    if feature not in df_encoded.columns:
        df_encoded[feature] = 0

# Subset features for prediction
X = df_encoded[top_xgb_features]

# Make predictions
df['Churn_Probability'] = model.predict_proba(X)[:, 1]
df['Churn_Prediction'] = (df['Churn_Probability'] >= 0.5).astype(int)

# Export to Excel
df.to_excel('churn_predictions.xlsx', index=False)

print("Excel file 'churn_predictions.xlsx' has been created with predictions.")