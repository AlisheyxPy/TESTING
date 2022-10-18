from aiogram import types
from states.post import post_s
from utils.db_api.postgres import send_ex
from aiogram.types import ContentTypes
from aiogram.dispatcher import FSMContext
from loader import bot



from loader import dp

@dp.message_handler(chat_id = 5771446949,commands="post")
async def bot_start(message: types.Message):
    await message.answer("Marxamat post rasmini yuboring")
    await post_s.rasm.set()



@dp.message_handler(content_types=ContentTypes.PHOTO,state=post_s.rasm)
async def bot_start(message: types.Message,state:FSMContext):
    await message.answer("post matnini yuboring")
    rasm = message.photo[-1].file_id
    await state.update_data({"rasm":rasm})
    await post_s.next()

@dp.message_handler(state=post_s.xabar)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Xabar yuborildi")
    info = await state.get_data()
    rasm = info.get("rasm")
    all_user = send_ex(f"""SELECT DISTINCT user_id FROM users_info""")
    try:
        for i in all_user:
            await bot.send_photo(chat_id=i[0],photo=rasm,caption=message.text)
    except:
        pass

    await state.finish()


