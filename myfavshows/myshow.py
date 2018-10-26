from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)

from myfavshows.backend import *
from myfavshows.classes import *

import requests

bp = Blueprint('myshow', __name__)


@bp.route('/myshow/<int:show_id>')
def get_my_show(show_id):
    if 'user_id' in session:
        shows_to_session()

    show = ShowDetailedView(show_id)

    return render_template('myshow/myshow.html', show=show)


@bp.route('/myshow/<show_title>/<int:show_id>/season/<int:season_number>')
def get_my_season(show_title, show_id, season_number):

    season = SeasonDetailedView(show_title, show_id, season_number)

    return render_template('myshow/myseason.html', season=season)
