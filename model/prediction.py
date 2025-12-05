import pickle
import numpy as np
import pandas as pd
import difflib
import random
import os


with open("model/preprocessing.pkl", "rb") as f:
    preprocessing = pickle.load(f)

with open("model/rf_classifier_model.pkl", "rb") as f:
    model = pickle.load(f)

content = pd.read_csv("\\content_cleaned.csv")

MODEL_EMOTIONS = ['uplifting', 'dark', 'calm', 'intense']

#Emotion lexicon 

EMOTIONS = {
    'uplifting': ['love', 'hope', 'acceptance', 'authenticity', 'release', 'pride', 'together', 'beautiful', 'freedom', 'romance', 'celebration'],
    'dark': ['loneliness', 'despair', 'death', 'loss', 'grief', 'tragedy', 'rage','dark', 'murder', 'crime', 'dangerous', 'addiction', 'AIDS', 'fear', 'violence'],
    'intense': ['drama', 'struggling', 'obsession', 'wild', 'psychosexual', 'hallucinatory', 'intense', 'battle', 'conflict', 'power',  'transgression'],
    'calm': ['gentle', 'quiet', 'serene', 'peace', 'slowly', 'tender', 'acceptance', 'warm', 'soft', 'comfort', 'stable']
}


def recommend_movie(mood:str, n_recs: int = 5):
    
    matches = content[content['emotions']== mood]

    if matches.empty:
        return{
            "error" : f"No movies found that match mood category'{mood}'."
        }
    
    n_recs = min(n_recs, len(matches))

    selected = matches.sample(n_recs)

    recommendations = []

    for _, row in selected.iterrows():
        recommendations.append({
            "title": row.get("title", "Unknown"),
            "genre": row.get("genre_name", "Unknown"),
            "overview": row.get("overview", "No description available.")

        })
    return{
        "user_mood": mood,
        "recommendations": recommendations
    }

if __name__ == "__main__":
    user_input = input("Enter your mood:  ")
    results = recommend_movie(user_input)

    print("\nRecommended Movies: ")
    for idx, movie in enumerate(results.get("recommendations",[]),start=1):
        print(f"\n{idx}.  {movie['title']} ({movie['genre']})")
        print(f"  {movie['overview']}")

