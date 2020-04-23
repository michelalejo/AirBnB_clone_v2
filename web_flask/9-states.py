#!/usr/bin/python3
# Script that starts a Flask web application.

from flask import Flask, render_template
from models import storage
from models.state import State
from operator import getitem


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """Display a HTML page with states_list."""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tear_down_app(db):
    """Method that remove the current SQLAlchemy Session."""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def list_cities():
    """Display a HTML page with cities_list."""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states', strict_slashes=False)
def states():
    """Display a HTML page with States."""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Display a HTML page states_id"""
    flag = 0
    states = None
    all_states = storage.all(State).values()
    for state in all_states:
        if id in state.id:
            flag = 1
            states = state
            break
    return render_template('9-states.html', states=states, flag=flag)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
