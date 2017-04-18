from flask import jsonify, render_template, request, Response

from functions import app
from models import User, db


@app.route('/community', methods=['GET'])
def community():
    result = db.engine.execute(
        '''SELECT
           user.user_id, tier, point_balance, display_name, attribute
           FROM user
           LEFT OUTER JOIN rel_user_multi
           ON user.user_id = rel_user_multi.user_id
           ORDER BY user.last_interaction_dttm DESC
           LIMIT 5'''
    )

    users = {}
    for row in result:
        # if the user with the given user_id exists,
        # add a new phone to his phones list
        if row[0] in users:
            users[row[0]]['phones'].append(row[4])
        else:
            users[row[0]] = {'tier': row[1],
                             'point_balance': row[2],
                             'display_name': row[3],
                             'phones': [row[4]]}

    args = {
        'users': users
    }
    return render_template("community.html", **args)

