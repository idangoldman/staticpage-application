from werkzeug.utils import secure_filename
from flask import current_app
import boto3
import os

from backend.helpers import path_builder

ALLOWED_EXTENSIONS = ('png','gif','jpg','jpeg','webp')


def file_extension( file_name ):
    return file_name.rsplit( '.', 1 )[ 1 ].lower()


def file_extension_allowed( file_name ):
    return '.' in file_name and \
           file_extension( file_name ) in ALLOWED_EXTENSIONS


def upload_file( _file, dest_path ):
    if not _file or not file_extension_allowed( _file.filename ):
        return None

    file_path = dest_path + '/' + _file.filename

    try:
        boto3.client('s3').upload_fileobj(
            _file,
            os.environ['AWS_S3_BUCKET'],
            file_path,
            {
                'ACL': 'public-read',
                'ContentType': _file.content_type
            }
        )
    except:
        return None

    return "{}{}".format(current_app.config['AWS_S3_BUCKET_URL'], file_path)
