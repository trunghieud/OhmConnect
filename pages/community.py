from flask import render_template
from flask.ext.login import login_user

from functions import app
from models.user import User


@app.route('/community', methods=['GET'])
def community():
    login_user(User.query.get(1))
    args = {
        "users": User.get_five_recent()
    }
    return render_template("community.html", **args)
