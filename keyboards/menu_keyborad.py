from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def menu_kb():
    kb_list = [
        [
            KeyboardButton(text="Время намаза"),
        ],
        [KeyboardButton(text="Пропущенные намазы"), KeyboardButton(text="Настройки")],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True
    )
    return keyboard
