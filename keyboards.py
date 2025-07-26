from telebot import types

def general_languange():
    keyboars = types.InlineKeyboardMarkup()
    uzbek = types.InlineKeyboardButton(text="yes")
    rus = types.InlineKeyboardButton()
    ingiliz = types.InlineKeyboardButton()
    keyboars.row(uzbek, rus, ingiliz)
    return keyboars

def general_menu():
    keyboards = types.ReplyKeyboardMarkup()
    computers = types.KeyboardButton("Computers")
    tv = types.KeyboardButton("Television")
    monitors = types.KeyboardButton("Printers")
    back = types.KeyboardButton("orqaga")
    keyboards.row(computers)
    keyboards.row(tv)
    keyboards.row(monitors)
    keyboards.row(back)
    return keyboards