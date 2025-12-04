import pickle
import numpy as np
import pandas as pd
import os
from sklearn.pipeline import Pipeline

with open("model/preprocessing.pkl", "rb") as f:
    preprocessing = pickle.load(f)

with open("model/model_pipe.pkl", "rb") as f:
    model = pickle.load(f)

pipeline = Pipeline([
    ("preprocess", preprocessing),
    ("model", model)
])    

def predict(emotion, year_min, year_max):
    input_df = pd.DataFrame([{
        "emotion": emotion,
        "year_min": year_min,
        "year_max": year_max
    }])

    return pipeline.predict(input_df)