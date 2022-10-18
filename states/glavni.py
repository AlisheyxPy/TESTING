from aiogram.dispatcher.filters.state import StatesGroup,State


class murojat_s(StatesGroup):
    butto = State()


class xabar_send(StatesGroup):
    muroja = State()



class uzbek(StatesGroup):
    uz = State()
    B_kurs = State()
    labara_kurs = State()


class regi(StatesGroup):
    isim = State()
    tele = State()
    kun = State()
    soat = State()