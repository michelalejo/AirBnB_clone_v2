#!/usr/bin/python3
# Script that starts a Flask web application.

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ Returns Dummy Text"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns Dummy Text"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_variable_text(text):
    """C with some variable content."""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
