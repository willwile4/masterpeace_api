"""empty message

Revision ID: 5349b89473db
Revises: 37a006a57b2e
Create Date: 2018-03-28 21:20:43.922793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5349b89473db'
down_revision = '37a006a57b2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=30), nullable=False),
    sa.Column('display_name', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('display_name'),
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
    op.add_column(u'TextMP', sa.Column('author', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'TextMP', 'users', ['author'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'TextMP', type_='foreignkey')
    op.drop_column(u'TextMP', 'creator')
    op.drop_table('ImageMP')
    op.drop_table('users')
    # ### end Alembic commands ###
