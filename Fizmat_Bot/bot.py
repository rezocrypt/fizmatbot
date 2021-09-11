# Importing Libraries
import aiogram
from config import TOKEN
from datetime import datetime
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher


start_text = """
🎓🎓🎓🎓🎓🎓
🎓Ահա բոլոր հրամանները որոնք կարող եք իրականացնել 😃     
🎓1. /schedule -- Կտեսնեք ներկայիս կիսամյակի ժամացուցակը 
🎓2. /time -- Կտեսնեք երեխաների դասացուցակը  
🎓3. /news -- Կտեսնեք վերջին լուրերը ֆիզմաթի մասին              
🎓4. /taskbook -- Կստանաք խնդրագիրքը որպես PDF ֆայլ 
🎓5. /contact -- Կոնտակտներ ֆիզմաթի հետ կապնվելու համար           
🎓🎓🎓🎓🎓🎓
"""

# Making and conneecting bot
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Open news file txt and reading it
def news():
    with open('Files/news.txt',encoding="utf8") as f:
        news = f.read()
    return news

# Opening applicant file text and reading it
def applicant():
    with open('Files/applicant.txt',encoding="utf8") as f:
        applicant = f.read()
    return applicant

# Opening contact file text and reading it
def contact():
    with open('Files/contact.txt',encoding="utf8") as f:
        applicant = f.read()
    return applicant

# Function for adding new log
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
    button_4 = types.KeyboardButton(text="🧑‍🎓Դիմորդի Անկյուն🧑‍🎓")
    keyboard.add(button_4)
    button_5 = types.KeyboardButton(text="📚Խնդրագիրք📚")
    keyboard.add(button_5)
    button_6 = types.KeyboardButton(text="☎️Կապ Ֆիզմաթի Հետ☎️")
    keyboard.add(button_6)
    await message.answer(start_text, reply_markup=keyboard)





# Function for scheaulde
@dp.message_handler(lambda message: message.text == "🕓Ժամացուցակ🕓")
async def cmd_start(msg: types.Message):
    addLog(msg,"Ժամացուցակ")
    await bot.send_photo(chat_id=msg.from_user.id, photo=open('Photos/times.jpg', 'rb'),caption="✅ Խնդրեմ, սա էլ ժամացուցակը😃 ✅")

@dp.message_handler(commands="schedule")
async def cmd_start(msg: types.Message):
    addLog(msg,"Ժամացուցակ")
    await bot.send_photo(chat_id=msg.from_user.id, photo=open('Photos/times.jpg', 'rb'),caption="✅ Խնդրեմ, սա էլ ժամացուցակը😃 ✅")










# Function for time
@dp.message_handler(lambda message: message.text == "🗓Դասացուցակ🗓")
async def cmd_start(msg: types.Message):
    addLog(msg,"Դասացուցակ")
    await bot.send_photo(chat_id=msg.from_user.id, photo=open('Photos/classtimes.jpg', 'rb'),caption="✅ Խնդրեմ, սա էլ դասացուցակը😃 ✅")

@dp.message_handler(commands="time")
async def cmd_start(msg: types.Message):
    addLog(msg,"Դասացուցակ")
    await bot.send_photo(chat_id=msg.from_user.id, photo=open('Photos/classtimes.jpg', 'rb'),caption="✅ Խնդրեմ, սա էլ դասացուցակը😃 ✅")










# Function for news
@dp.message_handler(lambda message: message.text == "🔔Վերջին Լուրեր🔔")
async def cmd_start(msg: types.Message):
    addLog(msg,"Վերջին Լուրեր")
    await bot.send_photo(chat_id=msg.from_user.id, photo=open('Photos/news.jpg', 'rb'),caption=news())

@dp.message_handler(commands="news")
async def cmd_start(msg: types.Message):
    addLog(msg,"Վերջին Լուրեր")
    await bot.send_photo(chat_id=msg.from_user.id, photo=open('Photos/news.jpg', 'rb'),caption=news())










# Function for member
@dp.message_handler(lambda message: message.text == "🧑‍🎓Դիմորդի Անկյուն🧑‍🎓")
async def cmd_start(msg: types.Message):
    addLog(msg,"Դիմորդի անկուն")
    await bot.send_message(msg.from_user.id, applicant())

@dp.message_handler(commands="member")
async def cmd_start(msg: types.Message):
    addLog(msg,"Դիմորդի անկուն")
    await bot.send_message(msg.from_user.id, applicant())










# Function for taskbook
@dp.message_handler(lambda message: message.text == "📚Խնդրագիրք📚")
async def cmd_start(msg: types.Message):
    addLog(msg,"Խնդրագիրք")
    await bot.send_message(msg.from_user.id, "Մեկ վայրկյան հիմա ֆայլը կուղարկվի․․․")
    await bot.send_document(chat_id = msg.from_user.id,caption = '✅Խնդրեմ սա էլ խմդրագիրքը😃 ✅',document = open("Files/taskbook.pdf", 'rb'))

@dp.message_handler(commands="taskbook")
async def cmd_start(msg: types.Message):
    addLog(msg,"Խնդրագիրք")
    await bot.send_message(msg.from_user.id, "Մեկ վայրկյան հիմա ֆայլը կուղարկվի․․․")
    await bot.send_document(chat_id = msg.from_user.id,caption = '✅Խնդրեմ սա էլ խմդրագիրքը😃 ✅',document = open("Files/taskbook.pdf", 'rb'))










# Function for contact them
@dp.message_handler(lambda message: message.text == "☎️Կապ Ֆիզմաթի Հետ☎️")
async def cmd_start(msg: types.Message):
    addLog(msg,"Կապ Ֆիզմաթի Հետ")
    await bot.send_message(msg.from_user.id, contact())

@dp.message_handler(commands="contact")
async def cmd_start(msg: types.Message):
    addLog(msg,"Կապ Ֆիզմաթի Հետ")
    await bot.send_message(msg.from_user.id, contact())








# Command not found
@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, f"⚠️Հրամանը Չգտնվեց⚠️\n\n\n😞🤷‍♂️ Ներողություն, դժվարանում եմ ինչ-որ բանով օգնել 🤷‍♂️😞\n\nԱյլ հարցերի կամ առաջարկների դեպքում կարող եք կապնվել ինձ հետ \n\n📣📣📣📣📣📣📣📣📣📣📣📣📣📣\n📣      Telegram : 📱 @cryptojacker 📱     📣\n📣📣📣📣📣📣📣📣📣📣📣📣📣📣\n\n\n⚠️Թույլատրելի հրամաններ⚠️\n\n{start_text}")


if __name__ == '__main__':
    executor.start_polling(dp)