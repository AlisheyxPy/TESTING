from loader import bot,dp
from aiogram import types
from keyboards.inline.prosta import kursga_yozilish, ruz, vaqt_so, murojat
from states.glavni import regi, murojat_s
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes
from keyboards.default.menu import cont, murojat_b
from utils.db_api.postgres import send_ex
from aiogram.types import ReplyKeyboardRemove
from states.glavni import xabar_send



@dp.callback_query_handler(text=["javobqaytar","notanswer"])
async def savod_haqida(sav: types.CallbackQuery):
    if sav.data == "javobqaytar":
        global user
        user = send_ex(f"""SELECT user_id FROM user_murojat WHERE text = '{sav.message.text.split("->")[-1]}'""")
        await sav.message.answer("marxamat javob yozishingiz mumkin")
        await xabar_send.muroja.set()
        await sav.message.delete()
    else:
        await sav.message.answer("murojat o'chrildi")
        await sav.message.delete()

@dp.message_handler(state=xabar_send.muroja)
async def xabarlar(msg: types.Message, state: FSMContext):
    await bot.send_message(chat_id=user[0][0], text=f"{msg.text}\nadmindan xabar keldi")
    await state.finish()