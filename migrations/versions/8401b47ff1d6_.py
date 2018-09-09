"""empty message

Revision ID: 8401b47ff1d6
Revises: 1adc950e9f33
Create Date: 2018-09-09 15:33:08.741700

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8401b47ff1d6'
down_revision = '1adc950e9f33'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ImageMP', sa.Column('created', sa.DateTime(), nullable=True))
    op.add_column('ImageMP', sa.Column('modified', sa.DateTime(), nullable=True))
    op.drop_column('ImageMP', 'date_created')
    op.drop_column('ImageMP', 'date_modified')
    op.add_column('TextMP', sa.Column('created', sa.DateTime(), nullable=True))
    op.add_column('TextMP', sa.Column('modified', sa.DateTime(), nullable=True))
    op.drop_column('TextMP', 'date_created')
    op.drop_column('TextMP', 'date_modified')
    op.add_column('users', sa.Column('created', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('modified', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'modified')
    op.drop_column('users', 'created')
    op.add_column('TextMP', sa.Column('date_modified', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('TextMP', sa.Column('date_created', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('TextMP', 'modified')
    op.drop_column('TextMP', 'created')
    op.add_column('ImageMP', sa.Column('date_modified', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('ImageMP', sa.Column('date_created', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('ImageMP', 'modified')
    op.drop_column('ImageMP', 'created')
    # ### end Alembic commands ###
