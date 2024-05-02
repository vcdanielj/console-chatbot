# Gemini Docs: https://ai.google.dev/gemini-api/docs/get-started/python?hl=es-419#chat_conversations

""" 
import textwrap

import google.generativeai as genai

from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

GOOGLE_API_KEY="AIzaSyBkzq50iPd6Iljyn0vKpw1HsChTA6hu5gs"

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

while True:
  message = input("Usuario: ")

  response = chat.send_message(message, stream=True)
  print("AI:", end=" ")
  for chunk in response:
    print(chunk.text)
    print("_"*80)
 """

