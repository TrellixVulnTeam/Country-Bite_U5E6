"""empty message

Revision ID: 95d594925919
Revises: 524ac5c5c0d0
Create Date: 2020-05-02 09:00:34.169600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95d594925919'
down_revision = '524ac5c5c0d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'message')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('message', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
