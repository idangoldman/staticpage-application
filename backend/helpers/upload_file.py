from werkzeug.utils import secure_filename
import boto3
import os

from backend.helpers import path_builder
from backend.helpers.folder_maker import user_file_uri

ALLOWED_EXTENSIONS = ('png','gif','jpg','jpeg','webp')


def file_extension( file_name ):
    return file_name.rsplit( '.', 1 )[ 1 ].lower()


def file_extension_allowed( file_name ):
    return '.' in file_name and \
           file_extension( file_name ) in ALLOWED_EXTENSIONS


def upload_file( _file, dest_path ):
    if not _file or not file_extension_allowed( _file.filename ):
        return None

    try:
        boto3.client('s3').upload_fileobj(
            _file,
            os.environ['AWS_S3_BUCKET'],
            dest_path + '.' + file_extension( _file.filename ),
            {
                "ACL": "public-read",
                "ContentType": _file.content_type
            }
        )
    except:
        return None

    return "{}{}".format('http://{}.s3.amazonaws.com/'.format(os.environ['AWS_S3_BUCKET']), dest_path + '.' + file_extension( _file.filename ))
