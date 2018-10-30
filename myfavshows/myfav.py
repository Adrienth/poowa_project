from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,session
)

from myfavshows.auth import login_required
from myfavshows.db import get_db
from myfavshows.backend import *
from myfavshows.classes import *

import requests

bp = Blueprint('myfav', __name__)

params = {'api_key': '7ecd6a3ceec1b96921b4647095047e8e'}


@bp.route('/myfav')
@login_required
def get_my_fav():
    """
    Gets the user's favourite shows' ids and queries the API in multithreading to get their information
    :return: the myfav.html templates with all the favourite shows
    """

    shows_to_session()

    shows = make_multi_requests(session['show_ids'])

    return render_template('myfav/myfav.html', shows=shows)


@bp.route('/addtofav/<int:show_id>/<name>')
@login_required
def add_to_fav(show_id, name):
    """
    Adds the given show_id to the users favourites in the database and redirects to the last page
    :param show_id: the show_id
    :param name: the name of the show
    :return: the last page
    """
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
    """
    Removes the given show_id from the users favourites in the database and redirects to the last page
    :param show_id: the show_id
    :param name: the name of the show
    :return: the last page
    """

    db = get_db()
    db.execute(
        'DELETE FROM shows_users WHERE show_id = ? and user_id = ?',
        (show_id, session['user_id'])
    )

    flash('\"%s\" has been successfully removed from your favourite TV Shows!' % name)
    db.commit()
    return redirect(request.referrer)
