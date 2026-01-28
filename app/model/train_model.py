import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os


# Get absolute path of current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build dataset path safely
DATA_PATH = os.path.join(BASE_DIR, "..", "..", "dataset", "Crop_recommendation.csv")

# Load dataset
data = pd.read_csv(DATA_PATH)

# Features and target
X = data.drop("Crop", axis=1)
y = data["Crop"]


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save model in same folder
MODEL_PATH = os.path.join(BASE_DIR, "crop_model.pkl")
joblib.dump(model, MODEL_PATH)

print("Model saved at:", MODEL_PATH)
