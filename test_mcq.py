from gemini_wrapper import get_response

your_text = """
Photosynthesis is the process used by plants to convert light energy into chemical energy.
It primarily occurs in the chloroplasts using chlorophyll.
"""

prompt = f"Generate 4 MCQs with answers based on the following text:\n\n{your_text}"
output = get_response(prompt)
print(output)
