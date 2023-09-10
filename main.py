# Importing required modules from the Flask library
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route("/")
def home():
    """
    Render the home page.
    
    Returns:
        render_template: Renders the 'index.html' template.
    """
    return render_template('index.html')

# Define the route for greeting a person by their first name
@app.route("/<string:prenom>")
def hello_person(prenom):
    """
    Render a personalized greeting page based on the provided first name.
    
    Parameters:
        prenom (str): The first name of the person to greet.
        
    Returns:
        render_template: Renders the 'name.html' template, passing in the first name.
    """
    return render_template('name.html', prenom=prenom)

# Run the Flask application
if __name__ == "__main__":
    """
    Entry point for the Flask application.
    The application will run in debug mode.
    """
    app.run(debug=True)
