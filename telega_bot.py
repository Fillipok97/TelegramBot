import telebot
from extensions import APIException, ConvertValue
from tokenfile import TOKEN, keys
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def helpme(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду в следующем формате: \n <имя валюты цену которой надо узнать> <имя валюты в которой надо узнать цену первой валюты> <количество первой валюты> \n Список всех доступных валют - /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try:
        valli = message.text.split(' ')

        if len(valli) != 3:
            raise APIException('Неверное количество параметров.')

        base, quote, amount = valli
        total = ConvertValue.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n {e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду.\n {e}')
    else:
        text = f'Цена {amount} {base} в {quote} - {total}'
        bot.send_message(message.chat.id, text)

bot.polling()