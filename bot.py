import os
import time
import telebot
from keyboard import *
from config.config import *
from localization.lang import choose_catalog

cfg = Config()
token = cfg.token
bot = telebot.TeleBot(token)

user_lang = {}


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    lang = user_lang.get(chat_id, 'uz')
    bot.send_message(chat_id, "Salom Butun jahon office ga Xush kelibsiz!\n Tilni tanlang",reply_markup=generate_language())
    bot.register_next_step_handler(message,chose_language)

def chose_language(message):
    chat_id = message.chat.id
    lang = user_lang.get(chat_id, 'uz')

    # if message.text == "🇺🇿Uz":
    #     lang = "uz"
    #     bot.send_message(chat_id, choose_catalog[lang], reply_markup=generate_main())
    # if message.text == "🇸🇦Ar":
    #     lang = "ar"
    #     bot.send_message(chat_id, choose_catalog[lang], reply_markup=generate_main())
    # if message.text == "🇬🇧En":
    #     lang = "en"
    #     bot.send_message(chat_id, choose_catalog[lang], reply_markup=generate_main())
    # if message.text == "🇩🇪Gr":
    #     lang = "gr"
    #     bot.send_message(chat_id, choose_catalog[lang], reply_markup=generate_main())
    # if message.text == "🇫🇷Fr":
    #     lang = "fr"
    #     bot.send_message(chat_id, choose_catalog[lang], reply_markup=generate_main())


    user_lang[chat_id] = lang
    bot.send_message(chat_id, 'Quyidagilardan birini tanlang!', reply_markup=generate_main())
    bot.register_next_step_handler(message, main_catalog)

def main_catalog(message):
    chat_id = message.chat.id
    lang = user_lang.get(chat_id, 'uz')

    if message.text == "🎯 Biz haqimizda":
        photo = open('media/Missiya va Vizyon.png','rb')
        bot.send_photo(chat_id, photo,
                       caption="\n<b>Missiya:</b> Biz yosh avlodga global imkoniyatlar yaratish orqali ularning shaxsiy va kasbiy rivojlanishiga hissa qo‘shishni maqsad qilganmiz."
                               '\n<b>Vizyon:</b> Yoshlarning ta’lim, tadbirkorlik va ko‘ngillilik yo‘nalishlaridagi imkoniyatlarini kengaytirib, kelajakda muvaffaqiyatli yetakchilarni tarbiyalash.\n\n',
                       parse_mode="HTML")
        time.sleep(1)
        photo_2 = open('media/team.png','br')
        bot.send_photo(chat_id, photo_2,
                       caption="\nBizning jamoamiz xalqaro tajribaga ega, faol va iqtidorli yoshlar, tadbirkorlar hamda yetakchilardan iborat. Har bir jamoa a’zosi yoshlar o‘rtasida global hamkorlikni mustahkamlash va yangi imkoniyatlar yaratishda muhim rol o‘ynaydi.")
        time.sleep(1)
        photo_3 = open('media/history.png','rb')
        bot.send_photo(chat_id, photo_3, caption='\nTashkilotimiz 2000-yillarning boshida yoshlar almashinuvi dasturlarini rivojlantirish va yosh avlodga xalqaro miqyosda yangi imkoniyatlar yaratish maqsadida tashkil topgan. Bugungi kunda, biz minglab yoshlarni global platformalarda muvaffaqiyatli ishtirok etishlariga ko‘maklashib kelmoqdamiz.',
                       reply_markup=generate_back())
        bot.register_next_step_handler(message, back)

    elif message.text == "💬 Biz bilan bog‘laning":
        bot.send_message(chat_id,"<b>Aloqa ma’lumotlari ga bossa quyidagi ma’lumotlar</b>\n\n"
                                       "<b>Eelefon raqamlari:</b> +998991234567\n"
                                       "<b>Elektron pochta:</b> example@gmail.com\n"
                                       "<b>Manzillari:</b> Nil bo’yi\n"
                                       "<b>Ofis vaqtlari:</b> 09:00 – 18:00",parse_mode='HTML',reply_markup=generate_connect())
        bot.register_next_step_handler(message, connect)


    elif message.text == "🌐 Ijtimoiy tarmoqlar":
        photo_social_networks = open("media/team.png","rb")
        bot.send_photo(chat_id, photo_social_networks,'\n🌐 Ijtimoiy tarmoqlar bo‘limi',reply_markup=generate_media())




    elif message.text == "📑 Yangiliklar va E'lonlar":
        bot.send_message(chat_id, "Prafilaktika ishlari olib borilmoqda!")
        time.sleep(2)
        bot.send_message(chat_id, 'Quyidagilardan birini tanlang!', reply_markup=generate_main())
        bot.register_next_step_handler(message, main_catalog)

    elif message.text == "📊 Yoshlar uchun resurslar":
        bot.send_message(chat_id,'📊Yoshlar uchun resurslar bo‘limi', reply_markup=generate_resource())
        bot.register_next_step_handler(message, teen_resource_group)

    elif message.text == "🏆 Musobaqalar":
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Bizning siyrat chellange ga qatnashish 👇', reply_markup=generate_tourment())



    elif message.text == "Tilni o'zgartirish":
        bot.send_message(chat_id, "Tilni tanlang!",reply_markup=generate_language())
        bot.register_next_step_handler(message, chose_language)


