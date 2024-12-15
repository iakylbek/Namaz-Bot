from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def city_kb():
    city_list = [
        [
            InlineKeyboardButton(text="Москва", callback_data="Москва"),
            InlineKeyboardButton(text="Бишкек", callback_data="Бишкек"),
        ],
        [
            InlineKeyboardButton(text="Ташкент", callback_data="Ташкент"),
            InlineKeyboardButton(text="Алматы", callback_data="Алматы"),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=city_list)


def notification_time_kb():
    notification_time_list = [
        [
            InlineKeyboardButton(text="Каждые 30 мин", callback_data="every_30_min"),
            InlineKeyboardButton(text="Не напоминать", callback_data="dont_notify"),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=notification_time_list)
