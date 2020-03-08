"""empty message

Revision ID: 25640f754903
Revises: 45019418bb80
Create Date: 2020-05-22 13:19:43.762772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25640f754903'
down_revision = '45019418bb80'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'posted_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('posted_at', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
