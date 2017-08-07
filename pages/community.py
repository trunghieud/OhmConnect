from flask import jsonify, render_template, request, Response, g
from flask.ext.login import current_user, login_user
from functions import app
from functions.connect_to import connectTo
from models import User
import mysql

user_dict={}

@app.route('/community', methods=['GET'])
def community():
    get_community_data()

    return render_template("community.html", user_dict=user_dict)

def get_community_data():
    conn = connectTo('access')
    cursor = conn.cursor()
    query = ('''SELECT user.user_id, user.display_name, user.tier,
                user.point_balance, rel_user_multi.attribute
                FROM user
                JOIN rel_user_multi on rel_user_multi.user_id = user.user_id
                ''')
    cursor.execute(query)

    for user_id in cursor:
        for (user_id, display_name, tier, point_balance, attribute) in cursor:
            user_id = str(user_id)
            if user_id not in user_dict:
                user_dict[user_id] = {}
            user_dict[user_id]['name'] = display_name
            user_dict[user_id]['tier'] = tier
            user_dict[user_id]['points'] = point_balance
            user_dict[user_id]['phone'] = attribute

    cursor.close()
    conn.close()
