import logging
import boto3
from botocore.exceptions import ClientError
import os

from flaskRestAPI02.total_param import s3_upload_bucket_name


def upload_file(file_name, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    bucket = s3_upload_bucket_name

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, file_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# # 동작확인 테스트
# if __name__ == "__main__":
#     upload_file("sunny.png")
#     os.remove('sunny.png')