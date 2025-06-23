from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# 🔁 Recommendation logic
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []

    for i in distances[1:6]:  # Top 5 recommendations
        title = movies.iloc[i[0]]['title']
        recommended_movie_names.append(title)

    return recommended_movie_names

# 📦 Load pickled data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# 🏠 Home route
@app.route('/', methods=['GET', 'POST'])
def index():
    movie_list = movies['title'].values
    recommendations = []

    if request.method == 'POST':
        selected_movie = request.form['movie']
        recommendations = recommend(selected_movie)

    return render_template('index.html', movie_list=movie_list, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
