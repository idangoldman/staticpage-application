from flask import current_app
import os

from . import path_builder, md5_identifier


def user_folder_path( identifier ):
    folder_path = path_builder( current_app.config['BASE_PATH'], \
                                current_app.config['UPLOAD_FOLDER'], \
                                md5_identifier( identifier ) )

    if not os.path.isdir( folder_path ):
        os.makedirs( folder_path )

    return folder_path

def user_folder_uri( identifier ):
    folder_uri = path_builder( current_app.config['UPLOAD_FOLDER'], \
                                md5_identifier( identifier ) )

    return folder_uri
