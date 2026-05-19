from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os

def train_random_forest(X_train, y_train):
    print("\n🌲 Random Forest Training...")
    rf = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )
    rf.fit(X_train, y_train)
    joblib.dump(rf, 'models/random_forest.pkl')
    print("✅ Random Forest saved: models/random_forest.pkl")
    return rf

def train_svm(X_train, y_train):
    print("\n🤖 SVM Training...")
    svm = SVC(
        kernel='rbf',
        C=1.0,
        gamma='scale',
        probability=True,
        random_state=42
    )
    svm.fit(X_train, y_train)
    joblib.dump(svm, 'models/svm_model.pkl')
    print("✅ SVM saved: models/svm_model.pkl")
    return svm

def evaluate_model(model, X_test, y_test, model_name):
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print(f"\n{'='*50}")
    print(f"📊 {model_name} Results")
    print(f"{'='*50}")
    print(f"Accuracy : {acc*100:.2f}%")
    print(f"\nClassification Report:")
    print(classification_report(y_test, y_pred,
          target_names=['No Disease', 'Disease']))

    return acc, y_pred