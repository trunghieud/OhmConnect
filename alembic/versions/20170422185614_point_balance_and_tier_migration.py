"""point_balance_and_tier_migration

Revision ID: 438e154a736
Revises: 00000000
Create Date: 2017-04-22 18:56:14.942928

"""

# revision identifiers, used by Alembic.
revision = '438e154a736'
down_revision = '00000000'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute("""
        UPDATE user
        SET point_balance=1000
        WHERE user.user_id = 2
    """)


    op.execute("""
        UPDATE user
        SET tier='Bronze'
        WHERE user.user_id = 3
    """)

def downgrade():
    pass
