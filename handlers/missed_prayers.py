from aiogram.types import Message
from aiogram.types import CallbackQuery

from keyboards.missed_prayers_keyboard import missed_fajr_kb, PrayerCallback

users_namaz = {}


async def missed_namaz_handler(message: Message) -> None:
    user_id = message.from_user.id

    if user_id not in users_namaz:
        users_namaz[user_id] = {
            "Fajr": 0,
            "Dhuhr": 0,
            "Asr": 0,
            "Maghrib": 0,
            "Isha": 0,
        }

    await message.answer(
        "\U0001F4C3 Список пропущенных намазов", reply_markup=missed_fajr_kb(users_namaz[user_id])
    )


async def missed_action_handler(call: CallbackQuery, callback_data: PrayerCallback):
    user_id = call.from_user.id
    name = callback_data.name
    action = callback_data.action

    user_namaz = users_namaz[user_id]

    if action == "plus":
        user_namaz[name] += 1
    elif action == "minus":
        user_namaz[name] = max(0, user_namaz[name] - 1)

    await call.message.edit_reply_markup(reply_markup=missed_fajr_kb(user_namaz))
