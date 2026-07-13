# app.py
from flask import Flask, render templates

# Create an instance of the Flask class.
# '__name__' is a special variable that tells Flask where to look for resources.
app = Flask(__name__)

# Decorator: Maps the URL '/' to the function below.
@app.route('/')
@app.route("/student/<name>")
def student(name="Guest"):
    return f"Welcome {name}"

# Route to about
@app.route('/about')

def about():
    return '<h1> Welcome to  </h2>'

# Dynamic Routing
@app.route('/contact/<name>')

def contact(name):
    return f'Welcome to {name}'


#

# To Ensure your server runs only if this script is executed directly

if __name__ == '__main__':
    app.run(debug=True)


