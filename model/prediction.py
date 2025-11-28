import pickle

def predict(data):
    clf=pickle.load("rf_classifier_model.pkl")
    return clf.predict(data)