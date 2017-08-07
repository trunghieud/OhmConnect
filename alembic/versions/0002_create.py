""" Initial rev of database -- this should always be the first alembic version

Revision ID: 0000002
Revises: 00000001
Create Date: 2014-10-28 14:14:45.896256

"""

# revision identifiers, used by Alembic.
revision = '00000002'
down_revision = '00000001'

from alembic import op


def upgrade():

    op.execute('''UPDATE user
        SET point_balance = 1000
        WHERE user_id = 2
        ''')
    op.execute('''UPDATE user
        SET tier = "Bronze"
        WHERE user_id = 3
        ''')


def downgrade():
    op.execute("TRUNCATE TABLE user")
    op.execute("TRUNCATE TABLE rel_user")
    op.execute("TRUNCATE TABLE rel_user_multi")
