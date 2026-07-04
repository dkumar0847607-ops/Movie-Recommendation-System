import requests
from src.config import TMDB_API_KEY

BASE_URL = "https://api.themoviedb.org/3/movie/"
IMAGE_URL = "https://image.tmdb.org/t/p/w500"


def fetch_movie_details(movie_id):
    """
    Fetch complete movie details from TMDB.
    """

    url = f"{BASE_URL}{movie_id}?api_key={TMDB_API_KEY}"

    response = requests.get(url)

    return response.json()