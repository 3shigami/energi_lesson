from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from aiogram import executor, types, Bot, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
from aiogram.types import InputFile, InputMedia
import json
import random

print('ковалев эенержи бот запущен [+]')

bot = Bot(token="6755841005:AAF8A6JxjhxwMaHo0Kq02ApRWO7iEn3dwjg")
dp = Dispatcher(bot)

#id админа

admin_id = 939199780

def generate_win_num(num, win_num):
    sp = [i for i in range(1, num + 1)]
    
    win = []
    
    for i in range(win_num):
        ww = random.choice(sp)
        win.append(ww)
        sp.remove(ww)

    return win


def add_konkurs(name, num1, win_num, photo):

    with open("data/data.json", "r", encoding="UTF-8") as file:
        data = json.load(file)
    
        win = generate_win_num(num=num1, win_num=win_num)
        wolodya = []
        for i in range(1, num1):
            
            if i in win:
                wolodya.append({
                    int(i): "win"
                })

            else:
                wolodya.append({
                    i: "lose"
                })

        data[name] = {
            "Название": name,
            "Билеты": wolodya,
            "Номера": num1,
            "фото": photo
        }

    
    with open("data/data.json", "w+", encoding="UTF-8") as file: 
        json.dump(data, file, ensure_ascii=False)
        print(data)


    
    


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    #проверяем id чела, есть админ то 1, если нет, то другое
    if message.chat.id == admin_id:
        markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
	keyboard = [
        [
            KeyboardButton("Профиль")
        ],
        [
            KeyboardButton("Конкрусы")
        ],
        [
            KeyboardButton("Админочка")
        ]
	]
)
        await message.answer("Привет, ты админ", reply_markup=markup)

    else:
        markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
	keyboard = [
        [
            KeyboardButton("Профиль")
        ],
        [
            KeyboardButton("Конкрусы")
        ]
	]
)
        await message.answer("Привет, если ты хочешь поучаствовать в конкурсах, то нажми на кнопку ниже, если хочешь посмотреть свой профиль, то нажми на кнопку профиль", reply_markup=markup)
    

@dp.message_handler(content_types=['text'], text='Админочка')
async def buy(message: types.Message): 
    if message.chat.id == admin_id:
        markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
	keyboard = [
        [
            KeyboardButton("Добавить конкурс")
        ],
        [
            KeyboardButton("Назад<-")
        ]
	]
)
        await message.answer("Вы в админ панельке", reply_markup=markup)


@dp.message_handler(content_types=['text'], text='Назад<-')
async def buy(message: types.Message): 
    if message.chat.id == admin_id:
        markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
	keyboard = [
        [
            KeyboardButton("Профиль")
        ],
        [
            KeyboardButton("Конкрусы")
        ],
        [
            KeyboardButton("Админочка")
        ]
	]
)
        await message.answer("Привет, ты админ", reply_markup=markup)

    else:
        markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
	keyboard = [
        [
            KeyboardButton("Профиль")
        ],
        [
            KeyboardButton("Конкрусы")
        ]
	]
)
        await message.answer("Привет, если ты хочешь поучаствовать в конкурсах, то нажми на кнопку ниже, если хочешь посмотреть свой профиль, то нажми на кнопку профиль", reply_markup=markup)


#if __name__ == '__main__':
#    executor.start_polling(dp)


add_konkurs(name="тамаевэнержи", num=1000, win_num=10, photo="рома хуесос")