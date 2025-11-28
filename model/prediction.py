import pickle
import numpy as np
import pandas as pd
import os

def predict(encoded_emotion):
    # Load the trained model
    with open("model/rf_classifier_model.pkl", "rb") as f:
        clf = pickle.load(f)

    # ---- RECREATE TRAINING INPUT STRUCTURE ----
    # Replace these with the exact column names used during training
    # (you can confirm them with the notebook: df.columns)
    feature_columns = [
        "mood",          # the emotion
        "year_min",      # year lower range
        "year_max"       # year upper range
    ]

    # Example: from Streamlit you must pass all inputs
    mood_value, year_min, year_max = encoded_emotion

    # Build the correct input structure
    X = pd.DataFrame([{
        "mood": mood_value,
        "year_min": year_min,
        "year_max": year_max
    }])

    # Predict
    return clf.predict(X)
