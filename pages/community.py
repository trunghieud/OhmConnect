
from flask import render_template
from functions import app
from models import User


@app.route('/community', methods=['GET'])
def community():
    users = User.get_five_recent_users()
    phones = {}
    locations = {}
    for user in users:
        numbers = User.get_phone_numbers_by_user_id(user[0])
        if numbers.rowcount > 0:
            phones[user[0]] = numbers
        locs = User.get_location_by_user_id(user[0])
        if len(locs) > 0:
            locations[user[0]] = locs[0][0]
    args = {
        'users': users,
        'phones': phones,
        'locations': locations
    }
    return render_template("community.html", **args)