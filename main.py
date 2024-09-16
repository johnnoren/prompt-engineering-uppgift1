import os
from instructor import patch
from openai import OpenAI
from pydantic import BaseModel

# Create the OpenAI client using the API key from environment variable
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Patch the OpenAI client with Instructor
patch(client)

# Define a Pydantic model for the response
class GPTResponse(BaseModel):
    content: str

# Make the API call
response = client.chat.completions.create(
    model="gpt-4",
    response_model=GPTResponse,
    messages=[
        {"role": "user", "content": "Hi, who are you?"}
    ]
)

# Print the response
print(response.content)
