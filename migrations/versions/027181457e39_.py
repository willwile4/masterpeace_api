"""empty message

Revision ID: 027181457e39
Revises: 4d27ce5da6eb
Create Date: 2018-08-25 11:01:58.766162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '027181457e39'
down_revision = '4d27ce5da6eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('location', sa.String(length=25), nullable=True))
    op.add_column('users', sa.Column('photo', sa.String(length=100), nullable=True))
    op.add_column('users', sa.Column('quip', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'quip')
    op.drop_column('users', 'photo')
    op.drop_column('users', 'location')
    # ### end Alembic commands ###
