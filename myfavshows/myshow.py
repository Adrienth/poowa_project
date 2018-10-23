from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort

from myfavshows.db import get_db
from myfavshows.backend import *
from myfavshows.classes import *


import requests

bp = Blueprint('myshow', __name__)


@bp.route('/myshow/<int:show_id>')
def get_my_show(show_id):
    if 'user_id' in session:
        shows_to_session()

    show = ShowDetailedView(show_id)
    seasons = []
    for season in show['seasons']:
        if season['poster_path']:
            season['poster_url'] = 'https://image.tmdb.org/t/p/w200' + season['poster_path']
        seasons.append(season)
    return render_template('myshow/myshow.html', show=show, seasons=seasons)


@bp.route('/myshow/<int:show_id>/season/<int:season_number>')
def get_my_season(show_id,season_number):

    season = get_season(show_id,season_number)

    if season['poster_path']:
        season['poster_url'] = 'https://image.tmdb.org/t/p/w200' + season['poster_path']

    episodes = []

    for episode in season['episodes'] :
        if episode['still_path']:
            episode['poster_url'] = 'https://image.tmdb.org/t/p/w200' + episode['still_path']
        episodes.append(episode)
    season['episode_count'] = len(episodes)

    return render_template('myshow/myseason.html', season=season, episodes=episodes)