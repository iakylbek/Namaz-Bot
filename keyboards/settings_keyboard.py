from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def city_kb():
    city_list = [
        [
            InlineKeyboardButton(text="Москва", callback_data="Москва"),
            InlineKeyboardButton(text="Бишкек", callback_data="Бишкек")
        ],
        [
            InlineKeyboardButton(text="Ташкент", callback_data="Ташкент"), 
            InlineKeyboardButton(text="Алматы", callback_data="Алматы")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=city_list)


def madhab_kb():
    madhab_list = [
        [
            InlineKeyboardButton(text="Ханафи", callback_data="Ханафи"),
            InlineKeyboardButton(text="Шафии", callback_data="Шафии")
        ],
        [
            InlineKeyboardButton(text="Малика", callback_data="Малика"), 
            InlineKeyboardButton(text="Ханбали", callback_data="Ханбали")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=madhab_list)


def notification_time_kb():
    notification_time_list = [[
        InlineKeyboardButton(text="За 15 минут", callback_data="За 15 минут"),
        InlineKeyboardButton(text="Точное время", callback_data="Точное время"),
        InlineKeyboardButton(text="После 15 минут", callback_data="После 15 минут")
    ]]
    return InlineKeyboardMarkup(inline_keyboard=notification_time_list)
