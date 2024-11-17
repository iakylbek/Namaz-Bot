from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def notification_kb():
    buttons = [
        [
            InlineKeyboardButton(text="Отметить прочитанным", callback_data="mark"),
            InlineKeyboardButton(text="Отложить на 30 минут", callback_data="postpone")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def last_notification_kb():
    buttons = [
        [
            InlineKeyboardButton(text="Отметить прочитанным", callback_data="mark"),
            InlineKeyboardButton(text="Отметить пропущенным", callback_data="missed")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
