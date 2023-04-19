from aiogram import Dispatcher
from aiogram.types import Message

import tgbot.db as db


async def user_start(message: Message):
    if db.get_user(message.from_user.id) is None:
        await message.answer('Сәлеметсіз бе, жұмысты жалғастыру үшін байланыс деректерін бөлісу керек./Здравствуйте, вам нужно поделиться своими контактными данными, чтобы продолжить')
        await message.reply("Hello, user!")


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
