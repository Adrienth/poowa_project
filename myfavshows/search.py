from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,session
)
from werkzeug.exceptions import abort

from myfavshows.auth import login_required
from myfavshows.db import get_db

import requests

bp = Blueprint('search', __name__)

params = {'api_key': '7ecd6a3ceec1b96921b4647095047e8e'}


def get_show(show_json):
    """
    Retrieves the information we need from the TMDB JSON API
    :param show_json:
    :return: dictionnary with more
    """

    result = {
        'title': show_json['name'],
        'date': show_json['first_air_date'],
        'popularity': show_json['popularity'],
        'vote_average': show_json['vote_average'],
        'trunc_overview': show_json['overview'],
        'overview': show_json['overview'],
        'id': show_json['id'],
        'poster_url': 'https://image.tmdb.org/t/p/w200' + show_json['poster_path']
    }
    # Truncates the overview text to fit our style need, 260 characters max
    nb_char = 270
    view = result['trunc_overview']
    if len(view) > nb_char:
        view = view[:nb_char] + '...'
    result['trunc_overview'] = view

    return result


def get_shows(req_json):

    results = []
    if req_json["total_results"] == 0:
        # print('no result corresponding')
        pass
    else:
        for res in req_json["results"]:
            results += [get_show(res)]
    return results


def shows_to_session():
    """
    Fetches the user's favourite shows' ids and stores it in the 'session' object, aborts if no user loged in
    :return: None
    """
    if not 'user_id' in session:
        return None

    shows = []
    show_ids = get_db().execute(
        'SELECT show_id'
        ' FROM shows_users '
        ' WHERE user_id = ?',
        (session.get('user_id'),)
    ).fetchall()

    for show in show_ids:
        shows += [show['show_id']]

    session['show_ids'] = shows
    return None


@bp.route('/', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        title = request.form['title']
        error = None

        if not title:
            error = 'A name is required.'

        if error is not None:
            flash(error)
        else:
            return redirect(url_for('search.get_results', query=title))

    if 'user_id' in session:
        shows_to_session()

    # Get the list of today's trending shows with an API call
    req = requests.get('https://api.themoviedb.org/3/trending/tv/day', params)
    results = get_shows(req.json())

    return render_template('search/search.html',results=results)


@bp.route('/results/<query>',methods=('GET',))
def get_results(query):

    if 'user_id' in session:
        shows_to_session()

    if query is None:
        query = 'house'

    params['query'] = query

    req = requests.get('https://api.themoviedb.org/3/search/tv',params)

    if not req.ok:
        # print('there was an error in the request : ', req.status_code)
        pass

    results = get_shows(req.json())

    return render_template('search/results.html', results=results)



@bp.route('/addtofav/<int:show_id>/<name>')
@login_required
def add_to_fav(show_id, name):

    db = get_db()
    db.execute(
        'INSERT INTO shows_users (show_id, user_id)'
        ' VALUES (?, ?)',
        (show_id, session['user_id'])
    )

    flash('\"%s\" has been successfully added to your favourite TV Shows!' % name)
    db.commit()
    return redirect(request.referrer)

@bp.route('/rmfromfav/<int:show_id>/<name>')
@login_required
def rm_from_fav(show_id, name):

    db = get_db()

    db.execute(
        'DELETE FROM shows_users WHERE show_id = ? and user_id = ?',
        (show_id, session['user_id'])
    )

    flash('\"%s\" has been successfully removed from your favourite TV Shows!' % name)
    db.commit()
    return redirect(request.referrer)


@bp.route('/myfav')
@login_required
def get_myfav():

    shows = []

    if 'user_id' in session:
        show_ids = get_db().execute(
            'SELECT show_id'
            ' FROM shows_users '
            ' WHERE user_id = ?',
            (session.get('user_id'),)
        ).fetchall()

        for show in show_ids:
            shows += [show['show_id']]

    results = []
    for show_id in shows:
        req = requests.get('https://api.themoviedb.org/3/tv/' + str(show_id), params)
        results += [get_show(req.json())]

    return render_template('search/myfav.html', results=results)
