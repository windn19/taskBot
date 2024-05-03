import telebot
from telebot.types import Message

from models import Task
from settings import telegram_token


bot = telebot.TeleBot(telegram_token)


@bot.message_handler(commands=['help', 'start'])
def start_bot(message: Message):
    bot.send_message(message.from_user.id, 'Начало работы!')


@bot.message_handler(commands=['add'])
def create_task(message: Message):
    text = message.text[4:].strip().split(maxsplit=1)
    if len(text) == 1:
        text.append(' ')
    if text:
        task = Task.create(title=text[0], describe=text[1])
        text = f'Создано новое' + str(task)
    else:
        text = 'Задание не создано - нет заголовка!'
    bot.send_message(message.from_user.id, text)


@bot.message_handler(commands=['tsk'])
def list_tasks(message: Message):
    for task in Task.select():
        bot.send_message(message.from_user.id, task.created_date.strftime('%d/%m/%Y %H:%M -> ') + str(task))


@bot.message_handler(content_types=['text'])
def get_echo(message: Message):
    bot.send_message(message.from_user.id, message.text.upper())


bot.infinity_polling()
