from flask import Flask, request, render_template, jsonify

from utils.constant import *
from utils import db_util

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    db = db_util.get_db()
    return render_template('index.html', notebook=db, title=TITLE)


@app.route("/notebook/<notebook_id>", methods=['GET'])
def notebook(notebook_id):
    title, content = db_util.get_content(notebook_id)
    return render_template('notebook.html', title=title, content=content, id=notebook_id)


@app.route("/add", methods=['POST'])
def add():
    notebook_id = db_util.getID(request.json[ID])
    title = request.json[TITLE]
    if notebook_id and title.strip() and db_util.add_note(notebook_id, title):
        return jsonify({'status': 'success'})
    return jsonify({'status': 'failure'})


@app.route("/refresh", methods=['POST'])
def refresh():
    try:
        text = request.json["data"]
        notebook_id = request.json["id"]
        db_util.update_content(notebook_id, text)
        return jsonify({'status': 'success'})
    except:
        return jsonify({'status': 'failure'})


if __name__ == '__main__':
    db_util.init_db()
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')