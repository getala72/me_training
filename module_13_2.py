# Цель: написать простейшего телеграм-бота, используя асинхронные функции

# Подготовка:

# Выполните все действия представленные в предыдущих видео модуля, создав и подготовив Telegram-бот для дальнейших заданий.



# Нужные версии для 13 и 14 модулей и вашего виртуального окружения находятся здесь. Если не помните, как установить необходимые библиотеки, 
# обратитесь к материалам 11 модуля.

# Актуальная версия Python для дальнейшей работы - 3.9.13.


# К коду из подготовительного видео напишите две асинхронные функции:

# start(message) - печатает строку в консоли 'Привет! Я бот помогающий твоему здоровью.' . Запускается только когда написана команда '/start' в чате с ботом. 
# (используйте соответствующий декоратор)
# all_massages(message) - печатает строку в консоли 'Введите команду /start, чтобы начать общение.'. Запускается при любом обращении не описанном ранее. 
# (используйте соответствующий декоратор)
# Запустите ваш Telegram-бот и проверьте его на работоспособность.

# Пример результата выполнения программы:

# Ввод в чат Telegram:

# Хэй!

# /start

# Вывод в консоль:

# Updates were skipped successfully.

# Введите команду /start, чтобы начать общение.

# Привет! Я бот помогающий твоему здоровью.



# Примечания:

# Для ответа на сообщение используйте декоратор message_handler.
# При отправке вашего кода на GitHub не забудьте убрать ключ для подключения к вашему боту!
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
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@dp.message()
async def echo_handler(message: Message) -> None:
    print("Введите команду /start, чтобы начать общение.")
    await message.answer("Введите команду /start, чтобы начать общение.")


async def main() -> None:
     await dp.start_polling(bot)


if __name__ == '__main__':
     asyncio.run(main())