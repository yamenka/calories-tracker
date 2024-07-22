import requests
import os
import openai
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class OpenAIController:
    def __init__(self, api_key):
        openai.api_key = OPENAI_API_KEY
        self.model = "gpt-4o"
        self.prompt = "Analyze the number of calories and answer in this template : Hello user your meal contains "

    def analyze_image(self, s3_url):
        messages = [{"role": "user", "content": self.prompt}]

        response = openai.ChatCompletion.create(

        model=self.model,

        messages=messages,

        temperature=0,

        )