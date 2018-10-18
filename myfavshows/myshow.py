from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,session
)
from werkzeug.exceptions import abort

from myfavshows.auth import login_required
from myfavshows.db import get_db
from myfavshows.backend import *

import requests

bp = Blueprint('myshow', __name__)

params = {'api_key': '7ecd6a3ceec1b96921b4647095047e8e'}


@bp.route('/myshow/<int:show_id>')
def get_my_show(show_id):

    result = [get_show_from_id(show_id)]
    return render_template('myshow/myshow.html', results=result)