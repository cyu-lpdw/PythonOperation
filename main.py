from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """
    Renders home page
    :return: Renders the 'index.html' template (home page)
    """
    return render_template('index.html')


@app.route("/<string:prenom>")
def hello_person(prenom):
    """
    Renders a personalized greetings page based on the provided name.
    :param prenom: The name of the person to greet.
    :return: Renders the 'name.html' template (greetings page)
    """
    return render_template('name.html', prenom=prenom)


if __name__ == "__main__":
    app.run(debug=True)