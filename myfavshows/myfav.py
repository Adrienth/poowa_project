from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,session
)
from werkzeug.exceptions import abort

from myfavshows.auth import login_required
from myfavshows.db import get_db
from myfavshows.backend import *

import requests

bp = Blueprint('myfav', __name__)

params = {'api_key': '7ecd6a3ceec1b96921b4647095047e8e'}

@bp.route('/myfav')
@login_required
def get_my_fav():

    if session['user_id'] is not None:
        shows_to_session()

    results = []
    for show_id in session['show_ids']:
        results += [get_show_from_id(show_id)]

    return render_template('myfav/myfav.html', results=results)
