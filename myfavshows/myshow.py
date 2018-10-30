from flask import (
    Blueprint, render_template, session
)
from myfavshows.backend import *
from myfavshows.classes import *

bp = Blueprint('myshow', __name__)


@bp.route('/myshow/<int:show_id>')
def get_my_show(show_id):
    """
    Create an object show of the ShowDetailedView class with all the information about our show.
    :return: the myshow.html template with all the information about the show contained in the object show
    """
    if 'user_id' in session:
        shows_to_session()

    show = ShowDetailedView(show_id)

    return render_template('myshow/myshow.html', show=show)


@bp.route('/myshow/<show_title>/<int:show_id>/season/<int:season_number>')
def get_my_season(show_title, show_id, season_number):
    """
    Create an object season of the SeasonDetailedView class with all the information about our season.
    :return: the myseason.html template with all the information about the season contained in the object season
    """
    season = SeasonDetailedView(show_title, show_id, season_number)

    return render_template('myshow/myseason.html', season=season)


@bp.route('/myshow/<show_title>/<int:show_id>/season/<int:season_number>/episode/<int:episode_number>')
def get_my_episode(show_title, show_id, season_number, episode_number):
    """
    Create an object episode of the EpisodeDetailedView class with all the information about our episode.
    :return: the myepisode.html template with all the information about the episode contained in the object episode
    """
    episode = EpisodeDetailedView(show_title, show_id, season_number, episode_number)

    return render_template('myshow/myepisode.html', episode=episode)
