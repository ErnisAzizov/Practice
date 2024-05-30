import telebot
import gtts
from telebot import types
from gtts import gTTS

bot = telebot.TeleBot('7364950157:AAGROPIv4C8qvVbmZC1C02iNcE7wtZW3lR8')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,'Здравствуйте! Добро пожаловать!')

# Перевод текста в речь

user_states = {}

@bot.message_handler(commands=['speech'])
def main(message):
    bot.send_message(message.chat.id, 'Введите текст')
    user_states[message.chat.id] = 'Ожидание'

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'Ожидание')
def text(message):
    if message.text.lower() == '/stop':
        bot.send_message(message.chat.id, 'Процесс приостановлен')
        user_states[message.chat.id] = None
    else:
        tts=gTTS(message.text, lang='ru')
        tts.save(f'{message.from_user.id}.mp3')
        bot.send_voice(message.chat.id, open(f"{message.from_user.id}.mp3", 'rb'))

bot.polling(non_stop=True)