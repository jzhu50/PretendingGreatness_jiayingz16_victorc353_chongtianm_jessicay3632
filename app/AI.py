from google import genai
import sys

def getGeminiResponse(key, prompt):

	client = genai.Client(api_key=key)

	response = client.models.generate_content(
    		model="gemini-2.5-pro-exp-03-25", contents=prompt
	)
	
	return response.text