import telebot
from chatbot import ChatBot

TOKEN = '7136318826:AAHjrFBK11UoEmmCwQ3OdW3GZvCuijPRmaU'

bot = telebot.TeleBot(TOKEN)
chatbot = ChatBot()
@bot.message_handler(commands=['start', 'help'])
def saludar(mensaje):
    bot.reply_to(mensaje, "Hola, soy un Bot de Telegram, ¿en que te puedo ayudar?")

@bot.message_handler(func=lambda mensaje: True)
def responder(mensaje):
    try:
        bot.reply_to(mensaje, chatbot.preguntar(mensaje.text))
    except Exception:
        responder(mensaje)

if __name__ == "__main__":
    bot.polling(non_stop=True)
    chatbot = ChatBot()