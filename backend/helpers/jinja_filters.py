from flask import current_app
from jinja2 import evalcontextfilter, Markup, escape
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
    if value == None:
        value = ''

    _paragraph_re = re.compile( r'(?:\r\n|\r|\n){2,}' )
    result = u'\n\n'.join( u'%s' % p.replace('\n', '<br>\n' ) \
        for p in _paragraph_re.split( escape( value ) ) )
    if eval_ctx.autoescape:
        result = Markup( result )
    return result
