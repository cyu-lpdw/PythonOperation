from jinja2 import Environment, FileSystemLoader

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<string:prenom>")
def hello_person(prenom):
    return render_template('name.html', prenom=prenom)

if __name__ == "__main__":
    app.run(debug=True)