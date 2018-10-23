from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort


import requests
from myfavshows.db import get_db
from myfavshows.classes import *

params = {'api_key': '7ecd6a3ceec1b96921b4647095047e8e'}


def get_shows_from_search(query):
    """
    :param query:
    :return: a list of all the API request's results. Each result is a dictionary with the same
    items : 'title', 'date', 'popularity', 'vote_average', 'overview', 'id', 'poster_url'
    """

    if query is None:
        req = requests.get('https://api.themoviedb.org/3/trending/tv/day', params)
        # Get the list of today's trending shows with an API call
    else:
        params['query'] = query
        req = requests.get('https://api.themoviedb.org/3/search/tv', params)

    if not req.ok:
        # print('there was an error in the request : ', req.status_code)
        pass

    req_json = req.json()

    results = []
    if req_json["total_results"] == 0:
        # print('no result corresponding')
        pass
    else:
        for res in req_json["results"]:
            results += [Show(res)]
    return results


def shows_to_session():
    """
    Fetches the user's favourite shows' ids and stores it in the 'session' object, aborts if no user logged in
    """
    if not 'user_id' in session:
        return None

    shows = []
    show_ids = get_db().execute(
        'SELECT show_id'
        ' FROM shows_users '
        ' WHERE user_id = ?',
        (session['user_id'],)
    ).fetchall()

    for show in show_ids:
        shows += [show['show_id']]

    session['show_ids'] = shows
    return None
