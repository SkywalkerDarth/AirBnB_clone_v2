#!/usr/bin/python3
# -*- coding: utf-8 -*-
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

@app.route('/python/', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text='is_cool'):
    """inputed text, replace "_" with " " """
    return "Python {}".format(text.repace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n=None):
    """Dynamic inputted integer"""
    return "%d is a number" % n

@app.route('/number_template/<int:n>', strict_slashes=False)
def first_template(n=None):
    """Display HTML Page only if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

