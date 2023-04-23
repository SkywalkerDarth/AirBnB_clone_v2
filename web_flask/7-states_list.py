#!/usr/bin/bash
""" script that runs an app with Flask """
from flask import Flask, render_template
from models import storage
from.models.state import Start


app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """ Teardown session """
    storage.close()

@app.route('/states_list', strict_slashes=False)
def display_HTML():
    """ display display a HTML page: (inside the tag BODY) """
    states = storage.all(State)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
