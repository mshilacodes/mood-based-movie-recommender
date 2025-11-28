import pickle
import numpy as np
import os

def predict(data):

    model_path = os.path.join(os.path.dirname(__file__), "rf_classifier_model.pkl")
   
    #load model
    with open("model/rf_classifier_model.pkl", "rb") as f:
        clf=pickle.load(f)

    X = np.array(data, dtype=float)

    try:
        return clf.predict(X)
    except AttributeError:

        if hasattr(clf, 'named_steps'):
            final_estimator = clf.named_steps.get('classifier') or clf.named_steps.get('model')
            if final_estimator:
                return final_estimator.predict(X)
        raise

