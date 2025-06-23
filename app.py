import pickle
import pandas as pd
import streamlit as st
# import requests  # ❌ No need for requests now

# # 🔍 Fetch poster from TMDB API safely
# def fetch_poster(movies_id):
#     try:
#         url = f"https://api.themoviedb.org/3/movie/{movies_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
#         response = requests.get(url)
# 
#         if response.status_code != 200:
#             st.warning(f"TMDb API error: {response.status_code} for movies_id {movies_id}")
#             return "https://via.placeholder.com/500x750?text=Poster+Unavailable"
# 
#         data = response.json()
#         poster_path = data.get('poster_path')
# 
#         if poster_path:
#             return "https://image.tmdb.org/t/p/w500/" + poster_path
#         else:
#             return "https://via.placeholder.com/500x750?text=No+Poster"
# 
#     except Exception as e:
#         st.error(f"Failed to fetch poster: {e}")
#         return "https://via.placeholder.com/500x750?text=Error"

# 🔁 Recommendation logic
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []

    for i in distances[1:6]:  # Top 5 recommendations
        title = movies.iloc[i[0]]['title']
        recommended_movie_names.append(title)

    return recommended_movie_names

# 🌟 Streamlit UI setup
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title('🎬 Movie Recommender System')

# 📦 Load pickled data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# 🎯 Dropdown to select a movie
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

# 🎁 Show Recommendations
if st.button('Show Recommendation'):
    names = recommend(selected_movie)
    st.subheader("Top 5 Recommended Movies:")
    for name in names:
        st.write(f"👉 {name}")
