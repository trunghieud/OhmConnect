"""Update users

Revision ID: 2bda5492762a
Revises: 00000000
Create Date: 2017-07-30 15:23:11.729000

"""

# revision identifiers, used by Alembic.
revision = '2bda5492762a'
down_revision = '00000000'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute('''UPDATE user
        SET point_balance=1000 
		WHERE user_id=2;
    ''')

    op.execute('''UPDATE user
        SET tier='Bronze'
		WHERE user_id=3;
    ''')

def downgrade():
    op.execute("UPDATE user SET point_balance=0 WHERE user_id =2")
    op.execute("UPDATE user SET tier_list='Bronze' WHERE user_id=3")