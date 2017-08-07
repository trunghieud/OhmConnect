"""migration to increase the point_balance for user 2 to 1000, and the tier for user 3 to Bronze

Revision ID: 2d81d6e44286
Revises: 00000000
Create Date: 2017-07-25 17:51:45.405519

"""

# revision identifiers, used by Alembic.
revision = '2d81d6e44286'
down_revision = '00000000'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute(
     '''UPDATE user
        SET point_balance = 1000
        WHERE user_id = 2
     '''
    )
    op.execute(
     '''UPDATE user
        SET tier = 'Bronze'
        WHERE user_id = 3
     '''
    )
    pass


def downgrade():
    op.execute(
     '''UPDATE user
        SET point_balance = 0
        WHERE user_id = 2
     '''
    )
    op.execute(
     '''UPDATE user
        SET tier = 'Carbon'
        WHERE user_id = 3
     '''
    )
    pass
