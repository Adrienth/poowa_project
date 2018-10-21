from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort


import requests
from myfavshows.db import get_db

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
            results += [select_useful_items(res)]
    return results


def select_useful_items(res):
    """
    :param res: one of the dictionary included in the req_json object, which is a list of dictionaries
    :return: a dictionary selecting the useful items of the input and cleaning them
    """

    result = {
        'id': res['id'],
        'title': res['name'],
        'date': res['first_air_date'],
        'popularity': res['popularity'],
        'vote_average': res['vote_average'],
        'poster_path': res['poster_path'],
        'overview': res['overview']
        }

    result = clean_result(result)

    return result


def get_show_from_id(show_id):
    """
    :param show_id:
    :return: a dictionary (about the show searched) with the following items : 'title', 'date', 'popularity',
    'vote_average', 'overview', 'id', 'poster_url', 'number of seasons' ...
    """

    req = requests.get('https://api.themoviedb.org/3/tv/' + str(show_id), params)
    req_json = req.json()
    result = {
        'id': show_id,
        'title': req_json['name'],
        'date': req_json['first_air_date'],
        'popularity': req_json['popularity'],
        'vote_average': req_json['vote_average'],
        'poster_path': req_json['poster_path'],
        'overview': req_json['overview'],
        'number_of_seasons': req_json['number_of_seasons'],
        'number_of_episodes': req_json['number_of_episodes'],
        'seasons': req_json['seasons'],
        'next_episode_to_air': req_json['next_episode_to_air']
        }

    result = clean_result(result)

    return result


def clean_result(result):
    """
    Cleans the dictionnary of a tv show by adapting it to our needs like clean poster URL and truncated overview field
    :param result: the dictionnary representing a tv show
    :return: result the same cleaned dictionnary
    """
    # Check if there is poster path before creating the URL
    if result['poster_path'] is None:
        result['poster_url'] = None
    else:
        result['poster_url'] = 'https://image.tmdb.org/t/p/w200' + result['poster_path']

    # Truncates the overview text to fit our style need, 260 characters max
    nb_char = 270
    view = result['overview']
    if len(view) > nb_char:
        view = view[:nb_char] + '...'
    result['trunc_overview'] = view

    return result


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
