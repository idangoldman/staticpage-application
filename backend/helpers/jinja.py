from flask import current_app, request
from jinja2 import evalcontextfilter, Markup, escape
import markdown as markdown_lib
import re, jinja2, os

from backend.helpers import is_phone


# images
images = jinja2.ChoiceLoader([
    current_app.jinja_loader,
    jinja2.FileSystemLoader('frontend/images')
])
current_app.jinja_loader = images

# template variables
@current_app.context_processor
def template_variables():
  return dict(
    sentry_dsn = os.environ['SENTRY_DSN_JAVASCRIPT'],
    on_phone = is_phone(request.user_agent)
  )

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
