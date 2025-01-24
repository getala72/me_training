# Задача "Ещё больше выбора":


# from aiogram import Bot, Dispatcher, executor
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# # Импорт классов InlineKeyboardMarkup, InlineKeyboardButton  из aiogram.types

# import config


from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder
from aiogram.types import Message,CallbackQuery
from aiogram import Bot, Dispatcher,F#, executor, types
from aiogram.filters import Command,CommandStart
from aiogram.fsm.state  import State, StatesGroup
from aiogram.fsm.context import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

import sys

with open("token.txt") as f:
    TOKEN = f.read().strip()

bot = Bot(token=TOKEN)

dp = Dispatcher()


class UserState(StatesGroup):
    age= State()
    growth=State() 
    weight=State()
def kb_menu(text:str|list):
    b=ReplyKeyboardBuilder()
    if isinstance(text,str):
        text=[text]
    [b.button(text=i) for i in text]
    return b.as_markup(resize_keyboard=True, one_time_keyboard=True)
    
def kb_inline_menu(text:str|list):
    b=InlineKeyboardBuilder()
    if isinstance(text,str):
        text=[text]
    [b.button(text=i,callback_data=i) for i in text]
    return b.as_markup(resize_keyboard=True)
    
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    
    await message.answer("Привет! Я бот помогающий твоему здоровью.",reply_markup=kb_menu(['Рассчитать' , 'Информация']))

@dp.message(F.text.lower()=='рассчитать')
async def  main_menu(message: Message) -> None:
    await message.answer('Выберите опцию:',reply_markup=kb_inline_menu(['Рассчитать норму каллорий' , 'Формулы расчёта']))

@dp.callback_query(F.data=='Формулы расчёта')
async def callback_query_hand(callback:CallbackQuery) -> None:

   await callback.message.answer('10 x вес (кг) + 6.25 x рост (см) - 5 x возраст (r) - 161') 
   await callback.answer()

@dp.callback_query(F.data=='Рассчитать норму каллорий')
async def start_hand(callback:CallbackQuery,state:FSMContext) -> None:
   await state.set_state(UserState.age)
   await callback.answer('Введите свой возраст:')
   await callback.answer()

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
        resalt=float(data['weight'])*10+float(data['growth'])*6.25-float(data['age'])*5-161 
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
        
# Необходимо дополнить код предыдущей задачи, чтобы при нажатии на кнопку 'Рассчитать' присылалась Inline-клавиатруа.

# Создайте клавиатуру InlineKeyboardMarkup с 2 кнопками InlineKeyboardButton:

# С текстом 'Рассчитать норму калорий' и callback_data='calories'
# С текстом 'Формулы расчёта' и callback_data='formulas'
# Создайте новую функцию main_menu(message), которая:

# Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Рассчитать'.
# Сама функция будет присылать ранее созданное Inline меню и текст 'Выберите опцию:'
# Создайте новую функцию get_formulas(call), которая:

# Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
# Будет присылать сообщение с формулой Миффлина-Сан Жеора.
# Измените функцию set_age и декоратор для неё:

# Декоратор смените на callback_query_handler, который будет реагировать на текст 'calories'.
# Теперь функция принимает не message, а call. Доступ к сообщению будет следующим - call.message.
# По итогу получится следующий алгоритм:

# Вводится команда /start
# На эту команду присылается обычное меню: 'Рассчитать' и 'Информация'.
# В ответ на кнопку 'Рассчитать' присылается Inline меню: 'Рассчитать норму калорий' и 'Формулы расчёта'
# По Inline кнопке 'Формулы расчёта' присылается сообщение с формулой.
# По Inline кнопке 'Рассчитать норму калорий' начинает работать машина состояний по цепочке.



