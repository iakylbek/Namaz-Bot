from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from .start import UserSettings
from keyboards.settings_keyboard import city_kb


async def settings_handler(message: Message, state: FSMContext) -> None:
    text = (
        "\U00002699 Ваши текущие найстройки: \n"
        "*Город:*        Москва\n"
        "*Уведомления:*  Точное время\n\n"
    )
    # await message.answer(text)
    await message.answer(text + "\U0001f4cd Выберите город в котором проживаите: ", reply_markup=city_kb())
    await state.set_state(UserSettings.city)
