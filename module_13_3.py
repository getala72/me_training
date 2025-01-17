# Цель: написать простейшего телеграмм-бота, используя асинхронные функции.

import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
# from aiogram.utils import executor

with open("token.txt") as f:
    TOKEN = f.read().strip()

bot = Bot(token=TOKEN)


dp = Dispatcher()
@dp.message(Command('start'))
async def command_start_handler(message: Message) -> None:
    
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@dp.message()
async def echo_handler(message: Message) -> None:
    
    await message.answer("Введите команду /start, чтобы начать общение.")


async def main() -> None:
     await dp.start_polling(bot)


if __name__ == '__main__':
     asyncio.run(main())
# Измените функции start и all_messages так, чтобы вместо вывода в консоль строки отправлялись в чате телеграм.

# Запустите ваш Telegram-бот и проверьте его на работоспособность.

# Пример результата выполнения программы:


# Примечания:

# Для ответа на сообщение запускайте метод answer асинхронно.
# При отправке вашего кода на GitHub не забудьте убрать ключ для подключения к вашему боту!
