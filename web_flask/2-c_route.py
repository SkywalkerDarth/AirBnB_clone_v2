#!/usr/bin/python3
"""
A script to start Flask Web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Starts basic Flash web application"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Add specific route /hbnb"""
    return 'HBNB'

@app.route('/c/<string:text>', strict_slashes=False)
def text(text=None):
    """Display c followed by the value of the text, replace "_" with " " """
    return "C {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

