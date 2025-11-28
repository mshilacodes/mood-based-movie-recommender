import pickle
import numpy as np
import pandas as pd
import os

MODEL_PATH = "model/rf_classifier_model.pkl"
IMPUTER_PATH = "model/imputer.pkl"
COLS_PATH = "model/columns.pkl"
KEYWORD_PATH = "model/keyword_cols.pkl"


with open(MODEL_PATH, "rb") as f:
    clf = pickle.load(f)

with open(IMPUTER_PATH, "rb") as f:
    imputer = pickle.load(f)

with open(COLS_PATH, "rb") as f:
    training_cols = pickle.load(f)

with open(KEYWORD_PATH, "rb") as f:
    keyword_cols = pickle.load(f)





def predict(data):

    encoded_emotion = int(data[0][0])

    df = pd.DataFrame([{

        "emotions": encoded_emotion
    }])

    df = df.reindex(columns=training_cols, fill_value=0)

    for col in keyword_cols:
        if col in df.columns:
            df[col] = df[col]*10
    
    df_imputed = imputer.transform(df)

    prediction = clf.predict(df_imputed)


    return prediction