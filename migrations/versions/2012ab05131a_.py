"""empty message

Revision ID: 2012ab05131a
Revises: bbc75263a435
Create Date: 2019-01-13 22:39:41.379708

"""

# revision identifiers, used by Alembic.
revision = '2012ab05131a'
down_revision = 'bbc75263a435'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.String(length=255),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'email',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=64),
               existing_nullable=False)
    # ### end Alembic commands ###
