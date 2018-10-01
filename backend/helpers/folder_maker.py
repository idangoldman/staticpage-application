from flask import current_app
import os

from backend.helpers import path_builder, path_slicer, md5_identifier, timestamp


def create_uploads_folder( identifier ):
    return path_builder( md5_identifier( identifier ), timestamp() )


def create_download_folder( identifier ):
    folder_path = path_builder( current_app.config['BASE_PATH'], \
                                current_app.config['TMP_FOLDER'], \
                                md5_identifier( identifier ), \
                                timestamp() )

    paths = [ folder_path, \
              folder_path + '/page/css', \
              folder_path + '/page/images' ]

    for path in paths:
        if not os.path.isdir( path ):
            os.makedirs( path )

    return folder_path
