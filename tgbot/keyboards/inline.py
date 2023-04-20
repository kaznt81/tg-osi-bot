from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def web_url():
    return InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton('Перейти на сайт', url='https://ots.kommunal.kz/ords/f?p=101'))