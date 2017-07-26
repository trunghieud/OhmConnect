from flask import jsonify, render_template, request, Response
from flask.ext.login import current_user, login_user

from functions import app
from models import User
from models import RelUserMulti
from models import RelUser
from models._helpers import *


@app.route('/community', methods=['GET'])
def community():
    login_user(User.query.get(1))
    args = {
        'users': db.engine.execute('''
                            SELECT DISTINCT user.user_id, user.display_name, user.tier, user.point_balance, GROUP_CONCAT(rel_user_multi.attribute) AS phone_numbers, ANY_VALUE(rel_user.attribute) AS location, user.create_time
                            FROM user
                            LEFT JOIN rel_user_multi ON user.user_id = rel_user_multi.user_id
                            LEFT JOIN rel_user ON user.user_id = rel_user.user_id
                            GROUP BY user.user_id
                            ORDER BY user.create_time DESC
                            LIMIT 5
                            '''
        )
    }
    return render_template("community.html", **args)
