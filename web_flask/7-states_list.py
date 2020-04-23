#!/usr/bin/python3
# Script that starts a Flask web application.

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with states_list."""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tear_down_app(self):
    """Method that remove the current SQLAlchemy Session."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
