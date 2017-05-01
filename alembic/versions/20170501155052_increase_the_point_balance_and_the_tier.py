"""increase the point_balance and the tier

Revision ID: 358602bdcda2
Revises: 00000000
Create Date: 2017-05-01 15:50:52.233289

"""

# revision identifiers, used by Alembic.
revision = '358602bdcda2'
down_revision = '00000000'

from alembic import op


def upgrade():
    op.execute('''UPDATE user
                  SET point_balance = 1000
                  WHERE user_id = 2
               ''')
    op.execute('''UPDATE user
                      SET tier = 'Bronze'
                      WHERE user_id = 3
                   ''')


def downgrade():
    pass
