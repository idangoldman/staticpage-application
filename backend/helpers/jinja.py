from flask import current_app
from jinja2 import evalcontextfilter, Markup, escape
import markdown as markdown_lib
import re, jinja2, os


# images
images = jinja2.ChoiceLoader([
    current_app.jinja_loader,
    jinja2.FileSystemLoader('frontend/images')
])
current_app.jinja_loader = images

# markdown
@current_app.template_filter()
@evalcontextfilter
def markdown(eval_ctx, value):
    return Markup(markdown_lib.markdown(value))

# strftime
@current_app.template_filter()
def strftime(date, format):
    if '' is not date:
        return date.strftime(format.encode('utf-8')).decode('utf-8')
    else:
        return ''
