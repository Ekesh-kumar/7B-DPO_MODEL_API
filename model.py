from flask import Flask, request, jsonify
import base64
import io
import time
import logging
from PIL import Image
from openai import OpenAI

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

class GUIAutomationAgent:
    def __init__(
        self,
        base_url,
        api_key,
        model: str = "tgi",
        max_tokens: int = 500,
        temperature: float = 0.2,
        top_p: float = 0.6,
        frequency_penalty: float = 0.0,
        presence_penalty: float = 0.0,
    ):
        """Initialize the GUI automation agent with OpenAI client settings and parameters."""
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty

    def preprocess_image(self, image) -> str:
        image_bytes = image.read()
        return base64.b64encode(image_bytes).decode("utf-8")

    def analyze_screen(self, image, instruction: str) -> str:
        """
        Sends an image and instruction to the OpenAI API and retrieves a response.
        """
        start_time = time.time()
        encoded_image = self.preprocess_image(image)

        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": instruction},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpg;base64,{encoded_image}"}},
                ],
            }
        ]

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                top_p=self.top_p,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty,
            )
            elapsed_time = time.time() - start_time
            logging.info(f"API Response Time: {elapsed_time:.2f}s")

            if not response.choices or not response.choices[0].message.content:
                raise ValueError("Invalid response from API")

            logging.info("Successfully retrieved response.")
            return response.choices[0].message.content

        except Exception as e:
            logging.error(f"Error in API invocation: {e}")
            return "Error processing the request."

