from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from datetime import datetime

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def news():
    with open('Files/news.txt',encoding="utf8") as f:
        news = f.read()
    return news

def applicant():
    with open('Files/applicant.txt',encoding="utf8") as f:
        applicant = f.read()
    return applicant

def addLog(msg,text):
    with open("logs.txt", "a",encoding="utf8") as f:
        log = f"[{text}]    ID:{msg.from_user.id}    NAME:{msg.from_user.full_name}    TIME:{datetime.now()}    [{text}]"+"\n"
        print(log)
        f.write(log)



@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="🕓Ժամացուցակ🕓")
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text="🗓Դասացուցակ🗓")
    keyboard.add(button_2)
    button_3 = types.KeyboardButton(text="🔔Վերջին Լուրեր🔔")
    keyboard.add(button_3)
    button_3 = types.KeyboardButton(text="🧑‍🎓Դիմորդի Անկյուն🧑‍🎓")
    keyboard.add(button_3)
    await message.answer("Ինչեք ցանկանում՞", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "🕓Ժամացուցակ🕓")
async def cmd_start(msg: types.Message):
    addLog(msg,"Ժամացուցակ")
    await bot.send_photo(chat_id=msg.from_user.id, photo=open('Photos/times.jpg', 'rb'),caption="✅ Խնդրեմ, սա էլ ժամացուցակը😃 ✅")

@dp.message_handler(lambda message: message.text == "🗓Դասացուցակ🗓")
async def cmd_start(msg: types.Message):
    addLog(msg,"Դասացուցակ")
    await bot.send_photo(chat_id=msg.from_user.id, photo=open('Photos/classtimes.jpg', 'rb'),caption="✅ Խնդրեմ, սա էլ դասացուցակը😃 ✅")

@dp.message_handler(lambda message: message.text == "🔔Վերջին Լուրեր🔔")
async def cmd_start(msg: types.Message):
    addLog(msg,"Վերջին Լուրեր")
    await bot.send_photo(chat_id=msg.from_user.id, photo=open('Photos/news.jpg', 'rb'),caption=news())

@dp.message_handler(lambda message: message.text == "🧑‍🎓Դիմորդի Անկյուն🧑‍🎓")
async def cmd_start(msg: types.Message):
    addLog(msg,"Դիմորդի անկուն")
    await bot.send_message(msg.from_user.id, applicant())




@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)