import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USERS_FILE = os.path.join(BASE_DIR, 'data', 'users.json')
MOVIES_FILE = os.path.join(BASE_DIR, 'data', 'movies.json')
SHOWTIMES_FILE = os.path.join(BASE_DIR, 'data', 'showtimes.json')
SEATS_FILE = os.path.join(BASE_DIR, 'data', 'seats.json')
