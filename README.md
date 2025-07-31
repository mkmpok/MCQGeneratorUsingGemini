MCQ Generator using Gemini API

This project is an automated Multiple Choice Question (MCQ) generator powered by Google's Gemini API. It takes educational content (text, PDF, or URLs) as input and uses Natural Language Processing to generate relevant MCQs. It is inspired by Langchain + OpenAI-based MCQ generators, but implemented using Gemini Pro for cost-effective and flexible LLM integration.


✨ Features
🔁 Converts long-form content into questions
📝 Generates MCQs (with 4 options and one correct answer)
📄 Accepts input from:
    Plain text
    PDF files
    URLs (with content extraction)
🧠 Uses Google Gemini Pro via Gemini API
⚙️ Streamlined backend using Python and Flask
💡 Custom prompt engineering for educational tasks

🔧 Installation::
1) Clone the repository
git clone https://github.com/mkmpok/MCQGeneratorUsingGemini.git
cd MCQGeneratorUsingGemini

2)Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3)Set your environment variables
GEMINI_API_KEY=your_gemini_api_key

4) to Run the Project
   streamlit app.py
