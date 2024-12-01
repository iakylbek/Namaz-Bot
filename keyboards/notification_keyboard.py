from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData


class MarkingCallback(CallbackData, prefix="marking"):
    name: str = "default"
    status: str  # mark, postpone, missed


def notification_kb():
    buttons = [
        [
            InlineKeyboardButton(
                text="Прочитано",
                callback_data=MarkingCallback(status="mark").pack(),
            ),
            InlineKeyboardButton(
                text="Отложить",
                callback_data=MarkingCallback(status="postpone").pack(),
            ),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def last_notification_kb():
    buttons = [
        [
            InlineKeyboardButton(
                text="Прочитано",
                callback_data=MarkingCallback(status="mark").pack(),
            ),
            InlineKeyboardButton(
                text="Пропущено",
                callback_data=MarkingCallback(status="missed").pack(),
            ),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
