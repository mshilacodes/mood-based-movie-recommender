import pickle

def predict(data):
    with open("rf_classifier_model.pkl", "rb") as f:
        clf=pickle.load(f)
    return clf.predict(data)