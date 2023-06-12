from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def send_phone(status=True):
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Бөлісу/Поделиться', request_contact=True))

def start_using():
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Начать пользоваться')).add(KeyboardButton('Запросить новый пароль'))