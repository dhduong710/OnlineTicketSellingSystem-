import threading
from utils.file_handler import read_json, write_json
from config.settings import SEATS_FILE

lock = threading.Lock()

def book_seat(show_id, seat_id, username):
    with lock:
        data = read_json(SEATS_FILE)
        if show_id not in data:
            data[show_id] = {}
        if data[show_id].get(seat_id) is None:
            data[show_id][seat_id] = username
            write_json(SEATS_FILE, data)
            return True
        else:
            return False
