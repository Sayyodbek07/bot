from telebot import TeleBot
from keyboards import *

token = "7700952085:AAGaAMwypyoIiBt_5-epOvzbJYqZ0Gd5d0Q"
bot = TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    print("Bot ishlashni boshladi")
    chat_id = message.chat.id
    bot.send_message(chat_id, "Assalomu aleykum online_market botimizga xush kelibsiz. tilni tanlang", reply_markup=general_languange())

def phone_number(message):
     name = message.text
     chat_id = message.chat.id
     bot.send_message(chat_id, "Telefon raqamingizni kiriting")
     bot.register_next_step_handler(message,)


