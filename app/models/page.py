from flask import json
from datetime import datetime

from app import db


class Page(db.Model):
    __tablename__ = 'pages'

    id = db.Column('id', db.Integer, primary_key=True, index=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column('created_at', db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column('updated_at', db.DateTime(), default=datetime.utcnow)

    file_type = db.Column('file_type', db.String(16), nullable=False, default='welcome')
    file_name = db.Column('file_name', db.String(128), default='index')

    content_logo = db.Column('content_logo', db.String(128))
    content_title = db.Column('content_title', db.Text())
    content_sub_title = db.Column('content_sub_title', db.Text())
    content_description = db.Column('content_description', db.Text())

    design_background_image = db.Column('design_background_image', db.String(128))
    design_background_color = db.Column('design_background_color', db.String(8))
    design_background_repeat = db.Column('design_background_repeat', db.String(16))
    design_font_family = db.Column('design_font_family', db.String(128))
    design_base_font_size = db.Column('design_base_font_size', db.String(8))
    design_font_color = db.Column('design_font_color', db.String(8))
    design_content_alignment = db.Column('design_content_alignment', db.String(8))
    design_content_direction = db.Column('design_content_direction', db.String(3))
    design_additional_styles = db.Column('design_additional_styles', db.Text())

    search_results_title = db.Column('search_results_title', db.Text())
    search_results_description = db.Column('search_results_description', db.Text())


    def with_features(self):
        with open('app/stubs/features.json', 'r') as json_file:
            features = json.load( json_file )

        page_dict = self.__dict__

        for feature in features:
            for field in feature.get('fields'):
                page_field_value = page_dict.get( field.get('id') )
                if page_field_value:
                    field['value'] = page_field_value

        return features

    def with_defaults(self):
        with open('app/stubs/features.json', 'r') as json_file:
            features = json.load( json_file )

        page_dict = self.__dict__

        for feature in features:
            for field in feature.get('fields'):
                if not page_dict.get( field.get('id') ) and field.get('default'):
                    page_dict[ field.get('id') ] = field.get('default')

        return page_dict
