import telebot
from telebot import types
from random import randint

bot = telebot.TeleBot('')

username = ''
random_rat = 0
arr_rat = ["Серёга", "Мишаня", "Колян", "Оля", "Лиза"]
who_rat = ''

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Кто крыс?":
        rand_rat(message)
    elif "крыс?" in message.text:
        rat_question(message)

def rand_rat(message):
    random_rat = randint(0, 4)
    who_rat = arr_rat[random_rat]
    bot.send_message(message.chat.id, f"{who_rat} крыыыс")

def rat_question(message):
    random_rat = randint(0, 1)
    if random_rat == 0:
        bot.send_message(message.chat.id, "Нет")
    else:
        bot.send_message(message.chat.id, "Да")

bot.polling(none_stop=True, interval=0)