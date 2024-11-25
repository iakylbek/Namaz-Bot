from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def notification_kb():
    buttons = [
        [
            InlineKeyboardButton(text="Отметить\nпрочитанным", callback_data="mark"),
            InlineKeyboardButton(text="Отложить\nна 30 минут", callback_data="postpone"),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def last_notification_kb():
    buttons = [
        [
            InlineKeyboardButton(text="Отметить\nпрочитанным", callback_data="mark"),
            InlineKeyboardButton(text="Отметить\nпропущенным", callback_data="missed"),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
