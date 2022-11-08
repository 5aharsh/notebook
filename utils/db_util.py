import json
import os
from utils.constant import *


def init_db():
    if (os.stat(DB_PATH).st_size == 0):
        set_db(DB_SCHEMA)


def add_note(notebook_id, title):
    db = get_db()
    db[notebook_id] = {
        TITLE: title,
        CONTENT: ""
    }
    return set_db(db)


def delete_note(notebook_id):
    db = get_db()
    db.pop(notebook_id, None)
    return set_db(db)


def update_content(notebook_id, title, content):
    db = get_db()
    db[notebook_id][TITLE]=title
    db[notebook_id][CONTENT]=content
    return set_db(db)


def get_content(notebook_id):
    db = get_db()
    return db[notebook_id][TITLE], db[notebook_id][CONTENT]


def get_db():
    with open(DB_PATH, "r") as f:
        db = json.load(f)
    return db


def set_db(db):
    try:
        with open(DB_PATH, "w") as f:
            json.dump(db, f, indent=2)
        return True
    except:
        return False


def getID(notebook_id):
    try:
        return int(notebook_id)
    except:
        return False
