import streamlit as st
import pandas as pd
import pickle
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="NeuroTune 🎧", layout="centered")

st.title("🎵 NeuroTune - Song Recommendation Engine")
st.markdown("""
Welcome to **NeuroTune**, a content-based song recommendation system inspired by Spotify.  
Select a song below to get the **top 10 similar recommendations** based on audio features.
""")

@st.cache_data
def load_data():
    data_file = "spotify_millsongdata.csv"
    sim_file = "similarity.pkl"

    if not os.path.exists(data_file):
        st.error(f"❌ File not found: `{data_file}`.")
        st.stop()
    if not os.path.exists(sim_file):
        st.error(f"❌ File not found: `{sim_file}`.")
        st.stop()

    df = pd.read_csv(data_file)
    with open(sim_file, 'rb') as f:
        similarity = pickle.load(f)

    return df, similarity

df, similarity = load_data()

# ✅ Debug Check: Ensure similarity is valid
if isinstance(similarity, (int, float, list)):
    st.error("❌ similarity.pkl does not contain a valid similarity matrix.")
    st.stop()

# ✅ Recommendation Logic
def recommend(song_name):
    if song_name not in df['song'].values:
        return []

    index = df[df['song'] == song_name].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:11]
    recommended = [df.iloc[i[0]].song for i in distances]
    return recommended

song_list = df['song'].dropna().unique()
selected_song = st.selectbox("🔍 Choose a Song", song_list)

if st.button("🎶 Recommend Similar Songs"):
    recommendations = recommend(selected_song)
    if recommendations:
        st.success("Here are your recommended songs:")
        for idx, song in enumerate(recommendations, 1):
            st.markdown(f"{idx}. {song}")
    else:
        st.warning("Sorry, we couldn't find similar songs.")

st.markdown("---")
