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

    shows_to_session()
    if ('user_id' in session) and (len(session['show_ids']) > 0):
        last_show_id = session['show_ids'][-1]
        shows, total_pages = get_shows_from_search(None, kind='recommendation', show_id=last_show_id)
        session['last_show_name'] = ShowDetailedView(last_show_id).title
        return render_template('search/search.html', shows=shows)

    # Get the list of today's trending shows with an API call
    shows, total_pages = get_shows_from_search(None, kind='trending_day')

    return render_template('search/search.html', shows=shows)


@bp.route('/results/<query>', defaults={'page': 1}, methods=('GET', 'POST'))
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
            return redirect(url_for('search.get_results', query=title))

    if 'user_id' in session:
        shows_to_session()

    if query is None:
        query = 'house'

    shows, total_pages = get_shows_from_search(query, page=page)

    return render_template('search/results.html', shows=shows, current_page=page, total_pages=total_pages, query=query)


@bp.route('/trending', defaults={'page': 1})
@bp.route('/trending/<int:page>', methods=('GET',))
def get_trending(page):
    if 'user_id' in session:
        shows_to_session()

    # Get the list of today's trending shows with an API call
    shows, total_pages = get_shows_from_search(None, kind='trending_week', page=page)

    return render_template('search/trending.html', shows=shows, current_page=page, total_pages=total_pages)


@bp.route('/popular', defaults={'page': 1})
@bp.route('/popular/<int:page>', methods=('GET',))
def get_popular(page):
    if 'user_id' in session:
        shows_to_session()

    # Get the list of today's trending shows with an API call
    shows, total_pages = get_shows_from_search(None, kind='popular', page=page)

    return render_template('search/popular.html', shows=shows, current_page=page, total_pages=total_pages)


@bp.route('/top_rated', defaults={'page': 1})
@bp.route('/top_rated/<int:page>', methods=('GET',))
def get_top_rated(page):
    if 'user_id' in session:
        shows_to_session()

    # Get the list of today's trending shows with an API call
    shows, total_pages = get_shows_from_search(None, kind='top_rated', page=page)

    return render_template('search/top_rated.html', shows=shows, current_page=page, total_pages=total_pages)
