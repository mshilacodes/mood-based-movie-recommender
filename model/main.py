import streamlit as st
import pandas as pd
import numpy as np
import os
from prediction import predict


st.title('CHILLIO')
st.markdown("Queer movie recommender, matching movies to your mood!")


emotion = st.selectbox("Mood",("Calm","Dark","Intense", "Uplifting"))
year = st.slider('Year Range', min_value=1950, max_value=2024, value=(1990,2024))


emotion_mapping = {
    "Calm": 0,
    "Dark": 1,
    "Intense": 2,
    "Uplifting": 3

}

encoded_emotion = emotion_mapping.get(emotion)

if encoded_emotion is None:
    st.error("Unknown emotion. Please select one emotion from list")

else:
    if st.button("Werk"):
        result = predict(np.array([[encoded_emotion]]))
        st.text(f"Recommended vibe: {result[0]}")

