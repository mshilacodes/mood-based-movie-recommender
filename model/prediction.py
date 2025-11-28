import pickle
import numpy as np
import os

def predict(data):

    model_path = os.path.join(os.path.dirname(__file__), "rf_classifier_model.pkl")
    #load model
    with open("model/rf_classifier_model.pkl", "rb") as f:
        clf=pickle.load(f)

    X = np.array(data, dtype=float)

    return clf.predict(X)