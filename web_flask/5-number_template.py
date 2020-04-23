#!/usr/bin/python3
# Script that starts a Flask web application.

from flask import Flask, render_template


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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_variable_text(text='is_cool'):
    """Python with some variable content."""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_variable_integers(n):
    """Number with some variable integers."""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_variable_integers(n):
    """number_template with some variable integers."""
    return render_template('5-number.html', number_template=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
