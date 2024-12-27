import pandas as pd
import streamlit as st
import pickle
import requests


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=6268e06a75995d5027462c06e5499df9&language=en-US'.format(movie_id))
    data = response.json()
    # just to check what is being printed
    # st.text(data)
    # st.text('https://api.themoviedb.org/3/movie/{}?api_key=%3C%3Capi_key%3E%3E&language=en-US'.format(movie_id))
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        # print(i[0]) just gives the index,we want title
        # movie_id = i[0] wrong actually see jupyter notebook
        movie_id = movies_df.iloc[i[0]].id
        # fetch poster for every movie_id using API (GET api from themoviedb api docs)
        # pass api key and movie id into it in the browser url
        recommended_movies.append(movies_df.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


new_movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))  # we have load the new_movies dataframe into movies list
movies_df = pd.DataFrame(new_movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title("Movie Recommender System")

selected_movie = st.selectbox(
    "Type a movie name or Select", movies_df['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)
    # for display, we'll use Lay out your app from st docs in api reference
    # for i in recommendations:
    #     st.write(i)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.header(names[0])
        st.image(posters[0])

    with col2:
        st.header(names[1])
        st.image(posters[1])

    with col3:
        st.header(names[2])
        st.image(posters[2])

    with col4:
        st.header(names[3])
        st.image(posters[3])

    with col5:
        st.header(names[4])
        st.image(posters[4])
