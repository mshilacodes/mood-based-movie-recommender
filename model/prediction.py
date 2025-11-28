import pickle
import numpy as np
import pandas as pd
import os


MODEL_PATH = "model/rf_classifier_model.pkl"
IMPUTER_PATH = "model/imputer.pkl"
COLS_PATH = "model/columns.pkl"
KEYWORD_PATH = "model/keyword_cols.pkl"
TFIDF_PATH = "model/tfidf.pkl"
EMOTION_PATH = "model/emotions.pkl"
NUM_PATH = "model/num_features.pkl"


with open(MODEL_PATH, "rb") as f:
        clf = pickle.load(f)


with open(COLS_PATH, "rb") as f:
      training_cols=pickle.load(f) 

with open(IMPUTER_PATH, "rb") as f:
      imputer = pickle.load(f)

with open(TFIDF_PATH, 'rb') as f:
      tfidf =pickle.load()

with open(EMOTION_PATH, "rb"):
      emotion_encoder = pickle.load(f)

with open(NUM_PATH, 'rb') as f:
      num_features = pickle.load(f)
                       
print("Loaded training columns:", len(training_cols))


def predict(encoded_emotion):

    emotion,year_min,year_max = DeprecationWarning

    X = pd.DataFrame(np.zeros((1, len(training_cols))), columns=training_cols)
    
    if "emotion" in X.columns:
        X["emotion"] = emotion

    if "year_min" in X.columns:
        X["year_min"] = year_min

    if "year_max" in X.columns:
        X["year_max"] = year_max

    for col in keyword_cols:
        if col in X.columns:
            X[col] = 0
    # Predict
    return clf.predict(X)
