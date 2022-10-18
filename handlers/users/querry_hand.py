from loader import bot,dp
from aiogram import types
from keyboards.inline.prosta import kursga_yozilish, ruz, vaqt_so, murojat
from states.glavni import regi, murojat_s
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes
from keyboards.default.menu import cont, murojat_b
from utils.db_api.postgres import send_ex
from aiogram.types import ReplyKeyboardRemove

a = "HTML"
kurs_ = ""
kurs_nomi = ""

@dp.callback_query_handler(text=["komp_savod","front","bekend","mabil","robotech","tride","photosh","gedizayn"])
async def optom(msg: types.CallbackQuery):
    global kurs_,kurs_nomi
    kurs_ = msg.data
    if msg.data == "komp_savod":
        kurs_nomi = "siz <b>Kamptuyer savodxonlik</b>"

    elif msg.data == "front":
        kurs_nomi = "siz <b>Frontend</b>"

    elif msg.data == "bekend":
        kurs_nomi = "siz <b>Backend</b>"

    elif msg.data == "mabil":
        kurs_nomi = "siz <b>Mobil Dasturlash</b>"

    elif msg.data == "robotech":
        kurs_nomi = "siz <b>Robotexnika</b>"

    elif msg.data == "tride":
        kurs_nomi = "siz <b>3D MAX</b>"

    elif msg.data == "photosh":
        kurs_nomi = "<b>Photoshop</b>"

    elif msg.data == "gedizayn":
        kurs_nomi = "<b>grafik dizayn</b> "

    else:
        pass
    await msg.message.answer(f"Siz {kurs_nomi} kursini tanladingiz",reply_markup=kursga_yozilish)
    await msg.message.delete()



@dp.callback_query_handler(text="savod_h")
async def savod_haqida(sav: types.CallbackQuery):
    await sav.message.answer(f"Savodxonli kursida siz\nkampyuter boshlang'ich bilimlar\ninternet bilan ishlash\n"
                             f"va xokazo")


@dp.callback_query_handler(text="regis")
async def savod_haqida(regis: types.CallbackQuery):
    await regis.message.answer("<b>Marxamat ism familyangizni kiriting: </b>",parse_mode=a)
    await regis.message.delete()
    await regi.isim.set()

    @dp.message_handler(state=regi.isim)
    async def fully_na(mesaage: types.Message, state: FSMContext):
        name = mesaage.text
        await state.update_data({"ism": name})
        await mesaage.answer("<b>Telefon raqamingizni kiriting</b>",reply_markup=cont)
        await regi.next()


    @dp.message_handler(content_types=ContentTypes.CONTACT,state=regi.tele)
    async def agene(messa: types.Message, state: FSMContext):
        tel = messa.contact.phone_number
        await state.update_data({"telefon":tel})
        await messa.answer("<b>O'zingizga maqul kunni tanlang</b>", reply_markup=ruz,parse_mode=a)
        await regi.next()

    @dp.callback_query_handler(state=regi.kun)
    async def agene(messa: types.CallbackQuery, state: FSMContext):
        if messa.data == "dushanba":
            x = "Dushanba, Chorshanba, Jumma"
        else:
            x = "Seshanba, Payshanba, Shanba"
        await state.update_data({"roz": x})
        await messa.message.answer("<b>O'zingizga maqul soatni tanlang</b>",reply_markup=vaqt_so,parse_mode=a)
        await messa.message.delete()
        await regi.next()

    @dp.callback_query_handler(state=regi.soat)
    async def agene(messa: types.CallbackQuery, state: FSMContext):
        if messa.data == "hashi":
            x = "08:00 -> 10:00"
        if messa.data == "dahi":
            x = "10:00 -> 12:00"
        if messa.data == "duyi":
            x = "14:00 -> 16:00"
        if messa.data == "chori":
            x = "16:00 -> 18:00"
        else:
            x = "18:00 -> 20:00"
        await state.update_data({"vaqt": x})
        await messa.message.delete()
        opshi = await state.get_data()

        ism = opshi.get("ism")
        tel =opshi.get("telefon")
        kun = opshi.get("roz")
        soat = opshi.get("vaqt")
        send_ex(f"""INSERT INTO users_register(full_name, telephon, hafta_kun, soat, kurs)
                VALUES('{ism}','{tel}','{kun}','{soat}','{kurs_}')
                returning *""")
        await messa.message.answer("<b>Siz ro'yxtdan o'ttingiz</b>",reply_markup=murojat_b,parse_mode=a)
        # await messa.message.answer("<b>siz bilan bog'lanamiz</b>",reply_markup=pass,parse_mode=a)
        await state.finish()

@dp.message_handler(text="Murojat")
async def savod_haqida(sav: types.Message):
    await murojat_s.butto.set()
    await sav.answer("marxamt murojatingini yozing")


@dp.message_handler(state=murojat_s.butto)
async def savod_haqida(sav: types.Message, state: FSMContext):
    await bot.send_message(chat_id=1737841515, text=f"{sav.from_user.full_name} dan sizga murojat\n@{sav.from_user.username}\n->{sav.text}",reply_markup=murojat)
    await state.update_data({"user":sav.from_user.id})
    await sav.answer("murojat yuborildi javobni kuting")
    send_ex(f"""INSERT INTO user_murojat (text, user_id)
                VALUES ('{sav.text}','{sav.from_user.id}')
                returning *""")
    await state.finish()