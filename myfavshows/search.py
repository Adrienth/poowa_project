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
            return redirect(url_for('search.get_results', query=title, page=1))

    shows_to_session()
    if ('user_id' in session) and (len(session['show_ids']) > 0):
        last_show_id = session['show_ids'][-1]
        shows = get_shows_from_recommandation(last_show_id, 1)
        session['last_show_name'] = ShowDetailedView(last_show_id).title
        return render_template('search/search.html', shows=shows)
    else:
        # Get the list of today's trending shows with an API call
        shows = get_shows_from_trending_day(1)

    return render_template('search/search.html', shows=shows)


@bp.route('/results/<query>/<int:page>', methods=('GET', 'POST'))
def get_results(query, page):

    if request.method == 'POST':
        title = request.form['title']
        error = None

        if not title:
            error = 'A TV show name is required.'

        if error is not None:
            flash(error)
        else:
            return redirect(url_for('search.get_results', query=title, page=1))

    if 'user_id' in session:
        shows_to_session()

    if query is None:
        query = 'house'

    shows, total_pages, query = get_shows_from_search(query, page)

    return render_template('search/results.html', shows=shows, current_page=page, total_pages=total_pages, query=query)


@bp.route('/trending', methods=('GET',))
def get_trending():
    if 'user_id' in session:
        shows_to_session()

    # Get the list of today's trending shows with an API call
    shows = get_shows_from_trending_week(1)

    return render_template('search/trending.html', shows=shows)


@bp.route('/popular', methods=('GET',))
def get_popular():
    if 'user_id' in session:
        shows_to_session()

    # Get the list of today's trending shows with an API call
    shows = get_shows_from_popular(1)

    return render_template('search/popular.html', shows=shows)


@bp.route('/top_rated', methods=('GET',))
def get_top_rated():
    if 'user_id' in session:
        shows_to_session()

    # Get the list of today's trending shows with an API call
    shows = get_shows_from_top_rated(1)

    return render_template('search/top_rated.html', shows=shows)
