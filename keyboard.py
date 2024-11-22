from telebot import types


def generate_language():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_uz = types.KeyboardButton(text="🇺🇿Uz")
    btn_ar = types.KeyboardButton(text="🇸🇦Ar")
    btn_en = types.KeyboardButton(text="🇬🇧En")
    btn_gr = types.KeyboardButton(text='🇩🇪Gr')
    btn_fr = types.KeyboardButton(text='🇫🇷Fr')
    keyboard.row(btn_uz, btn_ar, btn_en, btn_gr, btn_fr)
    return keyboard

def generate_main():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_about = types.KeyboardButton(text="🎯 Biz haqimizda")
    btn_connect = types.KeyboardButton(text="💬 Biz bilan bog‘laning")
    btn_social = types.KeyboardButton(text="🌐 Ijtimoiy tarmoqlar")
    btn_news = types.KeyboardButton(text="📑 Yangiliklar va E'lonlar")
    btn_idea = types.KeyboardButton(text="📊 Yoshlar uchun resurslar")
    btn_data = types.KeyboardButton(text="🏆 Musobaqalar")
    btn_back = types.KeyboardButton(text="Tilni o'zgartirish")
    keyboard.row(btn_about, btn_connect)
    keyboard.row(btn_social, btn_news)
    keyboard.row(btn_idea, btn_data)
    keyboard.row(btn_back)
    return keyboard

def generate_back():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn = types.KeyboardButton(text="🔙Orqaga")
    keyboard.row(btn)
    return keyboard

def generate_connect():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_question = types.KeyboardButton(text="F.I.O")
    btn_question = types.KeyboardButton(text="📝Savol/Taklif")
    btn_location = types.KeyboardButton(text="📍Geolokatsiya")
    btn_back = types.KeyboardButton(text="🔙Orqaga")
    keyboard.row(btn_question, btn_location)
    keyboard.row(btn_back)
    return keyboard


def generate_commit():
    keyboad = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    btn_yes = types.KeyboardButton(text='Ha')
    btn_no = types.KeyboardButton(text='Yoq')
    keyboad.row(btn_yes, btn_no)
    return keyboad


def generate_media():
    keyboard = types.InlineKeyboardMarkup()
    btn_facebok = types.InlineKeyboardButton(text='Facebook',url="https://www.facebook.com/")
    btn_insta = types.InlineKeyboardButton(text='Instagram',url="https://www.instagram.com/")
    btn_twit = types.InlineKeyboardButton(text='Twitter',url="https://x.com/")
    btn_youtube = types.InlineKeyboardButton(text='YouTube',url="https://www.youtube.com/")
    btn_back = types.InlineKeyboardButton(text="🔙Orqaga",callback_data='back')
    keyboard.row(btn_facebok, btn_insta)
    keyboard.row(btn_twit, btn_youtube)
    keyboard.row(btn_back)
    return keyboard

def generate_resource():
    keyboad = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    btn_material = types.KeyboardButton(text='Ta’lim materiallari')
    btn_path = types.KeyboardButton(text='Kasbiy yo‘naltirish')
    btn_mentor = types.KeyboardButton(text='Yoshlar mentorlari dasturi')
    btn_back = types.KeyboardButton(text="🔙Orqaga",)
    keyboad.row(btn_material, btn_path, btn_mentor)
    keyboad.row(btn_back)
    return keyboad

def generate_contact():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn = types.KeyboardButton(text='Kontakt yuborish', request_contact=True)
    keyboard.row(btn)
    return keyboard


def generate_tourment():
    keyboard = types.InlineKeyboardMarkup()
    btn_syrat = types.InlineKeyboardButton(text='Siyrat chellange!', callback_data='siyrat')
    btn_back = types.InlineKeyboardButton(text="🔙Orqaga", callback_data='back')
    keyboard.row(btn_syrat)
    keyboard.row(btn_back)
    return keyboard

# def generate_tourment_send():
#     keyboad = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
#     btn_material = types.KeyboardButton(text='Ta’lim materiallari')
