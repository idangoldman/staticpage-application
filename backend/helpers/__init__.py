from flask import json
import os, hashlib, time, re


def load_env_var( env_file = 'flask_env' ):
    if os.path.exists(env_file):
        print(' * Importing environment from %s...' % env_file)
        for line in open(env_file):
            variables = line.strip().split('=')
            if len(variables) == 2:
                # print(variables[0])
                os.environ[variables[0]] = variables[1]


def md5_identifier( identifier ):
    return hashlib.md5( identifier ).hexdigest()


def timestamp():
    return str(int(time.time()))


def path_builder( *paths ):
    full_path = ''

    for path in paths:
        full_path += '/' + os.path.sep.join( \
                        filter( None, path.split( os.path.sep ) ) )

    return full_path


def path_slicer( path, slice_path ):
    path = path_builder( path )
    slice_path = path_builder( slice_path )

    return path[ len( slice_path ) : ]


def is_phone( user_agent ):
    with open('backend/stubs/ua_detect.json', 'r') as json_file:
        ua_stub = json.load( json_file )
        ua_phone = ua_stub['uaMatch']['phones']

    detected_phone = None

    for phone, regex in ua_phone.iteritems():
        detected_phone = re.search( regex, str( user_agent ) )

        if detected_phone:
            break

    return bool( detected_phone )


def get_a_stub( name ):
    with open('backend/stubs/' + name + '.json', 'r') as json_file:
        return json.load( json_file )


def get_page_stub( name ):
    with open('backend/stubs/features.json', 'r') as json_file:
        features = json.load( json_file )
    with open('backend/stubs/website/' + name + '.json', 'r') as json_file:
        page_stub = json.load( json_file )

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
