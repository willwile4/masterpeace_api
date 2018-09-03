"""empty message

Revision ID: 4d27ce5da6eb
Revises: 
Create Date: 2018-07-04 08:37:55.848492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d27ce5da6eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('user_name', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_name'),
    sa.UniqueConstraint('email')
    )
    op.create_table('ImageMP',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=55), nullable=True),
    sa.Column('author', sa.Integer(), nullable=True),
    sa.Column('post', sa.String(length=1000), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author'], [u'users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('TextMP',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=55), nullable=True),
    sa.Column('author', sa.Integer(), nullable=True),
    sa.Column('post', sa.String(length=1000), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author'], [u'users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('TextMP')
    op.drop_table('ImageMP')
    op.drop_table('users')
    # ### end Alembic commands ###
