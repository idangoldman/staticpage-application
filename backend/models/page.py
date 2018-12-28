from flask import json, current_app
from datetime import datetime

from backend import db
from backend.helpers import get_a_stub

class Page(db.Model):
    __tablename__ = 'pages'

    id = db.Column('id', db.Integer, primary_key=True, index=True)
    name = db.Column('name', db.String(128), default='index')
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column('created_at', db.DateTime(), default=datetime.utcnow)

    content_logo = db.Column('content_logo', db.String(128))
    content_title = db.Column('content_title', db.Text())
    content_sub_title = db.Column('content_sub_title', db.Text())
    content_description = db.Column('content_description', db.Text())

    design_background_image = db.Column('design_background_image', db.String(128))
    design_background_color = db.Column('design_background_color', db.String(8))
    design_background_repeat = db.Column('design_background_repeat', db.String(16))
    design_font_family = db.Column('design_font_family', db.String(128))
    design_font_color = db.Column('design_font_color', db.String(8))
    design_content_alignment = db.Column('design_content_alignment', db.String(8))
    design_content_direction = db.Column('design_content_direction', db.String(3))
    design_additional_styles = db.Column('design_additional_styles', db.Text())

    search_results_title = db.Column('search_results_title', db.Text())
    search_results_description = db.Column('search_results_description', db.Text())

    google_analytics_code = db.Column('google_analytics_code', db.String(24))

    countdown_timezone = db.Column('countdown_timezone', db.String(64))
    countdown_datetime = db.Column('countdown_datetime', db.DateTime())
    countdown_redirect_url = db.Column('countdown_redirect_url', db.String(128))

    mailing_list_service = db.Column('mailing_list_service', db.String(128))
    mailing_list_mailchimp_username = db.Column('mailing_list_mailchimp_username', db.String(128))
    mailing_list_mailchimp_api_key = db.Column('mailing_list_mailchimp_api_key', db.String(128))
    mailing_list_mailchimp_list_id = db.Column('mailing_list_mailchimp_list_id', db.String(128))
    mailing_list_successful_submission = db.Column('mailing_list_successful_submission', db.String(128), default='successful-submission-message')
    mailing_list_message = db.Column('mailing_list_message', db.String(128))
    mailing_list_redirect_url = db.Column('mailing_list_redirect_url', db.String(128))
    mailing_list_cta_color = db.Column('mailing_list_cta_color', db.String(8))
    mailing_list_cta_text = db.Column('mailing_list_cta_text', db.String(128))
    mailing_list_placeholder_text = db.Column('mailing_list_placeholder_text', db.String(128))

    social_links_icon_style = db.Column('social_links_icon_style', db.String(128), default='colored')
    social_links_facebook_link = db.Column('social_links_facebook_link', db.String(128))
    social_links_instagram_link = db.Column('social_links_instagram_link', db.String(128))
    social_links_linkedin_link = db.Column('social_links_linkedin_link', db.String(128))
    social_links_twitter_link = db.Column('social_links_twitter_link', db.String(128))
    social_links_youtube_link = db.Column('social_links_youtube_link', db.String(128))


    def with_features(self):
        features = get_a_stub('features/all')

        page_dict = self.__dict__

        for feature in features:
            for field in feature.get('fields'):
                field['value'] = page_dict.get(field.get('id')) or field.get('value') or ''

                if field.get('id') == 'search_results_title':
                    field['placeholder'] = page_dict.get('content_title') \
                                           or ''
                if field.get('id') == 'search_results_description':
                    field['placeholder'] = page_dict.get('content_sub_title') \
                                           or ''

                if field.get('id') == 'search_results_preview':
                    field['link'] = current_app.config['HTTP_HOST'] + '/page/' + self.creator.site_name
                    field['link_title'] = page_dict.get('search_results_title') \
                                            or page_dict.get('content_title') \
                                            or ''
                    field['description'] = page_dict.get('search_results_description') \
                                            or page_dict.get('content_sub_title') \
                                            or ''
                if field.get('type') == 'fieldset':
                    for second_field in field.get('fields'):
                        second_field['value'] = page_dict.get(second_field.get('id')) or second_field.get('value') or ''

        return {
          'page': page_dict,
          'features': features
        }


    def with_defaults(self):
        features = get_a_stub('features/all')

        page_dict = self.__dict__

        for feature in features:
            for field in feature.get('fields'):

                if not page_dict.get(field.get('id')):
                    page_dict[field.get('id')] = field.get('default') or ''

                if field.get('id') == 'search_results_title':
                    page_dict['search_results_title'] = page_dict.get('search_results_title') \
                                            or page_dict.get('content_title') \
                                            or ''
                if field.get('id') == 'search_results_description':
                    page_dict['search_results_description'] = page_dict.get('search_results_description') \
                                            or page_dict.get('content_sub_title') \
                                            or ''

                if field.get('type') == 'fieldset':
                    for second_field in field.get('fields'):
                        if not page_dict.get(second_field.get('id')):
                            page_dict[second_field.get('id')] = second_field.get('default') or ''

        if page_dict.get('countdown_timezone'):
            page_dict['countdown_timezone'] = page_dict['countdown_timezone'].split('|')[1]

        if page_dict.get('countdown_datetime'):
            page_dict['countdown_datetime_with_timezone'] = " ".join([
                str(page_dict['countdown_datetime']),
                page_dict['countdown_timezone']
            ])

        return page_dict
