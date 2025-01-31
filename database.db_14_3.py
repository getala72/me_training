# Задача "Витамины для всех!":

# Подготовка:

# Подготовьте Telegram-бота из последнего домашнего задания 13 моудля сохранив код с ним в файл module_14_3.py.

# Если вы не решали новые задания из предыдущего модуля рекомендуется выполнить их.
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder
from aiogram.types import Message,CallbackQuery,FSInputFile
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


# Дополните ранее написанный код для Telegram-бота:

# Создайте и дополните клавиатуры:



# В главную (обычную) клавиатуру меню добавьте кнопку "Купить".
# Создайте Inline меню из 4 кнопок с надписями "Product1", "Product2", "Product3", "Product4". У всех кнопок назначьте callback_data="product_buying"
# Создайте хэндлеры и функции к ним:

# Message хэндлер, который реагирует на текст "Купить" и оборачивает функцию get_buying_list(message).
# Функция get_buying_list должна выводить надписи 'Название: Product<number> | Описание: описание <number> | Цена: <number * 100>' 4 раза. 
# После каждой надписи выводите картинки к продуктам. В конце выведите ранее созданное Inline меню с надписью "Выберите продукт для покупки:".
# Callback хэндлер, который реагирует на текст "product_buying" и оборачивает функцию send_confirm_message(call).
# Функция send_confirm_message, присылает сообщение "Вы успешно приобрели продукт!"

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


b=InlineKeyboardBuilder()
[b.button(text=f"Product{i}",callback_data="product_buying") for i in range(1,5)]
ikb_buy_menu = b.as_markup()

    
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Привет! Я бот помогающий твоему здоровью.",reply_markup=kb_menu(['Рассчитать' , 'Информация' , "Купить"]))


@dp.message(F.text.lower()=='рассчитать')
async def  main_menu(message: Message) -> None:
    await message.answer('Выберите опцию:',reply_markup=kb_inline_menu(['Рассчитать норму каллорий' , 'Формулы расчёта']))

@dp.message(F.text.lower()=='купить')
async def get_buying_list(message: Message) -> None:
    for i in range(1,5):
        await message.answer(f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}')
        await message.answer_photo(FSInputFile('1.jpg')) 
        await message.answer("Выберите продукт для покупки:",reply_markup=ikb_buy_menu)
            


@dp.callback_query(F.data=='Формулы расчёта')
async def callback_query_hand(callback:CallbackQuery) -> None:
   await callback.message.answer('10 x вес (кг) + 6.25 x рост (см) - 5 x возраст (r) - 161') 
   await callback.answer()



@dp.callback_query(F.data=='Рассчитать норму каллорий')
async def start_hand(callback:CallbackQuery,state:FSMContext) -> None:
   await state.set_state(UserState.age)
   await callback.answer('Введите свой возраст:')
   await callback.answer()


@dp.callback_query(F.data=="product_buying")
async def buy(callback:CallbackQuery,state:FSMContext) -> None:
   await callback.message.answer("Вы успешно приобрели продукт!") 
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
        
# Пример результата выполнения программы:

# Обновлённое главное меню:


# Список товаров и меню покупки:


# Примечания:

# Название продуктов и картинок к ним можете выбрать самостоятельно. (Минимум 4)
