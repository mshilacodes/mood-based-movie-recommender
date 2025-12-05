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

st.set_page_config(page_title="Chillio Flicks", layout ="wide")
st.title('CHILLIO')
st.markdown("Queer movie recommender, matching movies to your mood!")


#Side bar

st.sidebar.header("🗃️ Filters")

content = pd.read_csv("model/content_cleaned.csv")

all_genres = sorted(list(set(",".join(content["genre_name"].dropna()).split(","))))

genre_filter = st.sidebar.multiselect("Filter by Genre: ", all_genres)
year_min, year_max = st.sidebar.slider(
    "Release Year Range",
    
    min_value = int(content["release_year"].min()),
    max_value = int(content["release_year"].max()),
    value=(2000,2023)
) 

#User input
emotion = st.selectbox("What mood are you in Kween: ",EMOTION_OPTIONS)



if st.button("You Better Werk"):
    results = recommend_movie(emotion)

    if "error" in results:
        st.error(results["error"])
    else:
        st.success(f"Your current vibe is: **{results['user_mood']}**")

        st.markdown("---")

        recs = results["recommendations"]
        recs_df = pd.DataFrame(recs)

        if genre_filter:
            recs_df= recs_df[
                recs_df["genre"].apply(lambda g: any(x in g for x in genre_filter))
            ]

        recs_df= recs_df[
            (recs_df["year"] >= year_min) &(recs_df["year"]<= year_max)
        ]   

        if recs_df.empty:
            st.warning("No movies match the selected filters")

        else:
            cols =st.columns(2)    

            for index, movie in recs_df.iterrows:
                col = cols[index % 2]

                with col:
                    st.subheader(movie["title"])
                    st.caption(f"{movie['genre']} • {movie['year']}")
                    
                    if movie["poster_url"]:
                        st.image(movie["poster_url"], use_column_width = True)
                    
                    st.write(movie["overview"])
                    st.markdown("---")