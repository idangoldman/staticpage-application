"""empty message

Revision ID: c6b92c1dcff4
Revises: 46f6f051f4db
Create Date: 2018-10-12 14:58:27.548044

"""

# revision identifiers, used by Alembic.
revision = 'c6b92c1dcff4'
down_revision = '46f6f051f4db'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pages', sa.Column('social_links_facebook_link', sa.String(length=128), nullable=True))
    op.add_column('pages', sa.Column('social_links_icon_style', sa.String(length=128), nullable=True))
    op.add_column('pages', sa.Column('social_links_instagram_link', sa.String(length=128), nullable=True))
    op.add_column('pages', sa.Column('social_links_linkedin_link', sa.String(length=128), nullable=True))
    op.add_column('pages', sa.Column('social_links_twitter_link', sa.String(length=128), nullable=True))
    op.add_column('pages', sa.Column('social_links_youtube_link', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pages', 'social_links_youtube_link')
    op.drop_column('pages', 'social_links_twitter_link')
    op.drop_column('pages', 'social_links_linkedin_link')
    op.drop_column('pages', 'social_links_instagram_link')
    op.drop_column('pages', 'social_links_icon_style')
    op.drop_column('pages', 'social_links_facebook_link')
    # ### end Alembic commands ###
