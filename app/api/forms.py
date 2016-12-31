from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length


class PageForm(FlaskForm):
    # content_logo = StringField('', validators=[Length(1,64)])
    content_title = StringField('', validators=[Length(0,64)])
    # content_sub_title = StringField('', validators=[Length(1,64)])
    # content_description = StringField('', validators=[Length(1,64)])

    # design_background_image = StringField('', validators=[Length(1,64)])
    # design_background_color = StringField('', validators=[Length(1,64)])
    # design_background_repeat = StringField('', validators=[Length(1,64)])
    # design_font_family = StringField('', validators=[Length(1,64)])
    # design_base_font_size = StringField('', validators=[Length(1,64)])
    # design_font_color = StringField('', validators=[Length(1,64)])
    # design_content_alignment = StringField('', validators=[Length(1,64)])
    # design_content_direction = StringField('', validators=[Length(1,64)])
    # design_additional_styles = StringField('', validators=[Length(1,64)])

    # search_results_title = StringField('', validators=[Length(1,64)])
    # search_results_description = StringField('', validators=[Length(1,64)])