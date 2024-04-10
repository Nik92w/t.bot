 from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram import F
import InlineKeyboardMarkup,  ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton

bot = Bot(token="6953886901:AAF7-NRAZy4rk8GDOPL_eAe8o6lzRVoubwE")
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message)  :
     await message.answer(message.text)
print(1)

@dp.message(CommandStart())
async def hello_cmd(message: types.Message) :
    kb = [
        [types.KeyboardButton(text="распорядок дня")],
        [types.KeyboardButton(text="напоминания")],
        [types.KeyboardButton(text="погода")],
        [types.KeyboardButton(text="записи")],
    ]
    keyboard = types.ReplyKeyboardMarkup (keyboard=kb, resize_keyboard=True, input_field_placeholder="выберете, что вам нужно")
    await message.answer( text=f"hi, {message.from_user.username}", reply_markup=keyboard)

@dp.message(F.text.lower() == "распорядок дня")
async def with_day(message : types.Message):
kb = [
        [types.KeyboardButton(text="Создание нового дела")],
        [types.KeyboardButton(text="Удалить Запись")],
        [types.KeyboardButton(text="Меню")],
    ]
keyboard = types.ReplyKeyboardMarkup(keyboard=kb ,resize_keyboard=True,input_field_placeholder="выберете, что делать дальше" )

menu = "menu glav"
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="◀️ Выйти в меню")]
    ], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]
    ])

async def main() :
    print("Start")
    await dp.start_polling(bot)
asyncio.run(main())
