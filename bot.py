from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram import F

bot = Bot(token="6953886901:AAF7-NRAZy4rk8GDOPL_eAe8o6lzRVoubwE")
dp = Dispatcher()

# @dp.message(CommandStart())
# async def start_cmd(message: types.Message)  :
#     await message.answer('Hello')

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


async def main() :
    print("Start")
    await dp.start_polling(bot)
asyncio.run(main())
