import telebot
from telebot import types

bot = telebot.TeleBot('6908849803:AAGfduKWcaZWUikUaRDcCFx8p_gxWiEKOiQ')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Добрый вечер")


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "1":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("2")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)
    elif message.text == "Кнопка 2":
        bot.send_message(message.chat.id, 'https://habr.com/ru/articles/580408/')


bot.polling()