from flask import json, current_app
from itsdangerous import URLSafeTimedSerializer
import os, hashlib, time, re

from backend.helpers.constants import TEMPLATE_NAMES


def timed_url_safe():
    return URLSafeTimedSerializer(current_app.config["SECRET_KEY"])


def md5_identifier(identifier):
    return hashlib.md5(identifier).hexdigest()


def timestamp():
    return str(int(time.time()))


def path_builder(*paths):
    full_path = ''

    for path in paths:
        full_path += '/' + os.path.sep.join(\
                        filter(None, path.split(os.path.sep)))

    return full_path


def path_slicer(path, slice_path):
    path = path_builder(path)
    slice_path = path_builder(slice_path)

    return path[len(slice_path):]


def is_phone(user_agent):
    with open('backend/stubs/ua_detect.json', 'r') as json_file:
        ua_stub = json.load( json_file )
        ua_phone = ua_stub['uaMatch']['phones']

    detected_phone = None

    for phone, regex in ua_phone.iteritems():
        detected_phone = re.search(regex, str(user_agent))

        if detected_phone:
            break

    return bool(detected_phone)


def get_a_template(name):
    if not name == 'blank' and name in TEMPLATE_NAMES:
      stub = get_a_stub('templates/' + name)
    else:
      stub = {}
    return stub


def get_a_stub(name):
    with open('backend/stubs/' + name + '.json', 'r') as json_file:
        return json.load( json_file )


def get_page_stub(name):
    features = get_a_stub('features/all')
    page_stub = get_a_stub(name)

    for feature in features:
        for field in feature.get('fields'):
            if not page_stub.get( field.get('id') ):
                if field.get('default'):
                    page_stub[ field.get('id') ] = field.get('default')
                if field.get('id') == 'search_results_title':
                    page_stub['search_results_title'] = page_stub.get('content_title')
                if field.get('id') == 'search_results_description':
                    page_stub['search_results_description'] = page_stub.get('content_sub_title')

    return page_stub
