import joblib
import numpy as np
import os

# Load trained model
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "crop_model.pkl")

model = joblib.load(MODEL_PATH)

def predict_crop_with_details(input_data):
    """
    Returns:
    - recommended crop
    - confidence score
    - top 3 alternatives
    """

    X = np.array(input_data).reshape(1, -1)

    # Probabilities for each class
    probabilities = model.predict_proba(X)[0]
    classes = model.classes_

    # Sort by probability (descending)
    sorted_indices = np.argsort(probabilities)[::-1]

    top_indices = sorted_indices[:3]

    recommended_crop = classes[top_indices[0]]
    confidence = float(probabilities[top_indices[0]])
    top_alternatives = [classes[i] for i in top_indices[1:]]

    # Suitability logic
    if confidence > 0.75:
        suitability = "High"
    elif confidence > 0.5:
        suitability = "Medium"
    else:
        suitability = "Low"

    return recommended_crop, confidence, top_alternatives, suitability
