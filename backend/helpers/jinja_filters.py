from flask import current_app
from jinja2 import evalcontextfilter, Markup, escape
import markdown as markdown_lib
import re, jinja2


# markdown
@current_app.template_filter()
@evalcontextfilter
def markdown(eval_ctx, value):
    return Markup(markdown_lib.markdown(value))
