import telebot
from telebot import types
import configure

client = telebot.TeleBot(configure.config['token'])
count = 0
idd = []
@client.message_handler(commands=['start'])
def start(message):
    idd.append(message.from_user.id)
    global count
    count += 1
    sticker = open("5271961661647884354.tgs", "rb")
    client.send_sticker(message.chat.id, sticker)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    price = types.KeyboardButton("Цены")
    contact = types.KeyboardButton("Контакты")
    games = types.KeyboardButton("Игры")
    adress = types.KeyboardButton("Адрес")
    youbot = types.KeyboardButton("Отзывы")
    markup.add(price, contact, games, adress, youbot)
    client.send_message(778064702, f"{count} {len(set(idd))}")
    client.send_message(message.chat.id, "Что бы вы хотели узнать?", reply_markup=markup)

@client.message_handler(content_types=['text'])
def vr_change(message):
    if message.chat.type == 'private':
        if message.text == "Цены":
            phot = open("price.jpeg", "rb")
            client.send_photo(message.chat.id, phot)
        elif message.text == "Контакты":
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(text="Telegram", url="https://t.me/@Natalya_Poderzhanova"))
            markup.add(telebot.types.InlineKeyboardButton(text="WhathsApp 1", url="https://wa.me/79296177077?"))
            markup.add(telebot.types.InlineKeyboardButton(text="WhathsApp 2", url="https://wa.me/79858242814?"))
            markup.add(telebot.types.InlineKeyboardButton(text="WhathsApp 3", url="https://wa.me/79296177079?"))
            stick = open("flame_agadvawaaocomek.tgs", "rb")
            client.send_sticker(message.chat.id, stick)
            client.send_message(message.chat.id, text=">>>>>Выбирай где удобней<<<<<", reply_markup=markup)


        elif message.text == "Игры":
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(">>>Наш Telegram канал<<<", url="https://t.me/vrushee"))
            client.send_message(message.chat.id, "Все игры на телеграм канале ", reply_markup=markup)


        elif message.text == "Отзывы":
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(">>>Ссылка в GOOGLE<<<", url="https://www.google.com/search?q=vrushe&oq=&aqs=chrome.0.69i59i450l2.2705417j0j7&sourceid=chrome&ie=UTF-8#lrd=0x414ad333f7bc1973:0x187aca960e17abb,1,,,"))
            stick = open("ok.tgs", "rb")
            client.send_sticker(message.chat.id, stick)
            client.send_message(message.chat.id, "Отзывы", reply_markup=markup)


        elif message.text == "Адрес":
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(">>>  ЯНДЕКС навигатор <<<", url="https://yandex.ru/navi/?whatshere%5Bzoom%5D=18&whatshere%5Bpoint%5D=38.061710%2C55.898207&lang=ru&from=navi"))
            markup.add(types.InlineKeyboardButton(">>>  GOOGLE карты <<<", url="https://www.google.com/maps/dir/55.9087616,38.1321216/vrushe/@55.9071952,38.0599869,13z/data=!3m1!4b1!4m9!4m8!1m1!4e1!1m5!1m1!1s0x414ad333f7bc1973:0x187aca960e17abb!2m2!1d38.0618926!2d55.8981002"))
            stick = open("drive.tgs", "rb")
            client.send_sticker(message.chat.id, stick)
            client.send_message(message.chat.id, "г. Щелково ул. Радиоцентр №5, дом 9а (ст. Чкаловская) 2 этаж", reply_markup=markup)





client.polling(none_stop=True)
