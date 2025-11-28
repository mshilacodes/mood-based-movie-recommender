import streamlit as st
import pandas as pd
import numpy as np
import os
from prediction import predict


st.title('CHILLIO')
st.markdown("Queer movie recommender, matching movies to your mood!")

emotion = st.selectbox("Mood",("Dark","Uplifitng","Calm","Intense"))
year = st.slider('Year Range', min_value=1950, max_value=2024, value=(1990,2024))

if st.button("Werk"):
    result = predict(pd.DataFrame({'emotion': [emote]}))
    st.text(result[0])

