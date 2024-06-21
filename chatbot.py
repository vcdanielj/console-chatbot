import textwrap
import google.generativeai as genai
import dotenv
import os
from IPython.display import Markdown
dotenv.load_dotenv()

class ChatBot:
    def __init__(self):
        self.GOOGLE_API_KEY = os.getenv("API_KEY")
        genai.configure(api_key=self.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel("gemini-pro")
        self.chat = self.model.start_chat(history=[])

    def to_markdown(self, text):
        text = text.replace("•", "  *")
        return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))

    def preguntar(self, pregunta):
        respuesta = self.chat.send_message(pregunta, stream=True)
        acum = ""
        for chunk in respuesta:
            acum += chunk.text
        return acum


    def iniciar(self):
        try:
            while True:
                message = input("Usuario: ")
                response = self.chat.send_message(message, stream=True)
                print("AI:", end=" ")
                for chunk in response:
                    print(chunk.text)
        
        except KeyboardInterrupt:
            print("Saliendo...")
            exit()


if __name__ == "__main__":
    chat_bot = ChatBot()
    chat_bot.iniciar()
