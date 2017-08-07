from flask import jsonify, render_template, request, Response
from flask.ext.login import current_user, login_user

from functions import app
from models import User


@app.route('/community', methods=['GET'])
def community():
    
    recent_users = User.get_by_date()

    args = { 'recent_users': recent_users }

    return render_template("community.html", **args)

