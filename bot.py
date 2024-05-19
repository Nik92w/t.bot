import requests
import datetime
from config import open_weather_token
from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram import F

#создаем бота
bot = Bot(token="") #токен сохраню в заметках, чтобы злые дяди ничего случаем не поменяли
dp = Dispatcher()

#Его реакция на команду /start
@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привяо! Напиши сюда название города, и я выдам тебе его прогноз погоды на сегодня!!')

#Его реакция на все остальные сообщения
@dp.message()
async def get_weather(message: types.Message):
        
    #Соединяем название погоды с сайта с кодами эмодзи из Юникода
    emoji_for_bot = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }


    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        #pprint(data) #прогон всей даты с сайта

        #выбираем что будет выводить бот
        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_decription = data["weather"][0]["main"]
        if weather_decription in emoji_for_bot:
            wd = emoji_for_bot[weather_decription]
        else:
            wd = "У меня нет обьяснения тому что у тебя там происходит, глянь ка лучше в окно сам и узнай"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        #придаем выбранным данным красивый вид
        await  message.reply(f" \U00002728 {datetime.datetime.now().strftime('%Y-%m-%d %H:%M' ) } \U00002728 \n"
            f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd} \n"
            f"Влажность: {humidity}\nДавление: {pressure} мм.рт.ст\nВетер: {wind}\n"
            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
            f" \U0001F31F Хорошего дня \U0001F31F ") 




    #исключение в случае ошибки в вводе города
    except:
        await message.reply("\U0001F4DB Неправильное название города, проверьте и попробуйте еще раз! \U0001F4DB")




async def main() :
    print("Start")
    await dp.start_polling(bot)
asyncio.run(main())
