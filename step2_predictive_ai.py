"""
Predictive AI Module for Process Mining
---------------------------------------
Transforms raw event logs into a feature matrix using process characteristics,
and trains a Random Forest classifier to predict high-risk (delayed) cases.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import warnings

# Suppress warnings for clean console output
warnings.filterwarnings('ignore')

def main():
    input_file = "bpi_2019_sample.csv"
    
    print("[INFO] Initializing Predictive AI Module...")
    
    try:
        # 1. Load the sampled data from Sprint 1
        print(f"[INFO] Loading processed dataset '{input_file}'...")
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"[ERROR] '{input_file}' not found. Please run Sprint 1 first.")
        return

    # 2. Data Preprocessing & Feature Engineering
    print("[INFO] Performing Feature Engineering (Translating logs for the ML model)...")
    
    # Convert timestamps to datetime objects
    df['time:timestamp'] = pd.to_datetime(df['time:timestamp'], utc=True)
    
    # Extract structural features: Count of each activity per case (Bag of Activities)
    # This creates a matrix where each row is an order, and columns are activity frequencies.
    feature_matrix = pd.crosstab(df['case:concept:name'], df['concept:name'])
    
    # Calculate Throughput Time (Lead Time) per case
    case_duration = df.groupby('case:concept:name')['time:timestamp'].agg(['min', 'max'])
    case_duration['duration_days'] = (case_duration['max'] - case_duration['min']).dt.total_seconds() / (24 * 3600)
    
    # Define Target Label: 1 if delayed (duration > median), 0 if normal
    median_duration = case_duration['duration_days'].median()
    print(f"[INFO] Median process duration calculated: {median_duration:.2f} days.")
    case_duration['is_delayed'] = (case_duration['duration_days'] > median_duration).astype(int)
    
    # Merge features and labels
    dataset = feature_matrix.join(case_duration[['is_delayed']])
    
    # 3. Machine Learning Setup
    print("[INFO] Splitting data into Training and Testing sets (80/20)...")
    X = dataset.drop('is_delayed', axis=1) # Features
    y = dataset['is_delayed']              # Target Label
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 4. Train the Random Forest Model
    print("[INFO] Training Random Forest Classifier...")
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=5)
    rf_model.fit(X_train, y_train)
    
    # 5. Model Evaluation
    print("[INFO] Evaluating model performance...")
    y_pred = rf_model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    print("="*50)
    print(f"[RESULT] Model Accuracy: {accuracy * 100:.2f}%")
    print("-" * 50)
    print("[RESULT] Classification Report:")
    print(classification_report(y_test, y_pred))
    print("="*50)

    # 6. Business Value Extraction: Feature Importance
    print("[INFO] Extracting Top 3 Root Causes for delays (Feature Importance)...")
    importances = pd.Series(rf_model.feature_importances_, index=X.columns)
    top_causes = importances.sort_values(ascending=False).head(3)
    
    for idx, (activity, score) in enumerate(top_causes.items(), 1):
        print(f"  {idx}. Activity '{activity}' (Impact Score: {score:.3f})")

    print("[SUCCESS] Sprint 2 Predictive Model Completed.")

if __name__ == "__main__":
    main()