""" Initial rev of database -- this should always be the first alembic version

Revision ID: 0000001
Revises: None
Create Date: 2017-08-02

"""

# revision identifiers, used by Alembic.
revision = '00000001'
down_revision = '00000000'

from alembic import op


def upgrade():
    op.execute('''UPDATE user SET point_balance = 1000 WHERE user_id = 2''')

    op.execute('''UPDATE user SET tier = 'Bronze' WHERE user_id = 3''')


def downgrade():
    op.execute('''UPDATE user SET point_balance = 0 WHERE user_id = 2''')

    op.execute('''UPDATE user SET tier = 'Carbon' WHERE user_id = 3''')
