import pickle
import numpy as np
import pandas as pd
import re
import os
from sklearn.pipeline import Pipeline
from textblob import TextBlob

with open("model/preprocessing.pkl", "rb") as f:
    preprocessing = pickle.load(f)

with open("model/rf_classifier_model.pkl", "rb") as f:
    model = pickle.load(f)

pipeline = Pipeline([
    ("preprocess", preprocessing),
    ("model", model)
])    

#Emotion lexicon 

emotion_words = {
    'uplifting': ['love', 'hope', 'acceptance', 'authenticity', 'release', 'pride', 'together', 'beautiful', 'freedom', 'romance', 'celebration'],
    'dark': ['loneliness', 'despair', 'death', 'loss', 'grief', 'tragedy', 'rage','dark', 'murder', 'crime', 'dangerous', 'addiction', 'AIDS', 'fear', 'violence'],
    'intense': ['drama', 'struggling', 'obsession', 'wild', 'psychosexual', 'hallucinatory', 'intense', 'battle', 'conflict', 'power',  'transgression'],
    'calm': ['gentle', 'quiet', 'serene', 'peace', 'slowly', 'tender', 'acceptance', 'warm', 'soft', 'comfort', 'stable']
}

#synthetic overview
synthetic_overviews = {
    0: "A gentle calm story about peace, warmth, and quiet moments of comfort.",
    1: "A dark tale filled with despair, danger, death, and deep emotional struggle.",
    2: "An intense, powerful, dramatic story full of conflict and wild emotional tension.",
    3: "An uplifting story about love, hope, pride, beautiful moments and freedom."
}

def compute_sentiment_features(text):
    polarity = TextBlob(text).sentiment.polarity
    subjectivity = TextBlob(text).sentiment.subjectivity
    return polarity, subjectivity


def compute_lexicon_counts(text):
    counts = {}

    for emotion, words in emotion_words.items():
        pattern = '|'.join(words)
        counts[f"{emotion}_words"] = len(re.findall(pattern, text, flags=re.IGNORECASE))
    return counts

def predict(mood, year_min, year_max):

    overview = synthetic_overviews[mood]

    polarity,subjectivity = compute_sentiment_features(overview)
    
    lex_counts = compute_lexicon_counts(overview)
    data = {
        "overview": overview,
        "popularity": 5,
        "release_year": int((year_min+year_max)/2),
        "genre_name": "Drama",
        "original_title": "User Request",
        "sentiment_polarity": polarity,
        "sentiment_subjectivity": subjectivity,
        **lex_counts


    }

    df = pd.DataFrame([data])
    

    return pipeline.predict(df)