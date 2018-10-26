from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)

from myfavshows.backend import *
from myfavshows.classes import *

bp = Blueprint('search', __name__)


@bp.route('/', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        title = request.form['title']
        error = None

        if not title:
            error = 'A TV show name is required.'

        if error is not None:
            flash(error)
        else:
            return redirect(url_for('search.get_results', query=title))

    if 'user_id' in session:
        shows_to_session()

    # Get the list of today's trending shows with an API call
    shows = get_shows_from_search(None)

    return render_template('search/search.html', shows=shows)


@bp.route('/results/<query>', methods=('GET', 'POST'))
def get_results(query):

    if request.method == 'POST':
        title = request.form['title']
        error = None

        if not title:
            error = 'A TV show name is required.'

        if error is not None:
            flash(error)
        else:
            return redirect(url_for('search.get_results', query=title))

    if 'user_id' in session:
        shows_to_session()

    if query is None:
        query = 'house'

    shows = get_shows_from_search(query)

    return render_template('search/results.html', shows=shows)








