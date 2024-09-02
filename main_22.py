import gradio as gr
import requests
from fastapi import FastAPI, UploadFile, File
import boto3
import json
import os
from dotenv import load_dotenv
from openai_controller import OpenAIController
from s3_controller import s3Controller
from PIL import Image
import io
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

s3_controller = s3Controller(S3_BUCKET_NAME)
openai_controller = OpenAIController(OPENAI_API_KEY)

def upload_and_analyze_image(file):
    image = Image.open(file)
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    bytes_im = buf.getvalue()

    s3_url, file_jey = s3_controller.upload_image(file)
    presigned = s3_controller.generate_presigned_url(S3_BUCKET_NAME,file_jey)
    print(presigned)
    result = openai_controller.analyze_image(presigned)
    result = json.dumps(result)
    return result, image



interface = gr.Interface(
    upload_and_analyze_image,
    gr.Image(sources=["webcam"], streaming=False),
    live=True,
    outputs=[gr.Textbox(label="Analysis Result"), gr.Image(label="Uploaded Image")],
    title="Image Analysis Service",
    description="Upload an image to analyze using OpenAI API",
)

if __name__ == "__main__":
    interface.launch()