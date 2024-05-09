import textwrap
import google.generativeai as genai
from IPython.display import Markdown


class ChatBot:
    def __init__(self):
        self.GOOGLE_API_KEY = "AIzaSyBkzq50iPd6Iljyn0vKpw1HsChTA6hu5gs"
        genai.configure(api_key=self.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel("gemini-pro")
        self.chat = self.model.start_chat(history=[])

    def to_markdown(self, text):
        text = text.replace("•", "  *")
        return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))

    def preguntar(self, pregunta):
        response = self.chat.send_message(pregunta, stream=True)
        for chunk in response:
            return chunk.text


    def iniciar(self):
        while True:
            message = input("Usuario: ")
            response = self.chat.send_message(message, stream=True)
            print("AI:", end=" ")
            for chunk in response:
                print(chunk.text)


if __name__ == "__main__":
    chat_bot = ChatBot()
    chat_bot.iniciar()
