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
        print(session['show_ids'])

    show = ShowDetailedView(show_id)

    return render_template('myshow/myshow.html', show=show)


@bp.route('/myshow/<int:show_id>/season/<int:season_number>')
def get_my_season(show_id, season_number):

    show = ShowDetailedView(show_id)

    season = Season(show_id, season_number)

    return render_template('myshow/myseason.html', season=season, show=show)