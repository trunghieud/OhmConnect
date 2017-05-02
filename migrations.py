from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root',password='root', database='ohm_assessment')
cursor = cnx.cursor()

tomorrow = datetime.now().date() + timedelta(days=1)


cursor.execute ("""
   UPDATE user
   SET point_balance=%s
   WHERE user_id=%s
""", (1000,2))


cursor.execute ("""
   UPDATE user
   SET tier=%s
   WHERE user_id=%s
""", ('Bronze',3))


# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()