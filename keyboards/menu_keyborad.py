from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def menu_kb():
    kb_list = [
        [KeyboardButton(text="Пропущенные намазы"), KeyboardButton(text="Статистика за сегодня")],
        [KeyboardButton(text="Время намаза"), KeyboardButton(text="Настройки")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)
    return keyboard
