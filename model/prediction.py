import pickle
import numpy as np
import pandas as pd
import difflib
import random
import os
import requests

with open("model/preprocessing.pkl", "rb") as f:
    preprocessing = pickle.load(f)

with open("model/rf_classifier_model.pkl", "rb") as f:
    model = pickle.load(f)

content = pd.read_csv("model/content_cleaned.csv")

MODEL_EMOTIONS = ['uplifting', 'dark', 'calm', 'intense']

TMDB_API = "a75402a07cfe5aac6472933d86a99804"
#Emotion lexicon 

EMOTIONS = {
    'uplifting': ['love', 'hope', 'acceptance', 'authenticity', 'release', 'pride', 'together', 'beautiful', 'freedom', 'romance', 'celebration'],
    'dark': ['loneliness', 'despair', 'death', 'loss', 'grief', 'tragedy', 'rage','dark', 'murder', 'crime', 'dangerous', 'addiction', 'AIDS', 'fear', 'violence'],
    'intense': ['drama', 'struggling', 'obsession', 'wild', 'psychosexual', 'hallucinatory', 'intense', 'battle', 'conflict', 'power',  'transgression'],
    'calm': ['gentle', 'quiet', 'serene', 'peace', 'slowly', 'tender', 'acceptance', 'warm', 'soft', 'comfort', 'stable']
}

def poster(title):
    try:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API}&query={title}"
        response = requests.get(url).json()

        if response["results"]:
            poster_path = response["results"][0]["poster_path"]
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
    except:
        return None
    return None


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
            "title": row.get("original_title", "Unknown"),
            "genre": row.get("genre_name", "Unknown"),
            "overview": row.get("overview", "No description available."),
            "year": row.get("release_year", "Unknown"),
            "poster_url": poster(row.get("original_title", "")),
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

