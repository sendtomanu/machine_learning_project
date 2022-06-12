from flask import Flasks

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"