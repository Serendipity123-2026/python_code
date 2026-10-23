# session.py
import os
import json
from config import SESSION_LOCATION


def ensure_session_dir():
    if not os.path.exists(SESSION_LOCATION):
        os.makedirs(SESSION_LOCATION)


def load_session():
    sessions = []
    ensure_session_dir()
    for filename in os.listdir(SESSION_LOCATION):
        if filename.endswith(".json"):
            sessions.append(filename[:-5])
    return sorted(sessions, reverse=True)


def load_session_messages(session_name):
    file_path = os.path.join(SESSION_LOCATION, f"{session_name}.json")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_session(session_name, messages=None):
    ensure_session_dir()
    if messages is None:
        messages = []
    file_path = os.path.join(SESSION_LOCATION, f"{session_name}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)


def delete_session(session_name):
    file_path = os.path.join(SESSION_LOCATION, f"{session_name}.json")
    if os.path.exists(file_path):
        os.remove(file_path)
