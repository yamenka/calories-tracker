import boto3
from dotenv import load_dotenv
import os

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
            return s3_url
        except Exception as e:
            raise Exception(f"Failed to upload image to S3: {str(e)}")

        
