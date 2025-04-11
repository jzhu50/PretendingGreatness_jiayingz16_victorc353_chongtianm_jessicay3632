from google import genai
import sys

def getGeminiResponse(key, prompt):
	try: 
		client = genai.Client(api_key=key)
		response = client.models.generate_content(
				model="gemini-2.5-pro-exp-03-25", contents=prompt
		)
		return response.text
	except Exception as e:
		return f"<p><b>Gemini API Error:</b> {str(e)}</p>"