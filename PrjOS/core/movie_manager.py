from utils.file_handler import read_json
from config.settings import MOVIES_FILE, SHOWTIMES_FILE

def get_movies():
    return read_json(MOVIES_FILE)

def get_showtimes(movie_id):
    showtimes = read_json(SHOWTIMES_FILE)
    return showtimes.get(movie_id, [])
