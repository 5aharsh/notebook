from flask import Flask, request, render_template, jsonify
import json
import os

from utils.constant import *
from utils import db_util

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    with open("./data/notebook.txt", "r") as f:
        content = f.read()
    return render_template('notebook.html', content=content)    

@app.route("/home", methods=['GET'])
def home():
    db = db_util.get_db()
    return render_template('index.html', notebook=db[NOTEBOOK], title=TITLE)

@app.route("/add", methods=['POST'])
def add():
    title = request.json[TITLE]
    if title.strip() and db_util.add_note(title):
        return jsonify({'status': 'success'})
    return jsonify({'status': 'failure'})

@app.route("/refresh", methods=['POST'])
def refresh():
    text = request.json["data"]
    try:
        with open("./data/notebook.txt", "w") as f:
            f.write(text)
        return jsonify({'status': 'success'})
    except:
        return jsonify({'status': 'failure'})


if __name__ == '__main__':
    db_util.init_db()
    app.run()