@bot.callback_query_handler(func=lambda call: call.data == 'back')
def call_back(call):
    chat_id = call.message.chat.id
    lang = user_lang.get(chat_id, 'uz')
    if call.data :
        return chose_language(call.message)

@bot.callback_query_handler(func=lambda call: call.data == 'siyrat')
def siyrat_tour(call):
    chat_id = call.message.chat.id
    lang = user_lang.get(chat_id, 'uz')
    bot.send_message(chat_id, 'Savolni yuboring!')
    bot.register_next_step_handler(call.message, siyrat_tour_send)


def siyrat_tour_send(message):
    chat_id = message.chat.id
    lang = user_lang.get(chat_id, 'uz')
    user_name = message.from_user.first_name
    bot.send_message(chat_id, 'Savol qabul qilindi !')
    bot.send_message(chat_id, f' @{user_name}\n\n Yozdi: {message.text}')
    time.sleep(2)
    bot.send_message(chat_id, 'Quyidagilardan birini tanlang!', reply_markup=generate_main())
    bot.register_next_step_handler(message, main_catalog)


def teen_resource_group(message):
    chat_id = message.chat.id
    lang = user_lang.get(chat_id, 'uz')
    if message.text == 'Ta’lim materiallari':
        bot.send_message(chat_id, message.text)
        bot.register_next_step_handler(message, teen_resource_group)

    elif message.text == 'Yoshlar mentorlari dasturi':
        bot.send_message(chat_id, message.text)
        bot.register_next_step_handler(message, teen_resource_group)

    elif message.text == 'Kasbiy yo‘naltirish':
        bot.send_message(chat_id, message.text)
        bot.register_next_step_handler(message, teen_resource_group)

    return back(message)


def connect_back(message):
    chat_id = message.chat.id
    lang = user_lang.get(chat_id, 'uz')
    bot.send_message(chat_id, "<b>Aloqa ma’lumotlari ga bossa quyidagi ma’lumotlar</b>\n\n"
                              "<b>Eelefon raqamlari:</b> +998991234567\n"
                              "<b>Elektron pochta:</b> example@gmail.com\n"
                              "<b>Manzillari:</b> Nil bo’yi\n"
                              "<b>Ofis vaqtlari:</b> 09:00 – 18:00", parse_mode='HTML', reply_markup=generate_connect())
    bot.register_next_step_handler(message, connect)
def back(message):
    chat_id = message.chat.id
    lang = user_lang.get(chat_id, 'uz')
    if message.text == "🔙Orqaga":
        return chose_language(message)
    return f'Method back do not work!!'

