import gradio as gr
import requests
from fastapi import FastAPI, UploadFile, File
import boto3
import os
from dotenv import load_dotenv
from openai_controller import OpenAIController
from s3_controller import s3Controller
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

s3_controller = s3Controller(S3_BUCKET_NAME)
openai_controller = OpenAIController(OPENAI_API_KEY)

def upload_and_analyze_image(file):
    s3_url = s3_controller.upload_image(file)
    openai_controller.analyze_image(s3_url)




interface = gr.Interface(
    fn=upload_and_analyze_image,
    inputs=gr.File(label="Upload an image"),
    outputs="json",
    title="Image Analysis Service",
    description="Upload an image to analyze using OpenAI API",
)

if __name__ == "__main__":
    interface.launch()