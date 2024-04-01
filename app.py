import streamlit as st
import pickle
import pandas as pd
import requests
from ipykernel import kernelapp as app
# app.launch_new_instance
# https://saavn.me/search/songs?query={}&page=1&limit=2


def fetch_poster(music_title):
    response = requests.get(
        "https://saavn.me/search/songs?query=kun+faya+kun&page=1&limit=2".format(
            music_title
        )
    )
    data = response.json()
    return data["data"]["results"][0]["image"][2][
        "https://c.saavncdn.com/408/Rockstar-Hindi-2011-20221212023139-500x500.jpg"
    ]


def recommend(musics):
    music_index = music[music["title"] == musics].index[0]
    distances = similarity[music_index]
    music_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[
        1:6
    ]
    recommended_music = []
    recommended_music_poster = []
    for i in music_list:
        music_title = music.iloc[i[0]].title
        recommended_music.append(music.iloc[i[0]].title)
        recommended_music_poster.append(fetch_poster(music_title))
    return recommended_music, recommended_music_poster



music_dict = pickle.load(
    open(
        r"D:\music_recommender\drive-download-20240115T184029Z-001\ex.csv",
        "rb",
    )
)
music = pd.DataFrame(music_dict)
# "D:\music_recommender\drive-download-20240115T184029Z-001\similarities.pkl
similarity = pickle.load(
    open(
        r"D:\music_recommender\drive-download-20240115T184029Z-001\similarities.pkl",
        "rb",
    )
)
st.title("Music Recommendation System")

selected_music_name = st.selectbox("Select a music you like", music["title"].values)

if st.button("Recommend"):
    names, posters = recommend(selected_music_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
