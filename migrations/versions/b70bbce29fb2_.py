"""empty message

Revision ID: b70bbce29fb2
Revises: 6a5ffa135d6b
Create Date: 2020-05-01 14:46:24.147146

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b70bbce29fb2'
down_revision = '6a5ffa135d6b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('feedback', sa.Column('by', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'feedback', 'users', ['by'], ['id'])
    op.drop_column('feedback', 'at')
    op.drop_column('feedback', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('feedback', sa.Column('email', sa.VARCHAR(length=30), autoincrement=False, nullable=True))
    op.add_column('feedback', sa.Column('at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'feedback', type_='foreignkey')
    op.drop_column('feedback', 'by')
    # ### end Alembic commands ###
