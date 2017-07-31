from flask import jsonify, render_template, request, Response
from flask.ext.login import current_user, login_user
from functions import app
from models import User


@app.route('/community', methods=['GET'])
def community():

        results = User.get_recent_user_data(5)
        print(results)
	
        args = {
		'recent_users': results[0],
		'user_info': results[1],
		'phonenumbers': results[2],
                'location': results[3],
        }

        return render_template("community.html", **args)

