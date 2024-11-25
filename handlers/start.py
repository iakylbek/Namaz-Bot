from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards.menu_keyborad import menu_kb
from keyboards.settings_keyboard import city_kb, madhab_kb, notification_time_kb


class UserSettings(StatesGroup):
    city = State()
    madhab = State()
    notification = State()


async def command_start_handler(message: Message, state: FSMContext) -> None:
    text = (
        f"Привет, {(message.from_user.full_name)}! \U0001f44b\n\n"
        "Добро пожаловать в бот для напоминания о времени намаза."
        "Чтобы начать, пожалуйста, выберите город в котором проживаете.\n\n"
        "\U0001f4cd Город:"
    )
    await message.answer(text, reply_markup=city_kb())
    await state.set_state(UserSettings.city)


async def city_chosen_handler(callback_query: CallbackQuery, state: FSMContext) -> None:
    text = "Выберите свой мазхаб, чтобы мы корректно рассчитали время намаза.\n"

    await state.update_data(city=callback_query.data)
    await callback_query.message.answer(text, reply_markup=madhab_kb())
    await state.set_state(UserSettings.madhab)


async def madhab_chosen_handler(
    callback_query: CallbackQuery, state: FSMContext
) -> None:
    text = "Теперь выберите, когда вы хотите получать напоминание о начале намаза:"

    await state.update_data(madhab=callback_query.data)
    await callback_query.message.answer(text, reply_markup=notification_time_kb())
    await state.set_state(UserSettings.notification)


async def notification_chosen(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(notification_time=callback_query.data)
    settings = await state.get_data()
    text = (
        "\U00002699 Ваши настройки:\n"
        f"*Город:* {settings["city"]:>21}\n"
        f"*Мазхаб:* {settings["madhab"]:>18}\n"
        f"*Уведомления:* {settings["notification_time"]:<10}\n"
    )
    await callback_query.message.answer(text)
    await callback_query.message.answer(
        "\U0001f389 Настройки успешно сохранены", reply_markup=menu_kb(), parse_mode="Markdown"
    )
    await state.clear()
