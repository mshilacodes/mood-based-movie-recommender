import streamlit as st
import pandas as pd
import numpy as np
import os
from prediction import recommend_movie

EMOTION_OPTIONS = [
    "uplifting",
    "dark",
    "calm",
    "intense"
]

st.set_page_config(page_title="Chillio Flicks", layout ="centered")
st.title('CHILLIO')
st.markdown("Queer movie recommender, matching movies to your mood!")

#User input
emotion = st.selectbox("What mood are you in Kween: ",EMOTION_OPTIONS)



if st.button("You Better Werk"):
    results = recommend_movie(emotion)

    if "error" in results:
        st.error(results["error"])
    else:
        st.success(f"Your current vibe is: **{results['mapped_emotions']}**")

        st.markdown("---")

        for movie in results["recommendations"]:
            st.subheader(movie["title"])
            st.caption(movie["genre"])
            st.write(movie["overview"])
            st.markdown("---")