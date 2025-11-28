import pickle
import numpy as np
import pandas as pd
import os

MODEL_PATH = "model/rf_classifier_model.pkl"
COLS_PATH = "model/columns.pkl"
KEYWORD_PATH = "model/keyword_cols.pkl"



def predict(data):
    with open(MODEL_PATH, "rb") as f:
        clf = pickle.load(f)

    with open(COLS_PATH, "rb") as f:
        training_cols = pickle.load(f)

    with open(KEYWORD_PATH, "rb") as f:
        keyword_cols = pickle.load(f)


    X = pd.DataFrame(np.zeros((1,len(training_cols))), columns=training_cols)

    if "emotion" in X.columns:
        X.loc[0, "emotion"] = emotion_code
    else:
        raise ValueError("Column 'emotion' was not in training data.")

    return clf.predict(X)[0]