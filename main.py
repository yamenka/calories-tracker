from fastapi import FastAPI, UploadFile, File  # Ensure File is imported here
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import openai  # Make sure to install openai package
import os
import json
import tempfile
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

app = FastAPI()

@app.get("/")
async def read_index():
    return FileResponse("index.html")

@app.post("/upload_and_analyze_image/")
async def upload_and_analyze_image(file: UploadFile = File(...)):
    try:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(await file.read())
            tmp.flush()
            tmp.seek(0)

            s3_url, file_key = s3_controller.upload_image(tmp.name)
        presigned = s3_controller.generate_presigned_url(S3_BUCKET_NAME, file_key)
        result = openai_controller.analyze_image(presigned)
        result = json.dumps(result)
        return {"result": result, "image": presigned}
    finally:
        os.unlink(tmp.name)

@app.post("/chat")
async def chat(message: dict):
    user_message = message.get("message", "")
    context = message.get("context", "")

    # Call the chat method
    chat_response = openai_controller.chat(user_message, context)

    # Return the chat response
    return chat_response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
