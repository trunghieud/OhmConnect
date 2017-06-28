from flask import jsonify, render_template, request, Response
from flask.ext.login import current_user, login_user

from functions import app
from models import User
from models._helpers import *

@app.route('/community', methods=['GET'])
def community():
    login_user(User.query.get(1))
    
    headers = "tier, point_balance, display_name, attribute"
    
    # This query should select only the 5 most recent users from the left table, and only
    # attributes from the right table designated as "phone".
    table = db.engine.execute("SELECT %s FROM (SELECT * FROM user ORDER BY signup_date DESC LIMIT 5) AS user \
	                       LEFT JOIN (SELECT * FROM rel_user_multi WHERE rel_lookup=\"PHONE\") AS rel_user_multi \
			       ON user.user_id = rel_user_multi.user_id" %headers)
    
    headers_formatted_dict = {"tier": "Tier", "point_balance": "Point Balance", "display_name": "Display Name", 
	                      "attribute": "Phone Number"}
    headers_formatted = [headers_formatted_dict[h] for h in headers.split(", ")]
    return render_template("community.html", table=table, headers=headers_formatted)
