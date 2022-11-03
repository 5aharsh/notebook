from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    with open("./data/notebook.txt", "r") as f:
        content = f.read()
    return render_template('notebook.html', content=content)    

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
    app.run()