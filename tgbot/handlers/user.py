from aiogram import Dispatcher
from aiogram.types import Message
from tgbot.keyboards import reply, inline

import tgbot.db as db


async def user_start(message: Message):
    rez = db.get_user(message.from_user.id)
    if rez is None: # Новый пользователь
        await message.answer('Сәлеметсіз бе, жұмысты жалғастыру үшін байланыс деректерін бөлісу керек.\n'
                             'Здравствуйте, вам нужно поделиться своими контактными данными, чтобы продолжить', reply_markup=reply.send_phone())
    else:
        await message.answer('Вход выполнен успешно!')

async def send_contact(message: Message):
    rez = db.add_user(message.contact)
    await message.answer('Құпия сөзіңізді ешкіммен бөліспеңіз. Бірінші рет кірген кезде құпия сөзді өзгертіңіз. \n'
                         'Никому не сообщайте свой пароль. Измените пароль при первом входе в систему.', reply_markup=reply.start_using())
    await message.answer('Бір реттік пароль: \n'
                         'Одноразовый пароль:')
    await message.answer(rez, reply_markup=inline.web_url())




def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(send_contact, content_types=['contact'])

