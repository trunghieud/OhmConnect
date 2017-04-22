from flask import jsonify, render_template, request, Response
from flask.ext.login import current_user, login_user

from functions import app
from models import User


@app.route('/community', methods=['GET'])
def community():
    login_user(User.query.get(1))
    args = {'users': User.get_recent(5)}
    return render_template("community.html", **args)
