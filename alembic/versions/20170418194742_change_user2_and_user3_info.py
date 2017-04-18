"""change user2 and user3 info

Revision ID: 350ad0ecd18
Revises: 00000000
Create Date: 2017-04-18 19:47:42.674703

"""

# revision identifiers, used by Alembic.
revision = '350ad0ecd18'
down_revision = '00000000'

from alembic import op


def upgrade():
    op.execute('''UPDATE user SET point_balance = 1000.0 WHERE user_id = 2''')
    op.execute('''UPDATE user SET tier = 'Bronze' WHERE user_id = 3''')


def downgrade():
    pass
