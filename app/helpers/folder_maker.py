from flask import current_app
import os

from . import path_builder, path_slicer, md5_identifier, timestamp


def user_folder_path( identifier ):
    folder_path = path_builder( current_app.config['BASE_PATH'], \
                                current_app.config['UPLOAD_FOLDER'], \
                                md5_identifier( identifier ), \
                                timestamp() )

    if not os.path.isdir( folder_path ):
        os.makedirs( folder_path )

    return folder_path


def user_folder_uri( folder_path ):
    base_path = current_app.config['BASE_PATH']
    folder_uri = path_slicer( folder_path, base_path )

    return folder_uri
