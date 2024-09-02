
import requests
import os
from openai import OpenAI
import requests
import json
import logging
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class OpenAIController:
    def __init__(self, api_key):
        self.client = OpenAI()
        
    def analyze_image(self,uploaded_image_url, API_KEY=OPENAI_API_KEY):
        response = self.client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": """You are a dietitian. A user sends you an image of a meal and you tell them how many calories are in it. Use the following JSON format:

{
    "reasoning": "reasoning for the total calories",
    "food_items": [
        {
            "name": "food item name",
            "calories": "calories in the food item"
        }
    ],
    "total": "total calories in the meal"
}"""
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "How many calories is in this meal?"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": uploaded_image_url
                        }
                    }
                ]
            },
        ],
    )
        print(response)
        response_message = response.choices[0].message
        content = response_message.content
        print(content)
        return json.loads(content)






    def chat(self, user_message, context, API_KEY=None):

        # Prepare the prompt using the context and user message
        prompt = f"Based on the following image analysis:\n{context}\n\nUser: {user_message}\nChatGPT:"

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert conversational assistant. Answer the user's questions based on the provided context."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=150  # Adjust according to your needs
        )

        print(response)
        response_message = response.choices[0].message.content.strip()
        return {"reply": response_message}