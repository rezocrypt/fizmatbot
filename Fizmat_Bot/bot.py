# Importing Libraries
import aiogram
import keyboards as kb
from config import TOKEN
from datetime import datetime
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher



start_text = """
Ահա բոլոր հրամանները որոնք կարող եք իրականացնել 😃    

1.  🏁 /start -- Սկիզբ        
2.  🕓 /schedule -- Կտեսնեք ներկայիս կիսամյակի ժամացուցակը 
3.  🗓 /time -- Կտեսնեք երեխաների դասացուցակը  
4.  🔔 /news -- Կտեսնեք վերջին լուրերը ֆիզմաթի մասին              
5.  📚 /taskbook -- Կստանաք խնդրագիրքը որպես PDF ֆայլ 
6.  ☎️ /contact -- Կոնտակտներ ֆիզմաթի հետ կապնվելու համար           
7.  🧑‍🎓 /member -- Դիմորդի անկյուն        
8.  📝 /tasks -- Առաջադրանքներ      
9.  📊 /results -- Արդյունքներ      
10. 💔 /ourheroes -- Մեր Հերոսները      
11. ❓  /aboutphysmath -- Ֆիզմաթի Մասին   

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

# Opening our heroes file text and reading it
def ourheroes():
    with open('Files/ourheroes.txt',encoding="utf8") as f:
        a = f.read()
    return a

# Opening about physmath file text and reading it
def aboutphysmath():
    with open('Files/aboutphysmath.txt',encoding="utf8") as f:
        a = f.read()
    return a




# Function for adding new log
def addLog(msg,text):
    with open("Files/logs.txt", "a",encoding="utf8") as f:
        log = f"[{text}]    ID:{msg.from_user.id}    NAME:{msg.from_user.full_name}    TIME:{datetime.now()}    [{text}]"+"\n"
        print(log)
        f.write(log)










# Function for start
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
    button_7 = types.KeyboardButton(text="📝Առաջադրանքներ📝")
    keyboard.add(button_7)
    button_8 = types.KeyboardButton(text="📊Արդյունքներ📊")
    keyboard.add(button_8)
    button_9 = types.KeyboardButton(text="💔Մեր Հերոսները💔")
    keyboard.add(button_9)
    button_10 = types.KeyboardButton(text="❓Ֆիզմաթի Մասին❓")
    keyboard.add(button_10)
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
    addLog(msg,"Դիմորդի անկյուն")
    await bot.send_message(msg.from_user.id, applicant())










# Function for taskbook
@dp.message_handler(lambda message: message.text == "📚Խնդրագիրք📚")
async def cmd_start(msg: types.Message):
    addLog(msg,"Խնդրագիրք")
    await bot.send_message(msg.from_user.id, "Մեկ վայրկյան հիմա ֆայլը կուղարկվի․․․")
    await bot.send_document(chat_id = msg.from_user.id,caption = '✅Խնդրեմ սա էլ խնդրագիրքը😃 ✅',document = open("Files/taskbook.pdf", 'rb'))

@dp.message_handler(commands="taskbook")
async def cmd_start(msg: types.Message):
    addLog(msg,"Խնդրագիրք")
    await bot.send_message(msg.from_user.id, "Մեկ վայրկյան հիմա ֆայլը կուղարկվի․․․")
    await bot.send_document(chat_id = msg.from_user.id,caption = '✅Խնդրեմ սա էլ խնդրագիրքը😃 ✅',document = open("Files/taskbook.pdf", 'rb'))










# Function for contact them
@dp.message_handler(lambda message: message.text == "☎️Կապ Ֆիզմաթի Հետ☎️")
async def cmd_start(msg: types.Message):
    addLog(msg,"Կապ Ֆիզմաթի Հետ")
    await bot.send_message(msg.from_user.id, contact())

@dp.message_handler(commands="contact")
async def cmd_start(msg: types.Message):
    addLog(msg,"Կապ Ֆիզմաթի Հետ")
    await bot.send_message(msg.from_user.id, contact())










# Function for tasks
@dp.message_handler(lambda message: message.text == "📝Առաջադրանքներ📝")
async def cmd_start(msg: types.Message):
    addLog(msg,"Առաջադրանքներ")
    await bot.send_message(msg.from_user.id, "📝 Նշեք որ դասարանի առաջադրանքները և լուծումները կցանկանաք տեսնել? 😀 ",reply_markup=kb.tasksKb)

@dp.message_handler(commands="tasks")
async def cmd_start(msg: types.Message):
    addLog(msg,"Առաջադրանքներ")
    await bot.send_message(msg.from_user.id, "📝 Նշեք որ դասարանի առաջադրանքները և լուծումները կցանկանաք տեսնել? 😀 ",reply_markup=kb.tasksKb)










# Function for results
@dp.message_handler(lambda message: message.text == "📊Արդյունքներ📊")
async def cmd_start(msg: types.Message):
    addLog(msg,"Արդյունքներ")
    await bot.send_message(msg.from_user.id, "📊 Նշեք որ դասարանի արդյունքներն եք ցանկանում տեսնել? 😀 ",reply_markup=kb.resultsKb)

@dp.message_handler(commands="results")
async def cmd_start(msg: types.Message):
    addLog(msg,"Արդյունքներ")
    await bot.send_message(msg.from_user.id, "📊 Նշեք որ դասարանի արդյունքներն եք ցանկանում տեսնել? 😀 ",reply_markup=kb.resultsKb)









# Function for Our Heroes
@dp.message_handler(lambda message: message.text == "💔Մեր Հերոսները💔")
async def cmd_start(msg: types.Message):
    addLog(msg,"Հերոսներ")
    await bot.send_photo(chat_id=msg.from_user.id, photo=open('Photos/ourheroes.png', 'rb'),caption=ourheroes())

@dp.message_handler(commands="ourheroes")
async def cmd_start(msg: types.Message):
    addLog(msg,"Հերոսներ")
    await bot.send_photo(chat_id=msg.from_user.id, photo=open('Photos/ourheroes.png', 'rb'),caption=ourheroes())









# Function for about physmath
@dp.message_handler(lambda message: message.text == "❓Ֆիզմաթի Մասին❓")
async def cmd_start(msg: types.Message):
    addLog(msg,"Ֆիզմաթի Մասին")
    await bot.send_photo(chat_id=msg.from_user.id, photo=open('Photos/aboutphysmath.jpg', 'rb'),caption="Ֆիզմաթի Մասին")
    await bot.send_message(msg.from_user.id, aboutphysmath()[0:1000])
    await bot.send_message(msg.from_user.id, aboutphysmath()[1000:2000])
    await bot.send_message(msg.from_user.id, aboutphysmath()[2000:3000])
    await bot.send_message(msg.from_user.id, aboutphysmath()[3000:3902])

@dp.message_handler(commands="aboutphysmath")
async def cmd_start(msg: types.Message):
    addLog(msg,"Ֆիզմաթի Մասին")
    await bot.send_photo(chat_id=msg.from_user.id, photo=open('Photos/aboutphysmath.jpg', 'rb'),caption="Ֆիզմաթի Մասին")
    await bot.send_message(msg.from_user.id, aboutphysmath()[0:1000])
    await bot.send_message(msg.from_user.id, aboutphysmath()[1000:2000])
    await bot.send_message(msg.from_user.id, aboutphysmath()[2000:3000])
    await bot.send_message(msg.from_user.id, aboutphysmath()[3000:3902])








# Functions for tasks
@dp.message_handler(lambda message: message.text == "7 դասարան մաթեմատիկա")
async def cmd_start(msg: types.Message):
    addLog(msg,"Խնդիրներ")
    await bot.send_message(msg.from_user.id, "Մեկ վայրկյան հիմա ֆայլը կուղարկվի․․․")
    await bot.send_document(chat_id = msg.from_user.id,caption = '✅Խնդրեմ սա էլ առաջադրանքները😃 ✅',document = open("Files/7m.pdf", 'rb'))

@dp.message_handler(lambda message: message.text == "10 դասարան ֆիզիկա")
async def cmd_start(msg: types.Message):
    addLog(msg,"Խնդիրներ")
    await bot.send_message(msg.from_user.id, "Մեկ վայրկյան հիմա ֆայլը կուղարկվի․․․")
    await bot.send_document(chat_id = msg.from_user.id,caption = '✅Խնդրեմ սա էլ առաջադրանքները😃 ✅',document = open("Files/10f.pdf", 'rb'))

@dp.message_handler(lambda message: message.text == "8 դասարան մաթեմատիկա")
async def cmd_start(msg: types.Message):
    addLog(msg,"Խնդիրներ")
    await bot.send_message(msg.from_user.id, "Մեկ վայրկյան հիմա ֆայլը կուղարկվի․․․")
    await bot.send_document(chat_id = msg.from_user.id,caption = '✅Խնդրեմ սա էլ առաջադրանքները😃 ✅',document = open("Files/8m.pdf", 'rb'))

@dp.message_handler(lambda message: message.text == "10 դասարան մաթեմատիկա")
async def cmd_start(msg: types.Message):
    addLog(msg,"Խնդիրներ")
    await bot.send_message(msg.from_user.id, "Մեկ վայրկյան հիմա ֆայլը կուղարկվի․․․")
    await bot.send_document(chat_id = msg.from_user.id,caption = '✅Խնդրեմ սա էլ առաջադրանքները😃 ✅',document = open("Files/10m.pdf", 'rb'))








# Functions for results
@dp.message_handler(lambda message: message.text == "7 դասարան արդյունքներ մաթեմատիկա")
async def cmd_start(msg: types.Message):
    addLog(msg,"Խնդիրներ")
    await bot.send_message(msg.from_user.id, "Մեկ վայրկյան հիմա ֆայլը կուղարկվի․․․")
    await bot.send_document(chat_id = msg.from_user.id,caption = '✅Խնդրեմ սա էլ արդյունքները😃 ✅',document = open("Files/a7m.pdf", 'rb'))

@dp.message_handler(lambda message: message.text == "10 դասարան արդյունքներ ֆիզիկա")
async def cmd_start(msg: types.Message):
    addLog(msg,"Խնդիրներ")
    await bot.send_message(msg.from_user.id, "Մեկ վայրկյան հիմա ֆայլը կուղարկվի․․․")
    await bot.send_document(chat_id = msg.from_user.id,caption = '✅Խնդրեմ սա էլ արդյունքները😃 ✅',document = open("Files/a10f.pdf", 'rb'))

@dp.message_handler(lambda message: message.text == "8 դասարան արդյունքներ մաթեմատիկա")
async def cmd_start(msg: types.Message):
    addLog(msg,"Խնդիրներ")
    await bot.send_message(msg.from_user.id, "Մեկ վայրկյան հիմա ֆայլը կուղարկվի․․․")
    await bot.send_document(chat_id = msg.from_user.id,caption = '✅Խնդրեմ սա էլ արդյունքները😃 ✅',document = open("Files/a8m.pdf", 'rb'))

@dp.message_handler(lambda message: message.text == "10 դասարան արդյունքներ մաթեմատիկա")
async def cmd_start(msg: types.Message):
    addLog(msg,"Խնդիրներ")
    await bot.send_message(msg.from_user.id, "Մեկ վայրկյան հիմա ֆայլը կուղարկվի․․․")
    await bot.send_document(chat_id = msg.from_user.id,caption = '✅Խնդրեմ սա էլ արդյունքները😃 ✅',document = open("Files/a10m.pdf", 'rb'))












# Command not found
@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, f"⚠️Հրամանը Չգտնվեց⚠️\n\n\n😞🤷‍♂️ Ներողություն, դժվարանում եմ ինչ-որ բանով օգնել 🤷‍♂️😞\n\nԱյլ հարցերի կամ առաջարկների դեպքում կարող եք կապնվել ինձ հետ \n\n📣📣📣📣📣📣📣📣📣📣📣📣📣📣\n📣      Telegram : 📱 @cryptojacker 📱     📣\n📣📣📣📣📣📣📣📣📣📣📣📣📣📣\n\n\n⚠️Թույլատրելի հրամաններ⚠️\n\n{start_text}")


if __name__ == '__main__':
    executor.start_polling(dp)