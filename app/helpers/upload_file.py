from flask import current_app
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = ('png','gif','jpg','jpeg','webp', 'svg')


def file_extension_allowed( file_name ):
    return '.' in file_name and \
           file_name.rsplit( '.', 1 )[ 1 ].lower() in ALLOWED_EXTENSIONS


def upload_file( _file, dest_path ):
    if not _file:
        return None

    file_name = secure_filename( _file.filename )

    if not file_name \
            or not file_extension_allowed( file_name ):
        return None

    try:
        file_path = os.path.sep.join( [ dest_path, file_name ] )
        _file.save( file_path )
    except:
        return None

    return file_name
