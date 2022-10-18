from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

til = ReplyKeyboardMarkup([
    [KeyboardButton("UZ"),KeyboardButton("RU")]
],resize_keyboard=True)

uz_B = ReplyKeyboardMarkup([
    [KeyboardButton("Boshlangich kurslar"),KeyboardButton("Labaratoriya kurslari")]
],resize_keyboard=True)

cont = ReplyKeyboardMarkup([
    [KeyboardButton("Send Contact",request_contact=True)]
],resize_keyboard=True)


murojat_b = ReplyKeyboardMarkup([
    [KeyboardButton("Murojat")]
])
