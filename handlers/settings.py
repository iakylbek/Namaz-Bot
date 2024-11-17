from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from .start import UserSettings
from keyboards.settings_keyboard import city_kb


async def settings_handler(message: Message, state: FSMContext) -> None:
    text = (
        f"\U00002699 Ваши текущие найстройки: \n\n"
        "Город:        Москва\n"
        "Мазхаб:       Ханафи\n"
        "Уведомления:  Точное время"
    )
    await message.answer(text)
    await message.answer("\U0001F4CD Выберите город: ", reply_markup=city_kb())
    await state.set_state(UserSettings.city)
