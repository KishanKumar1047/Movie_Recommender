# 🎬 Movie Recommender System

A content-based movie recommender system built using **Streamlit**, **Pandas**, and **Scikit-learn**, deployed on **Render**. This app suggests top 5 similar movies based on the one you select from the dropdown.

---

## 🚀 Demo

🌐 [Live App on Render](https://your-render-app-url)  
📷 Screenshot:

![Movie Recommender Preview](https://via.placeholder.com/1200x600?text=Add+Screenshot+Here)

---

## 📦 Features

- 🔍 Search for a movie from the dropdown
- 📃 Get top 5 similar movie suggestions
- ⚡ Fast and simple UI using Streamlit
- 🎯 Purely name-based recommendations (no images)

---

## 🧠 How It Works

1. A similarity matrix is precomputed using **cosine similarity** on movie metadata (not shown in this repo).
2. A pickled dictionary `movie_dict.pkl` stores movie titles and their TMDB IDs.
3. On selecting a movie, the app retrieves top 5 similar movies using the similarity matrix.
4. (Optional) You can extend this app to fetch posters using TMDB API.

---

## 📁 Directory Structure

.
├── app.py # Main Streamlit application
├── movie_dict.pkl # Pickled dictionary with movie data
├── similarity.pkl # Pickled similarity matrix
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 📥 Installation (For Local Testing)

```bash
git clone https://github.com/your-username/movie-recommender-streamlit.git
cd movie-recommender-streamlit
pip install -r requirements.txt
streamlit run app.py

☁️ Deploying on Render
1. 📝 Create requirements.txt

    streamlit
    pandas==2.3.0
    numpy==2.3.1
    scikit-learn==1.7.0

2. ⚙️ Add render.yaml (optional but recommended)

    services:
    - type: web
        name: movie-recommender
        env: python
        buildCommand: pip install -r requirements.txt
        startCommand: streamlit run app.py --server.port=$PORT


3. 🚀 Deploy Steps
Push code to GitHub

Go to Render Dashboard

Click "New Web Service"

Connect your GitHub repo

Set the start command to:

    streamlit run app.py --server.port=$PORT
Deploy!