from flask import Flask
from flask import render_template
from string_reader import parse_file

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/mazegen")
def mazegen():
    title1 = "my poopoo project"
    content1 = "my poopoo project poo"
    code1 = parse_file("mazegen.txt")
    return render_template('mazegen.html', title = title1, content = content1, code = code1)

@app.route("/snake")
def snake():
    title1 = "my peepee project"
    content1 = "my peepee project pee"
    code1 = parse_file("snake.txt")
    return render_template('mazegen.html', title = title1, content = content1, code = code1)

if __name__== '__main__':
    app.run()