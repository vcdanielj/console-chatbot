import textwrap

import google.generativeai as genai

from IPython.display import Markdown


class Chatbot:
  def __init__(self, api_key, modelo="gemini-pro"):
    self.cliente = genai.ServiceClient(api_key=api_key)
    self.modelo = modelo
    self.historial = []
    self.chat = self.cliente.generative_models().get(name=f"projects/-/locations/global/models/{modelo}").chat()

  def generar_respuesta(self, mensaje):
    self.historial.append(mensaje)
    respuesta = self.chat.send_messages(input=genai.TextInputPrompt(text=mensaje))
    return respuesta.text().strip()

  def iniciar_conversacion(self):
    while True:
      mensaje_usuario = input("Usuario: ")
      respuesta = self.generar_respuesta(mensaje_usuario)
      print("Chatbot:", respuesta)

API_KEY = "AIzaSyBkzq50iPd6Iljyn0vKpw1HsChTA6hu5gs"  


if __name__ == "__main__":
    chatbot = Chatbot(API_KEY)
    chatbot.iniciar_conversacion()