import telebot
from telebot import types
from glob import glob
from random import choice


bot = telebot.TeleBot('5684735320:AAHi3mP_4HsG_9Pax9QIizfNaruea_67T_8', threaded=False)

def im(message, markup):
    lists = glob("/home/WolleBot1234/images/*")
    picture = choice(lists)
    bot.send_photo(message.chat.id, photo=open(picture, 'rb'), caption = "Поделитесь этой карточкой с друзьями, если вам откликнулось предсказание!", reply_markup=markup)
    lists.remove(picture)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
    button2 = types.KeyboardButton("Получить карточку с ответом")
    markup.add(button2)
    mess = f'Привет, {message.from_user.first_name}! Подумайте о том, что сейчас вас волнует. Сконцентрируйтесь на вопросе и жмите на кнопку.'
    bot.send_message(message.chat.id, mess, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Получить карточку с ответом":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
        button1 = types.KeyboardButton("Получить еще одну карточку")
        button2 = types.KeyboardButton("Записаться на Лабораторию")
        button3 = types.KeyboardButton("Что такое Лаборатория Wolle?")
        markup1.add(button1, button2, button3)

        im(message, markup1)

    elif(message.text == "Что такое Лаборатория Wolle?"):
        bot.send_message(message.chat.id, text="Wolle – это сервис митап-лабораторий, направленных на поиск решений в сложных профессиональных и личных ситуациях. Вместе с профессиональными психологами наши участники в онлайн и офлайн-формате разбирают глубинные причины проблем, обсуждают свои кейсы и вырабатывают новые подходы и решения.")
        bot.send_message(message.chat.id, text="Но Wolle – это не только про решение. Это прежде всего про комьюнити, которое, меняясь само, меняет мир.")
        content = [types.InputMediaPhoto(open('/home/WolleBot1234/'+str(i)+'.jpg', 'rb')) for i in range(1, 5)]
        bot.send_media_group(message.chat.id, content)
        bot.send_message(message.chat.id, text="Мы создали Wolle, потому что знаем сами, как здорово, когда рядом есть эксперты и поддерживающее комьюнити, которые могут не просто подсказать, как действовать, но и поддержать и поделиться общей заряженностью.")

    elif(message.text == "Получить еще одну карточку"):
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
        button1 = types.KeyboardButton("Записаться на Лабораторию")
        button2 = types.KeyboardButton("Что такое Лаборатория Wolle?")
        markup2.add(button1, button2)

        im(message, markup2)
        bot.send_message(message.chat.id, text="Мы надеемся, что это было полезно - если вы хотите изучить и решить вашу проблему на более глубоком уровне, приходите на наши Лаборатории", reply_markup=markup2)

    elif message.text == "Записаться на Лабораторию":
        bot.send_message(message.chat.id, text="Чтобы записаться на Лабораторию, просто оставьте заявку на нашем сайте!\nhttps://wollelab.ru/#price")
    elif 'карточка' in message.text:
        bot.send_message(message.chat.id, text="К сожалению лимит карточек исчерпан :(\nПриходи на лабораторию и получи свою персональную карточку-предсказание!")
    else:
        bot.send_message(message.chat.id, text="Ой, произошли технические шоколадки, кажется, нет такой команды.")

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)
#bot.infinity_polling()