import pickle
import numpy as np

def predict(data):
    #load model
    with open("model/rf_classifier_model.pkl", "rb") as f:
        clf=pickle.load(f)

    with open("model/rf_classifier_model.pkl", "rb") as f:
        le=pickle.load(f)

    encoded = le.transform(data)
    encoded = np.array(encoded).reshape(-1,1)

    return clf.predict(encoded)