import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os

def load_data(path='data/raw/heart.csv'):
    df = pd.read_csv(path)
    print(f"✅ Data loaded: {df.shape}")
    return df

def preprocess(df):
    # Duplicates remove karo
    df = df.drop_duplicates()
    print(f"✅ Duplicates removed. Shape: {df.shape}")

    # Features aur Target alag karo
    X = df.drop('target', axis=1)
    y = df['target']

    # Train/Test Split — 80/20
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )
    print(f"✅ Train size: {X_train.shape}, Test size: {X_test.shape}")

    # Scaling — SVM ke liye zaroori hai
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled  = scaler.transform(X_test)

    # Scaler save karo — webapp mein kaam aayega
    os.makedirs('models', exist_ok=True)
    joblib.dump(scaler, 'models/scaler.pkl')
    print("✅ Scaler saved: models/scaler.pkl")

    return X_train_scaled, X_test_scaled, y_train, y_test, X.columns.tolist()