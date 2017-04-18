from flask import jsonify, render_template, request, Response
from flask.ext.login import current_user, login_user

from functions import app
from models import User, RelUserMulti, RelUser


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

    users = User.query.order_by(User.signup_date).limit(5).all()

    users_data = []
    for user in users:
        user_phones = RelUserMulti.query.filter_by(user_id = user.user_id).all()
        user_loc = RelUser.query.filter_by(user_id = user.user_id).first()
        data = {'name':user.display_name,
                'tier':user.tier,
                'point_balance':user.point_balance,
                'phones':[phone.attribute for phone in user_phones],
                'location':'Unknown'}
        if user_loc:
            data['location'] = user_loc.attribute
        users_data.append(data)
    args = {'users':users_data}
    return render_template("community.html", **args)

