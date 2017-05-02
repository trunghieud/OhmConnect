from flask import jsonify, render_template, request, Response
from flask.ext.login import current_user, login_user

from functions import app
from models import User


@app.route('/dashboard', methods=['GET'])
def dashboard():

    login_user(User.query.get(1))

    points_and_dollars = current_user.get_points_and_dollars()


    args = {
            'points': points_and_dollars['points'],
            'dollars': points_and_dollars['dollars'],
            'gift_card_eligible': True,

            'cashout_ok': True,
            'user_below_silver': current_user.is_below_tier('Silver'),
    }
    return render_template("dashboard.html", **args)




@app.route('/community', methods=['GET'])
def community():

    login_user(User.query.get(1))

    points_and_dollars = current_user.get_points_and_dollars()


    args = {
            'points': points_and_dollars['points'],
            'dollars': points_and_dollars['dollars'],
            'gift_card_eligible': True,

            'cashout_ok': True,
            'user_below_silver': current_user.is_below_tier('Silver'),
    }
    return render_template("community.html", **args)


