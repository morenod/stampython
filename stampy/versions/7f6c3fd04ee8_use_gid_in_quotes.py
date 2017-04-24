"""Use gid in quotes

Revision ID: 7f6c3fd04ee8
Revises: d87d296fb8a9
Create Date: 2017-04-24 23:11:52.859910

"""

# revision identifiers, used by Alembic.
revision = '7f6c3fd04ee8'
down_revision = 'd87d296fb8a9'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column(u'quote', sa.Column('gid', sa.Text(), nullable=True))
    op.execute("""
            UPDATE
               "quote"
            SET
                gid = 0
        """)


def downgrade():
    op.drop_column(u'quote', 'gid')
