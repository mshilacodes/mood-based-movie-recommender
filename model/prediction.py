import pickle
import numpy as np
import pandas as pd
import os
from sklearn.pipeline import Pipeline


def predict(emotion, year_min, year_max):
    input_df = pd.DataFrame([{
        "emotion": emotion,
        "year_min": year_min,
        "year_max": year_max
    }])

    return Pipeline.predict(input_df)