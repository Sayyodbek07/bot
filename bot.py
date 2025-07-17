from telebot import TeleBot

token = "7700952085:AAGaAMwypyoIiBt_5-epOvzbJYqZ0Gd5d0Q"
bot = TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    print("Bot ishlashni boshladi")
    chat_id = message.chat.id
    bot.send_message(chat_id, "Assalomu aleykum mening market_botimizga xush kelibsiz")


bot.polling(non_stop=True)
