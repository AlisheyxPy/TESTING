from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import til, uz_B
from keyboards.inline.prosta import b_kusr_ib
from utils.db_api.postgres import send_ex



from loader import dp

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    send_ex(f"""INSERT INTO users_info(username,user_id)
                VALUES ('@{message.from_user.username}','{message.from_user.id}')
                returning *""")
    await message.answer(f"Tilni Tanlang, {message.from_user.full_name}\nВыбирать",reply_markup=til)


@dp.message_handler(text=["UZ","RU"])
async def tillar(msg: types.Message)-> None:
    if msg.text == "UZ":
        await msg.answer("siz O'zbek tilini tanladingiz",reply_markup=uz_B)
    elif msg.text == "RU":
        pass

@dp.message_handler(text=["Boshlangich kurslar","Labaratoriya kurslari"])
async def kategoria(m:types.Message)-> None:
    await m.delete()
    if m.text == "Boshlangich kurslar":
        biz = "Bizda mavjud Kurslar"
        await m.answer(biz,reply_markup=b_kusr_ib)
    elif m.text == "Labaratoriya kurslari":
        await m.answer("tugallanmagan")








































# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Tilni Tanlang, {message.from_user.full_name}\nВыбирать",reply_markup=til)
#     await till_S.yazik.set()


# @dp.message_handler(state=till_S.yazik)
# async def tillar(msg: types.Message)-> None:
#     if msg.text == "UZ":
#         await msg.answer("tanlang",reply_markup=uz_B)
#         await uzbek.uz.set()
#     elif msg.text == "RU":
#         pass

# @dp.message_handler(state=uzbek.uz)
# async def kategoria(super_msg: types.Message,state:FSMContext)-> None:
#     remov = ReplyKeyboardRemove()
#     if super_msg.text == "Boshlangich kurslar":
#         biz = "Bizda mavjud Kurslar"
#         await super_msg.answer(biz,reply_markup=b_kusr_ib)
#         await state.finish()
#     elif super_msg.text == "Labaratoriya kurslari":
#         await super_msg.answer("tugallanmagan")
#         await state.finish()
#     else:
#         pass



