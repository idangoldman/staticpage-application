from flask import current_app
from jinja2 import evalcontextfilter, Markup
import markdown as markdown_lib
import re


# markdown
@current_app.template_filter()
@evalcontextfilter
def markdown(eval_ctx, value):
    return Markup(markdown_lib.markdown(value))

# nl2br
@current_app.template_filter()
@evalcontextfilter
def nl2br(eval_ctx, value):
    value = re.sub(r'\r\n|\r|\n', '\n', value)
    param = re.split('\n{2,}', value)
    param = [u'%s' % p.replace('\n', '<br />') for p in param]
    param = u'\n\n'.join(param)
    return Markup(param)