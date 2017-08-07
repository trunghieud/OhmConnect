"""modify user data

Revision ID: 46c7a17f6f5a
Revises: 00000000
Create Date: 2017-06-19 16:31:05.398382

"""

# revision identifiers, used by Alembic.
revision = '46c7a17f6f5a'
down_revision = '00000000'

from alembic import op
import sqlalchemy as sa


def upgrade():
  op.execute('''UPDATE user
  	SET `point_balance` = 1000
  	WHERE user_id = 2
  ''')

  op.execute('''UPDATE user
  	SET `tier` = 'Bronze'
  	WHERE user_id = 3
  ''')


def downgrade():
    pass
