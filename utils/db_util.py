import json
import os
from utils.constant import *


def init_db():
    if (os.stat(DB_PATH).st_size == 0):
        set_db(DB_SCHEMA)


def add_note(id, title):
    db = get_db()
    db[id] = {
        TITLE: title,
        CONTENT: ""
    }
    return set_db(db)


def update_content(id, content):
    db = get_db()
    db[id][CONTENT]=content
    return set_db(db)


def get_content(id):
    db = get_db()
    return db[id][CONTENT]


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


def getID(id):
    try:
        return int(id)
    except:
        return False
