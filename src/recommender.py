import pickle

# Load saved files
movies = pickle.load(open("models/movies.pkl", "rb"))
similarity = pickle.load(open("models/similarity.pkl", "rb"))


def search_movie(movie_name):
    """
    Search movie names using partial and case-insensitive matching.
    """

    return movies[movies["title"].str.contains(movie_name, case=False, na=False)]


def recommend(movie_name):
    """
    Returns the top 5 recommended movies.
    """

    movie_index = movies[movies["title"] == movie_name].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:21]

    recommended_movies = []

    for movie in movies_list:

        recommended_movies.append(
            {
                "movie_id": movies.iloc[movie[0]].movie_id,
                "title": movies.iloc[movie[0]].title
            }
        )

    return recommended_movies