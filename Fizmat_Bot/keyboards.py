# Importing libraries
from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup


# Task buttons
btn1 = KeyboardButton("7 դասարան մաթեմատիկա")
btn2 = KeyboardButton("10 դասարան ֆիզիկա")
btn3 = KeyboardButton("8 դասարան մաթեմատիկա")
btn4 = KeyboardButton("10 դասարան մաթեմատիկա")
tasksKb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(btn1,btn2,btn3,btn4)


# Result buttons
btn1 = KeyboardButton("7 դասարան արդյունքներ մաթեմատիկա")
btn2 = KeyboardButton("10 դասարան արդյունքներ ֆիզիկա")
btn3 = KeyboardButton("8 դասարան արդյունքներ մաթեմատիկա")
btn4 = KeyboardButton("10 դասարան արդյունքներ մաթեմատիկա")
resultsKb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(btn1,btn2,btn3,btn4)