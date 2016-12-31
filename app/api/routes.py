from flask import request, jsonify, g, escape

from . import api, errors
# from .forms import PageForm
from app import db
from app.models import Page


@api.route('/page/<int:id>', methods=['POST'])
def page(id):
    request_data = request.get_json()
    page = Page.query.get_or_404(id)

    # if page.creator != g.current_user \
    #         and not g.current_user.is_admin:
    #     return errors.unauthorized

    setattr(page, request_data['name'], escape(request_data['value']))
    db.session.commit()

    return jsonify({'status': 'ok', 'data': request_data})

# @api.route('/comments/<int:id>', methods=['PUT'])
# def approve_comment(id):
#     comment = Comment.query.get_or_404(id)
#     if comment.talk.author != g.current_user and \
#             not g.current_user.is_admin:
#         return forbidden('You cannot modify this comment.')
#     if comment.approved:
#         return bad_request('Comment is already approved.')
#     comment.approved = True
#     db.session.add(comment)
#     db.session.commit()
#     send_comment_notification(comment)
#     return jsonify({'status': 'ok'})


# @api.route('/comments/<int:id>', methods=['DELETE'])
# def delete_comment(id):
#     comment = Comment.query.get_or_404(id)
#     if comment.talk.author != g.current_user and \
#             not g.current_user.is_admin:
#         return forbidden('You cannot modify this comment.')
#     if comment.approved:
#         return bad_request('Comment is already approved.')
#     db.session.delete(comment)
#     db.session.commit()
#     return jsonify({'status': 'ok'})

# @api.before_request
# def before_api_request():
#     if request.json is None:
#         return errors.bad_request('Invalid JSON in body.')
#     token = request.json.get('token')
#     if not token:
#         return errors.unauthorized('Authentication token not provided.')
#     user = User.validate_api_token(token)
#     if not user:
#         return errors.unauthorized('Invalid authentication token.')
#     g.current_user = user
