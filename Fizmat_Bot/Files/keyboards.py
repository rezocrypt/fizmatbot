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


# Exercise grade buttons
btn1 = KeyboardButton("5-րդ դասարանի")
btn2 = KeyboardButton("6-րդ դասարանի")
btn3 = KeyboardButton("7-րդ դասարանի")
btn4 = KeyboardButton("8-րդ դասարանի")
btn5 = KeyboardButton("9-րդ դասարանի")
btn6 = KeyboardButton("10-րդ դասարանի")
btn7 = KeyboardButton("11 ից 12-րդ դասարանի")
exercisesKb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(btn1,btn2,btn3,btn4,btn5,btn6,btn7)