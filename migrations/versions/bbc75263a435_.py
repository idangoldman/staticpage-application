"""empty message

Revision ID: bbc75263a435
Revises: b756953d5736
Create Date: 2018-12-28 22:26:46.827152

"""

# revision identifiers, used by Alembic.
revision = 'bbc75263a435'
down_revision = 'b756953d5736'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pages', 'content_logo',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=2083),
               existing_nullable=True)
    op.alter_column('pages', 'countdown_redirect_url',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=2083),
               existing_nullable=True)
    op.alter_column('pages', 'countdown_timezone',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.String(length=128),
               existing_nullable=True)
    op.alter_column('pages', 'design_background_image',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=2083),
               existing_nullable=True)
    op.alter_column('pages', 'design_font_family',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=256),
               existing_nullable=True)
    op.alter_column('pages', 'mailing_list_message',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=2083),
               existing_nullable=True)
    op.alter_column('pages', 'mailing_list_redirect_url',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=2083),
               existing_nullable=True)
    op.alter_column('pages', 'name',
               existing_type=sa.VARCHAR(length=128),
               nullable=True,
               existing_server_default=sa.text(u"'index'::character varying"))
    op.alter_column('pages', 'social_links_facebook_link',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=2083),
               existing_nullable=True)
    op.alter_column('pages', 'social_links_instagram_link',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=2083),
               existing_nullable=True)
    op.alter_column('pages', 'social_links_linkedin_link',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=2083),
               existing_nullable=True)
    op.alter_column('pages', 'social_links_twitter_link',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=2083),
               existing_nullable=True)
    op.alter_column('pages', 'social_links_youtube_link',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=2083),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pages', 'social_links_youtube_link',
               existing_type=sa.String(length=2083),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)
    op.alter_column('pages', 'social_links_twitter_link',
               existing_type=sa.String(length=2083),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)
    op.alter_column('pages', 'social_links_linkedin_link',
               existing_type=sa.String(length=2083),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)
    op.alter_column('pages', 'social_links_instagram_link',
               existing_type=sa.String(length=2083),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)
    op.alter_column('pages', 'social_links_facebook_link',
               existing_type=sa.String(length=2083),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)
    op.alter_column('pages', 'name',
               existing_type=sa.VARCHAR(length=128),
               nullable=False,
               existing_server_default=sa.text(u"'index'::character varying"))
    op.alter_column('pages', 'mailing_list_redirect_url',
               existing_type=sa.String(length=2083),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)
    op.alter_column('pages', 'mailing_list_message',
               existing_type=sa.String(length=2083),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)
    op.alter_column('pages', 'design_font_family',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)
    op.alter_column('pages', 'design_background_image',
               existing_type=sa.String(length=2083),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)
    op.alter_column('pages', 'countdown_timezone',
               existing_type=sa.String(length=128),
               type_=sa.VARCHAR(length=64),
               existing_nullable=True)
    op.alter_column('pages', 'countdown_redirect_url',
               existing_type=sa.String(length=2083),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)
    op.alter_column('pages', 'content_logo',
               existing_type=sa.String(length=2083),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)
    # ### end Alembic commands ###
