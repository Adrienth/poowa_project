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
        if len(session['show_ids']) > 0:
            last_show_id = session['show_ids'][-1]
            shows = get_shows_from_search(None, kind='recommendation', show_id=last_show_id)
            session['last_show_name'] = ShowDetailedView(last_show_id).title
            # print(session.get('test'))
            return render_template('search/search.html', shows=shows)
    else:
        # Get the list of today's trending shows with an API call
        shows = get_shows_from_search(None, kind='trending_day')

    return render_template('search/search.html', shows=shows)


@bp.route('/results/<query>', methods=('GET',))
def get_results(query):

    if 'user_id' in session:
        shows_to_session()

    if query is None:
        query = 'house'

    shows = get_shows_from_search(query)

    return render_template('search/results.html', shows=shows)


@bp.route('/trending', methods=('GET',))
def get_trending():
    if 'user_id' in session:
        shows_to_session()

    # Get the list of today's trending shows with an API call
    shows = get_shows_from_search(None, kind='trending_week')

    return render_template('search/trending.html', shows=shows)


@bp.route('/popular', methods=('GET',))
def get_popular():
    if 'user_id' in session:
        shows_to_session()

    # Get the list of today's trending shows with an API call
    shows = get_shows_from_search(None, kind='popular')

    return render_template('search/popular.html', shows=shows)


@bp.route('/top_rated', methods=('GET',))
def get_top_rated():
    if 'user_id' in session:
        shows_to_session()

    # Get the list of today's trending shows with an API call
    shows = get_shows_from_search(None, kind='top_rated')

    return render_template('search/top_rated.html', shows=shows)