def connect(message):
    chat_id = message.chat.id
    lang = user_lang.get(chat_id, 'uz')
    if message.text == "📝Savol/Taklif":
        bot.send_message(chat_id, 'F.I.O ni yuboring!: ')
        bot.register_next_step_handler(message, user_email)

    elif message.text == "📍Geolokatsiya":
        bot.send_message(chat_id, 'Bizning geolokatsiya !')
        bot.send_location(chat_id, latitude=40.86091, longitude=69.58965, reply_markup=generate_back())
        bot.register_next_step_handler(message, connect_back)

    elif message.text == "🔙Orqaga":
        return back(message)

def user_email(message):
    chat_id = message.chat.id
    lang = user_lang.get(chat_id, 'uz')
    fio = message.text
    bot.send_message(chat_id, 'Elektron pochtani yuboring: ')
    bot.register_next_step_handler(message,user_ask, fio)

def user_ask(message, fio):
    chat_id = message.chat.id
    lang = user_lang.get(chat_id, 'uz')
    email = message.text
    if "@" in email:
        bot.send_message(chat_id, 'Savol/Taklifingiz yuboring: ')
        bot.register_next_step_handler(message, user_phone, fio, email)
    else:
        bot.send_message(chat_id, 'Elektron pochta xato! \nBoshqatdan kiriting!: ')
        time.sleep(1)
        bot.send_message(chat_id, 'Elektron pochtani yuboring: ')
        bot.register_next_step_handler(message,user_ask, fio)
def user_phone(message, fio, email):
    chat_id = message.chat.id
    lang = user_lang.get(chat_id, 'uz')
    ask = message.text
    bot.send_message(chat_id, 'Telefon raqamingizni yuboring!: ', reply_markup=generate_contact())
    bot.register_next_step_handler(message, permission_group, fio, email, ask)

def permission_group(message, fio, email, ask):
    chat_id = message.chat.id
    lang = user_lang.get(chat_id, 'uz')
    if message.text:
        phone = message.text
        bot.send_message(chat_id,f'Tasdiqlaysizmi!\n\nF.I.O: {fio}\n'
                                 f'Elektron pochtangiz: {email}\n'
                                  f'Savol/Taklifingiz: {ask}\n'
                                  f'Tel raqamingiz: {phone}',reply_markup=generate_commit())
        bot.register_next_step_handler(message,send_group, fio, email, ask, phone)
    elif message.contact:
        phone = message.contact.phone_number
        bot.send_message(chat_id, f'Tasdiqlaysizmi!\n\nF.I.O: {fio}\n'
                                  f'Elektron pochtangiz: {email}\n'
                                  f'Savol/Taklifingiz: {ask}\n'
                                  f'Tel raqamingiz: {phone}', reply_markup=generate_commit())
        bot.register_next_step_handler(message, send_group, fio, email, ask, phone)

def send_group(message, fio, email, ask, phone):
    chat_id = message.chat.id
    lang = user_lang.get(chat_id, 'uz')
    if message.text == "Ha":
        bot.send_message(chat_id, 'Malumotlar qabul qilindi!')
        bot.send_message(cfg.channel_id, f'Tasdiqlaysizmi!\n\nF.I.O: {fio}\n'
                                              f'Elektron pochtangiz: {email}\n'
                                              f'Savol/Taklifingiz: {ask}\n'
                                              f'Tel raqamingiz: {phone}')
        time.sleep(2)
        bot.send_message(chat_id, 'Quyidagilardan birini tanlang!', reply_markup=generate_main())
        bot.register_next_step_handler(message, main_catalog)

    elif message.text == "Yoq":
        bot.send_message(chat_id, "<b>Aloqa ma’lumotlari ga bossa quyidagi ma’lumotlar</b>\n\n"
                                  "<b>Eelefon raqamlari:</b> +998991234567\n"
                                  "<b>Elektron pochta:</b> example@gmail.com\n"
                                  "<b>Manzillari:</b> Nil bo’yi\n"
                                  "<b>Ofis vaqtlari:</b> 09:00 – 18:00", parse_mode='HTML',
                         reply_markup=generate_connect())
        bot.register_next_step_handler(message, connect)


bot.polling(non_stop=True)

