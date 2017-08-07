"""update user2 points & user3 tier

Revision ID: 3b80bab07dec
Revises: 00000000
Create Date: 2017-06-27 11:24:45.964636

"""

# revision identifiers, used by Alembic.
revision = '3b80bab07dec'
down_revision = '00000000'

from alembic import op
from sqlalchemy.sql import table, column

def upgrade():
    users = table('user', column('user_id'), column('point_balance'), column('tier'))
    op.execute(users.update().where(users.c.user_id==op.inline_literal('2')).\
               values({'point_balance':op.inline_literal('1000')}))
    op.execute(users.update().where(users.c.user_id==op.inline_literal('3')).\
               values({'tier':op.inline_literal('Bronze')}))
    pass


def downgrade():
    users = table('user', column('user_id'), column('point_balance'), column('tier'))
    op.execute(users.update().where(users.c.user_id==op.inline_literal('2')).\
               values({'point_balance':op.inline_literal('0')}))    
    op.execute(users.update().where(users.c.user_id==op.inline_literal('3')).\
               values({'tier':op.inline_literal('Carbon')}))
    pass
