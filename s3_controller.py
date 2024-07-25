import boto3
from dotenv import load_dotenv
import os
import logging
from botocore.exceptions import ClientError


load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

class s3Controller():
    def __init__(self,bucket_name) -> None:
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )
        self.bucket_name = bucket_name

    def upload_image(self, file_path):
        try:
            file_key = os.path.basename(file_path)
            with open(file_path, "rb") as file:
                self.s3.upload_fileobj(file, self.bucket_name, file_key)
            s3_url = f"https://{self.bucket_name}.s3.amazonaws.com/{file_key}"
            return s3_url, file_key
        except Exception as e:
            raise Exception(f"Failed to upload image to S3: {str(e)}")

    def generate_presigned_url(self, bucket_name, file_key, expiration=3600):
        try:
            response = self.s3.generate_presigned_url('get_object',
                                                Params={'Bucket': bucket_name, 'Key': file_key},
                                                ExpiresIn=expiration)
        except ClientError as e:
            logging.error(e)
            return None
        return response
