from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<string:prenom>")
def hello_person(prenom):
    return f"<p>Hello, {prenom}!</p>"

def main():
    app.run()

if __name__ == '__main__':
    main()