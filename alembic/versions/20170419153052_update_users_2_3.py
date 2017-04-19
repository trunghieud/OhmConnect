"""update users 2 3

Revision ID: 64525cc458f
Revises: 00000000
Create Date: 2017-04-19 15:30:52.090095

"""

# revision identifiers, used by Alembic.
revision = '64525cc458f'
down_revision = '00000000'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute('''UPDATE user SET
        point_balance=user.point_balance+1000 WHERE user.user_id=2
    ''')

    op.execute('''UPDATE user SET tier='Bronze' WHERE user.user_id=3
    ''')


def downgrade():
    pass
