import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

def GenrateResponse(input_text):
    
  response = model.generate_content([
  "you are agriculture chatbot so reply accordingly",
  "input: what all can you do",
  "output: I can provide you any agriculture related information and \ncan help you to solve your agriculture related problems",
  f"input: {input_text}",
  "output: ",
  ])
  return response.text

#while True:
    #string =str(input("Enter your prompt:"))
    #print("BOT:",GenrateResponse(string))
