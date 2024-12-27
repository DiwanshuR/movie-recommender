# Movie Recommender System

This is a content-based movie recommendation system built using machine learning algorithms and Streamlit for the interactive front-end. 
The system recommends movies based on user input, providing a personalized movie discovery experience.

## Features
- **Movie Recommendations**: Recommends top 5 similar movies based on the user's selected movie.
- **Poster Display**: Displays movie posters alongside recommendations.
- **Interactive UI**: Built using Streamlit for a user-friendly interface.
- **Movie Data**: Uses data from the Movie Database (TMDb) API for fetching movie details and posters.

# Technologies Used
- **Python**: Core language for implementing machine learning and backend logic.
- **Streamlit**: Framework for building the web-based user interface.
- **Pandas**: For data manipulation and loading the movie dataset.
- **Scikit-learn**: Used for implementing the similarity model (content-based filtering).
- **TMDb API**: Fetches movie details and posters using movie IDs.

## Installation

To run the project locally, follow these steps:

1. Clone the repository:
   git clone https://github.com/your-username/movie-recommender.git
   cd movie-recommender
   
2. Set up a virtual environment
   python -m venv .venv

3. Install Dependencies
   pip install -r requirements.txt

4. Run the Streamlit app
    streamlit run app.py

## WORKFLOW
1.  The system takes the title of a movie as input from the user.
2.  It uses a pre-trained machine learning model (cosine similarity) to find similar movies from the dataset.
3.  The top 5 recommended movies are displayed along with their posters fetched from the TMDb API.

