from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


b_kusr_ib = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("💻Kompyuter Savodxonlik💻",callback_data="komp_savod"),
         InlineKeyboardButton("🖥Frontend🖥",callback_data="front")],
        [InlineKeyboardButton("⚙️Backend⚙️",callback_data="bekend"),
         InlineKeyboardButton("📱Mobil📱",callback_data="mabil")],
        [InlineKeyboardButton("🎨Grafik Dizayn🎨",callback_data="gedizayn"),
         InlineKeyboardButton("🤖Robotexnika🤖",callback_data="robotech")],
        [InlineKeyboardButton("3D MAX",callback_data="tride"),
         InlineKeyboardButton("Photo Shop",callback_data="photosh")],
    ]
)


kursga_yozilish = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Kursga yozilish",callback_data="regis"),
            InlineKeyboardButton("Kurs haqida",callback_data="savod_h")
        ]
    ]
)


ruz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("1 Dushanba  Chorshanba  Jumma",callback_data="dushanba")
        ],
        [
            InlineKeyboardButton("2 Seshanba  Payshanba  shanba",callback_data="seshanba")
        ]
    ]
)



vaqt_so = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🕗 08:00 -> 10:00",callback_data="hashi")
        ],
        [
            InlineKeyboardButton("🕙 10:00 -> 12:00",callback_data="dahi")
        ],
[
            InlineKeyboardButton("🕑 14:00 -> 16:00",callback_data="duyi")
        ],
[
            InlineKeyboardButton("🕓 16:00 -> 18:00",callback_data="chori")
        ],
[
            InlineKeyboardButton("🕕 18:00 -> 20:00",callback_data="shishi")
        ]
    ]
)


murojat = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="javob yozish",callback_data="javobqaytar"),
         InlineKeyboardButton(text="bekor qilish",callback_data="notanswer")]
])

