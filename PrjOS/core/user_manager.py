import json
from utils.file_handler import read_json, write_json
from config.settings import USERS_FILE

def register_user(username, password):
    users = read_json(USERS_FILE)
    if any(user["username"] == username for user in users):
        return False
    users.append({"username": username, "password": password})
    write_json(USERS_FILE, users)
    return True

def authenticate_user(username, password):
    users = read_json(USERS_FILE)
    return any(user["username"] == username and user["password"] == password for user in users)
