import telebot
import gtts
from telebot import types
from gtts import gTTS

bot = telebot.TeleBot('7364950157:AAGROPIv4C8qvVbmZC1C02iNcE7wtZW3lR8')

#Основные команды бота

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,'Здравствуйте! Добро пожаловать!')

@bot.message_handler(commands=['fullinfo'])
def main(message):
    bot.send_message(message.chat.id, message)

#Перевод текста в речь

@bot.message_handler(commands=['speech'])
def main(message):
    bot.send_message(message.chat.id, 'Введите текст')
    bot.register_next_step_handler(message, text)

def text(message):
    tts=gTTS(message.text, lang='ru')
    tts.save(f'{message.from_user.id}.mp3')
    bot.send_voice(message.chat.id, open(f"{message.from_user.id}.mp3", 'rb'))

bot.polling(non_stop=True)