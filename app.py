import telebot
from extensions import APIException, Convertor
from config import TOKEN, keys
import traceback

keys = {
    'Доллар': 'USD',
    'Евро': 'EUR',
    'Рубль': 'RUB'
}
TOKEN = "6421097476:AAEERis_PGzT3kxHd3KOS1GuzUV4w61md5M"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = "Посмотреть список валют: /values\nЧтобы узнать курс введите:\n<валюта, которую переводим> <валюта, в которую переводим> <количество переводимой валюты>"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in keys.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise APIException('Слишком много параметров!')
        quote, base, amount = values
        total_base = Convertor.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}" )
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"Неизвестная ошибка:\n{e}" )
    else:
        bot.reply_to(message,answer)

bot.polling(none_stop=True)
