import logging
import sys
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart
import requests

# def try_input(message) -> str:
#     fail = True
#     while fail:
#         try:
#             result = input(message)
#             fail = False
#         except:
#             print("Wrong input. Try again.")
#     return result

# _from, _to, _date_yyyy_mm_dd, _n_guys, _transport = None, None, None, None, None

# _from = try_input("From: ")
# _to = try_input("To: ")
# _date_yyyy_mm_dd = try_input("Date (YYYY-MM-DD): ")
# _n_guys = try_input("Amount of guys: ")
# search_url = f"https://www.blablacar.com.ua/search?fn={_from}&tn={_to}&db={_date_yyyy_mm_dd}&seats={_n_guys}&search_origin=HOME"

# _transport = try_input("1) Автобус\n2) Спільна поїздка\n3) Всі\n : ")
# _transport_lst = ["&transport_type=bus","&transport_type=carpooling",""]
# transport_type=carpooling   CARS
# transport_type=bus          BUS

# fail = True
# while fail:
    # if _transport in ["1","2","3"]:
        # search_url += _transport_lst[int(_transport)-1]
        # fail = False
    # else:
        # print("Wrong input. Try again.")

API_TOKEN = "7155199366:AAE7or1as2a6hC3k0gGWAL9tsQrKaCN9vr4"

# print(search_url)

dp = Dispatcher()

i = 0

@dp.message(CommandStart())
async def send_weclome(message: types.Message):
    global i
    print([message])
    await message.answer(f"Ваше число = {i}")
    i += 1
    # html = requests.get(search_url)
    # print(html.text)
@dp.message()
async def echo(message: types.Message):
    ...

async def main():
    bot = Bot(token=API_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    while True:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())