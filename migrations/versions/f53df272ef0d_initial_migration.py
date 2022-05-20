"""Initial Migration

Revision ID: f53df272ef0d
Revises: 526651bed1ec
Create Date: 2022-05-19 23:22:06.808595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f53df272ef0d'
down_revision = '526651bed1ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    op.drop_column('roles', 'pass_secure')
    # ### end Alembic commands ###