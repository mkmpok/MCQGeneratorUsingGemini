import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("YOUR_GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

def get_response(prompt):
    response = model.generate_content(prompt)
    return response.text



 

