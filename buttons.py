import telebot
from telebot import types
import time
bot = telebot.TeleBot('TOKEN')
prise = 50
lupik_id = 847720158

@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == 'private':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('📲Подключить кнопки')
        item2 = types.KeyboardButton('🧾Примеры')
        item3 = types.KeyboardButton('💬Отзывы')
        markup.add(item1).row(item2, item3)

        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\n'
                                          f'Я - бот, способный подключить кнопки в твою беседу абсолютно любого типа.\n'
                                          f'Размер, количество, текст - все по твоему усмотрению.\n'
                                          f'Цена за кнопки - <b> {prise}₽ </b>\n'
                                          f'Если хочешь посмотреть, как это работает, то добавь меня в беседу и напиши команду:\n <code>/buttons_test@ButtonsLikeYouWant_bot</code>',  parse_mode='HTML', reply_markup = markup)

@bot.message_handler(commands=['back'])
def back(message):
    markup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, 'Кнопки удалены.', reply_markup = markup)

@bot.message_handler(commands=['buttons_test'])
def test(message):
    if message.chat.type != 'private':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('@ButtonsLikeYouWant_bot')
        item2 = types.KeyboardButton('Тест1')
        item3 = types.KeyboardButton('Тест2')
        markup.add(item1).row(item2, item3)

        bot.send_message(message.chat.id, 'Тестовые кнопки подключены!', reply_markup = markup)
        bot.send_message(message.chat.id, 'До конца тестового периода осталось <b>2 минут</b>', parse_mode='HTML')

        time.sleep(120)

        markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Тестовый период закончен.\nКнопки удалены.', reply_markup=markup)

@bot.message_handler(commands=['buttons1'])
def buttons1(message):
    if message.from_user.id == lupik_id:
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('Профиль')
        item2 = types.KeyboardButton('Казино 1')
        item3 = types.KeyboardButton('Казино все')
        markup.add(item1, item2, item3)

        bot.send_message(message.chat.id, 'Кнопки подключены!', reply_markup = markup)
    else:
        stick = open('sticker.webm', 'rb')
        bot.send_sticker(message.chat.id, stick)
@bot.message_handler(commands=['buttons2'])
def buttons2(message):
    if message.from_user.id == lupik_id:
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('Правда')
        item2 = types.KeyboardButton('Действие')
        item3 = types.KeyboardButton('@ButtonsLikeYouWant_bot')
        markup.add(item1, item2).row(item3)

        bot.send_message(message.chat.id, 'Кнопки подключены!', reply_markup = markup)
    else:
        stick = open('sticker.webm', 'rb')
        bot.send_sticker(message.chat.id, stick)

@bot.message_handler(content_types=['text', 'photo', 'document'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '📲Подключить кнопки':
            bot.send_message(message.chat.id,'Итак, ты решился подключить кнопки и уже наверняка знаешь, какие именно кнопки ты хочешь?\n'
                                             'Отлично!\n'
                                             'Ответь сообщением ниже на такую форму:\n'
                                             '1. Ссылка на беседу в которую нужно будет добавить кнопки\n'
                                             '2. Сами кнопки, какие хочешь сделать. В формате:\n'
                                             '<code>кнопка1 кнопка2\n'
                                             'кнопка3 кнопка4</code>\n'
                                             '(количество кнопок в строчку и столбик ограничено лишь вашим желанием)', parse_mode='HTML')
        elif message.text == '🧾Примеры':
            photo1 = open('test.png', 'rb')
            photo2 = open('leysa.png', 'rb')
            photo3 = open('mafia.png', 'rb')
            bot.send_photo(message.chat.id, photo1, caption='Тестовые кнопки\n'
                                                            'P.s. <code>/buttons_test@ButtonsLikeYouWant_bot</code> в беседу с этим ботом)', parse_mode='HTML')
            bot.send_photo(message.chat.id, photo2, caption='Пример кнопок для игрового бота Леся')
            bot.send_photo(message.chat.id, photo3, caption='Пример для Мафии')
        elif message.text == '💬Отзывы':
            bot.send_message(message.chat.id, 'Отзывы можешь посмотреть [тут](https://t.me/ButtonsReviews)', parse_mode='Markdown')
        elif 't.me' in message.text:
            bot.send_message(lupik_id, f'Имя - {message.from_user.first_name}')
            bot.forward_message(lupik_id, message.chat.id, message.message_id)
            bot.send_message(message.chat.id,'Супер. Осталось только оплатить\n'
                                             f'Перейди по этой [ссылке](https://www.tbank.ru/bank_pay_link), оплати {prise}₽ и укажи в комментарие свой никнейм в ТГ (не id)\n'
                                              'В течение дня, я обязательно зайду в чат и добавлю кнопки. Если будут вопросы - пиши @lupiktg', parse_mode='Markdown')

bot.polling(none_stop=True, interval=0)
