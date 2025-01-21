# Цель: научится создавать клавиатуры и кнопки на них в Telegram-bot.


# Задача "Меньше текста, больше кликов":

# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.dispatcher import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder
# import asyncio

# Необходимо дополнить код предыдущей задачи, чтобы вопросы о параметрах тела для расчёта калорий выдавались по нажатию кнопки.

# Измените massage_handler для функции set_age. Теперь этот хэндлер будет реагировать на текст 'Рассчитать', а не на 'Calories'.
# Создайте клавиатуру ReplyKeyboardMarkup и 2 кнопки KeyboardButton на ней со следующим текстом: 'Рассчитать' и 'Информация'. Сделайте так, чтобы клавиатура подстраивалась под размеры интерфейса устройства при помощи параметра resize_keyboard.
# Используйте ранее созданную клавиатуру в ответе функции start, используя параметр reply_markup.
# В итоге при команде /start у вас должна присылаться клавиатура с двумя кнопками. При нажатии на кнопку с надписью 'Рассчитать' срабатывает функция set_age 
# с которой начинается работа машины состояний для age, growth и weight.


# Пример результата выполнения программы:

# Клавиатура по команде /start:++

# После нажатия на кнопку 'Рассчитать':

from aiogram.types import Message
from aiogram import Bot, Dispatcher,F#, executor, types
from aiogram.filters import Command,CommandStart
from aiogram.fsm.state  import State, StatesGroup
from aiogram.fsm.context import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
# import config
# import logging
import sys

with open("token.txt") as f:
    TOKEN = f.read().strip()

bot = Bot(token=TOKEN)

dp = Dispatcher()


class UserState(StatesGroup):
    age= State()
    growth=State() 
    weight=State()
def main_menu(text:str|list):
    b=ReplyKeyboardBuilder()
    if isinstance(text,str):
        text=[text]
    [b.button(text=i) for i in text]
    return b.as_markup(resize_keyboard=True, one_time_keyboard=True)    

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    
    await message.answer("Привет! Я бот помогающий твоему здоровью.",reply_markup=main_menu(['Рассчитать' , 'Информация']))

@dp.message(F.text.lower().contains('рассчитать'))
async def  set_age(message: Message,state:FSMContext) -> None:
    await state.set_state(UserState.age)
    await message.answer('Введите свой возраст:')

@dp.message(UserState.age)
async def set_age(message: Message,state:FSMContext) -> None:
    if message.text.isdigit():
        await state.update_data(age=message.text)
        await state.set_state(UserState.growth)
        await message.answer('Введите свой рост:')
    else:
        await message.answer('Введите число ещё раз:')
        
# @dp.message(Command('Calories'))
# async def  set_age(message: Message,state:FSMContext) -> None:
#     await state.set_state(UserState.age)
#     await message.answer('Введите свой возраст:')

@dp.message(UserState.growth)
async def set_growth(message: Message,state:FSMContext) -> None:
    if message.text.isdigit():
        await state.update_data(growth=message.text)
        await state.set_state(UserState.weight)
        await message.answer('Введите свой вес:')
    else:
        await message.answer('Введите число ещё раз:')
        


@dp.message(UserState.weight)
async def set_weight(message: Message,state:FSMContext) -> None:
    if message.text.isdigit():
        await state.update_data(weight=message.text)
        data=await state.get_data()
        await state.clear()
        resalt=float(data['weight'])*10+float(data['growth'])*6.25-float(data['age'])*5+5
        await message.answer(f'Ваша норма каллорий: {resalt}')

    else:
        await message.answer('Введите число ещё раз:')

@dp.message()
async def echo_handler(message: Message) -> None:
    
    await message.answer("Введите команду /start, чтобы начать общение.")


async def main() -> None:
     await dp.start_polling(bot)


if __name__ == '__main__':
     asyncio.run(main())
        





