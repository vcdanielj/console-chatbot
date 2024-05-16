import telebot
import dotenv
import os
from chatbot import ChatBot

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)
chatbot = ChatBot()
@bot.message_handler(commands=['start', 'help'])
def saludar(mensaje):
    bot.reply_to(mensaje, "Hola, soy un Bot de Telegram, ¿en que te puedo ayudar?")

@bot.message_handler(func=lambda mensaje: True)
def responder(mensaje):
    try:
        bot.reply_to(mensaje, chatbot.preguntar(mensaje.text))
    except Exception as e:
        manejar_error(e)

def manejar_error():
    bot.send_message("Lo siento, hubo un problema al procesar tu mensaje.")

if __name__ == "__main__":
    bot.polling(non_stop=True)
    chatbot = ChatBot()