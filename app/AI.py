
from google import genai
import sys
import os
from dotenv import load_dotenv

load_dotenv()

def getGeminiResponse(key, prompt):
	try: 
		client = genai.Client(api_key=key)
		response = client.models.generate_content(
			model="gemini-2.5-flash", contents=prompt
		)
		return response.text
	except Exception as e:
		return f"<p><b>Gemini API Error:</b> {str(e)}</p>"