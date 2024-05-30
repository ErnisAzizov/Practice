import telebot
import gtts
from telebot import types
from gtts import gTTS

bot = telebot.TeleBot('')

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
    elif message.text.strip()!= '' and message.text.replace('.', '', 1).strip()!= '':
        tts=gTTS(message.text, lang='ru')
        tts.save(f'{message.from_user.id}.mp3')
        bot.send_voice(message.chat.id, open(f"{message.from_user.id}.mp3", 'rb'))
    else:
        bot.send_message(message.chat.id, 'Произошла ошибка!')
        
bot.polling(non_stop=True)


#Символы — . , () [] : ; ! ?  не вводятся по отдельности

#Символы ₽ · • ♪ § ¢ ✓ вводятся, но не воспроизводятся

#На гифки и стикеры никак не реагирует

#Озвучивает каждый эмодзи