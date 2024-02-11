from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from flaskr.db import get_db


import datetime 
 

bp = Blueprint("sunday_ban", __name__, url_prefix="/sunday_ban")


@bp.route("/sunday", methods=("GET",))
def sunday_ban():
    today = datetime.date.today()
    time_diff = 6 - (today.weekday()) 
    sunday =  today + datetime.timedelta(time_diff)

    db = get_db()
    database = db.execute(
        f"""SELECT date
            FROM sundays 
            where 1=1 
                and date >= "{today}"
                and is_handlowa = 1 
            ORDER BY date"""
    ).fetchall()


    is_handlowa = "nie"
    is_handlowa_headed = "NIE"
    if len(database) > 0:
        print(database[0]['date'])
        if str(database[0]['date']) == str(sunday):
            is_handlowa = ''
            is_handlowa_headed = 'TAK'

    return render_template(
        "sunday_ban/sunday.html",
        today=today,
        sunday=sunday,
        time_diff=time_diff,
        is_handlowa=is_handlowa,
        is_handlowa_headed=is_handlowa_headed
        )
