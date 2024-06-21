
import textwrap

import google.generativeai as genai

from IPython.display import Markdown


def to_markdown(text):
  """
  Convierte texto plano a formato markdown.
  """
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Establece tu clave de API de Google
GOOGLE_API_KEY = "AIzaSyBkzq50iPd6Iljyn0vKpw1HsChTA6hu5gs"

# Configura la biblioteca de inteligencia artificial generativa con la clave de API
genai.configure(api_key=GOOGLE_API_KEY)

# Crea una instancia del modelo generativo
model = genai.GenerativeModel('gemini-pro')

# Start a chat session with an empty history
chat = model.start_chat(history=[])

while True:
  # Get user input
  message = input("Usuario: ")

  # Send user message to the chat model and receive response
  response = chat.send_message(message, stream=True)

  # Print the AI response
  print("AI:", end=" ")
  for chunk in response:
    print(chunk.text)
    print("_" * 80)


