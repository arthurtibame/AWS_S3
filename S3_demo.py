import logging
import boto3
from botocore.exceptions import ClientError

# setting up logging file info.
logging.basicConfig(
    filename="S3_demo.log",
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)


s3_client = boto3.client(service_name="s3")
_successful_message: str = "Successfully"

def upload_file(self, file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file

    try:
        s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False

    logging.info(_successful_message)
    return True

def download_file(file_name, bucket, object_name=None):
    """download a file to an S3 bucket

    :param file_name: File to download
    :param bucket: Bucket to download to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was download, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # download_file the file

    try:
        s3_client.download_file(bucket, object_name, file_name)
    except ClientError as e:
        logging.error(e)
        return False
    logging.info(self._successful_message)
    return True

def delete_file(bucket, object_name=None):
    """delete_file a file to an S3 bucket

    :param bucket: Bucket to delete to
    :param object_name: S3 object name. If not specified then return False
    :return: True if file was deleted, else False
    """

    # If S3 object_name was not specified, return False
    if object_name is None:
        return False

    # delete_file the file
    try:
        s3_client.delete_object(Bucket=bucket, Key=object_name)
    except ClientError as e:
        logging.error(e)
        return False
    logging.info(_successful_message)
    return True


if __name__ == "__main__":
    # upload_file('test.py', 'iii-tutorial-v2', 'student14/test1.py')
    # download_file('test1.py', 'iii-tutorial-v2', 'student14/test1.py')   
    
    delete_file("iii-tutorial-v2", "student14/test1.py")

