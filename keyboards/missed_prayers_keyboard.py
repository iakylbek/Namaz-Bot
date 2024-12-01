from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData


class PrayerCallback(CallbackData, prefix="prayer"):
    name: str
    action: str


prayer_names_rus = {
    "Fajr": "Фаджр",
    "Dhuhr": "Зухр",
    "Asr": "Аср",
    "Maghrib": "Магриб",
    "Isha": "Иша",
}


def missed_fajr_kb(missed_namaz: dict):
    buttons = []
    for name, count in missed_namaz.items():
        buttons.append(
            [
                InlineKeyboardButton(
                    text=f"{prayer_names_rus[name]} - {count} пропущено",
                    callback_data=PrayerCallback(name=name, action="noop").pack(),
                )
            ]
        )
        buttons.append(
            [
                InlineKeyboardButton(
                    text="\U00002705",
                    callback_data=PrayerCallback(name=name, action="plus").pack(),
                ),
                InlineKeyboardButton(
                    text="\U0000274c",
                    callback_data=PrayerCallback(name=name, action="minus").pack(),
                ),
            ]
        )
    return InlineKeyboardMarkup(inline_keyboard=buttons)
