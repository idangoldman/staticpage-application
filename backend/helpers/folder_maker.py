from flask import current_app
import os

from backend.helpers import path_builder, path_slicer, md5_identifier, timestamp


def create_uploads_folder( identifier ):
    folder_path = path_builder( current_app.config['BASE_PATH'], \
                                current_app.config['USER_FOLDER'], \
                                md5_identifier( identifier ), \
                                'uploads', \
                                timestamp() )

    if not os.path.isdir( folder_path ):
        os.makedirs( folder_path )

    return folder_path


def create_download_folder( identifier ):
    folder_path = path_builder( current_app.config['BASE_PATH'], \
                                current_app.config['USER_FOLDER'], \
                                md5_identifier( identifier ), \
                                'downloads', \
                                timestamp() )

    paths = [ folder_path, \
              folder_path + '/page/css', \
              folder_path + '/page/images' ]

    for path in paths:
        if not os.path.isdir( path ):
            os.makedirs( path )

    return folder_path


def user_folder_uri( folder_path ):
    base_path = path_builder( current_app.config['BASE_PATH'], \
                              current_app.config['USER_FOLDER'] )
    folder_uri = path_slicer( folder_path, base_path )

    return folder_uri
