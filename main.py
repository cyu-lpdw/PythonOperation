from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/<string:prenom>")
def hello_person(prenom):
    return render_template('name.html', prenom=prenom)

if __name__ == "__main__":
    app.run(debug=True)