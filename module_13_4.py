# Задача "Цепочка вопросов":

# Необходимо сделать цепочку обработки состояний для нахождения нормы калорий для человека.

# Группа состояний:
from aiogram.types import Message
from aiogram import Bot, Dispatcher#, executor, types
from aiogram.filters import Command,CommandStart
from aiogram.fsm.state  import State, StatesGroup

# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# Импорт классов State и StatesGroup из aiogram.dispatcher.filters.state.
import asyncio
# import config
# import logging
import sys

with open("token.txt") as f:
    TOKEN = f.read().strip()

bot = Bot(token=TOKEN)


dp = Dispatcher()


# Импортируйте классы State и StateGroup из aiogram.dispatcher.filters.state.
# Создайте класс UserState наследованный от StateGroup.

class UserState(StatesGroup):
    age= State()
    growth=State() 
    weight=State()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@dp.message(Command('Calories'))
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
        







