from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,session
)
from werkzeug.exceptions import abort

from myfavshows.auth import login_required
from myfavshows.db import get_db
from myfavshows.search import get_show, shows_to_session

import requests

bp = Blueprint('myfav', __name__)

params = {'api_key': '7ecd6a3ceec1b96921b4647095047e8e'}

@bp.route('/myfav')
@login_required
def get_my_fav():

    if g.user is not None:
        shows_to_session()

    results = []
    for show_id in session['show_ids']:
        req = requests.get('https://api.themoviedb.org/3/tv/' + str(show_id), params)
        results += [get_show(req.json())]

    return render_template('myfav/myfav.html', results=results)