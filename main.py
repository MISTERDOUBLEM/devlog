from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/other")
def other():
    return render_template('other.html')