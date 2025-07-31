import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("AIzaSyCH8TJUfsuGqDOzPg1tlpVNfGaDY5f8dWQ"))
model = genai.GenerativeModel("gemini-2.5-flash")

def get_response(prompt):
    response = model.generate_content(prompt)
    return response.text



 

