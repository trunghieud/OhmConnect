"""increase_point_user_2

Revision ID: 2c83a3f957ff
Revises: 00000000
Create Date: 2017-04-18 20:48:10.550208

"""

# revision identifiers, used by Alembic.
revision = '2c83a3f957ff'
down_revision = '00000000'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute('''UPDATE user
        SET point_balance = 100
        WHERE username = 'tester2'
    ''')

    op.execute('''UPDATE user
        SET tier = 'Bronze'
        WHERE username = 'tester3'
    ''')

def downgrade():
    op.execute('''UPDATE user
        SET point_balance = 0
        WHERE username = 'tester2'
    ''')

    op.execute('''UPDATE user
        SET tier = 'Carbon'
        WHERE username = 'tester3'
    ''')
