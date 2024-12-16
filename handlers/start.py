from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from sqlalchemy.orm import Session

from keyboards.menu_keyborad import menu_kb
from keyboards.settings_keyboard import city_kb, notification_time_kb
from models.user import User
from models.city import City
from models.db_config import SessionLocal


class UserSettings(StatesGroup):
    city = State()
    notification = State()


async def command_start_handler(message: Message, state: FSMContext) -> None:
    text = (
        f"Привет, {(message.from_user.full_name)}! \U0001f44b\n\n"
        "Добро пожаловать в бот для напоминания о времени намаза."
        "Чтобы начать, пожалуйста, настройте бот."
    )
    text_choose = "Выберите город в котором проживаете\n\U0001f4cd Город:"
    await message.answer(text)
    await message.answer(text_choose, reply_markup=city_kb())
    await state.set_state(UserSettings.city)


async def city_chosen_handler(callback_query: CallbackQuery, state: FSMContext) -> None:
    text = "Как часто напоминать о намаза, если намаз не был отмечен прочитанным?"

    await state.update_data(city=callback_query.data)
    await callback_query.message.answer(text, reply_markup=notification_time_kb())
    await callback_query.message.delete()
    await state.set_state(UserSettings.notification)


async def notification_chosen(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(notification_time=callback_query.data)
    settings = await state.get_data()
    
    text = (
        "\U00002699 Ваши настройки:\n"
        f"*Город:* {settings["city"]:>21}\n"
        f"*Уведомления:* {settings["notification_time"]:<10}\n"
    )
    
    session: Session = SessionLocal()
    existing_user = session.query(User).filter_by(user_id=callback_query.from_user.id).first()
    city = session.query(City).filter(City.id == 1).first()

    if existing_user is None:
        new_user = User(
            user_id=callback_query.from_user.id,
            username=callback_query.from_user.username,
            first_name=callback_query.from_user.first_name,
            last_name=callback_query.from_user.last_name,
            city = city
        )
        session.add(new_user)

    else:
        existing_user.city = city
        pass

    session.commit()
    session.close()
    await callback_query.message.answer(text)
    await callback_query.message.delete()
    await callback_query.message.answer(
        "\U0001f389 Настройки успешно сохранены",
        reply_markup=menu_kb(),
        parse_mode="Markdown",
    )
    await state.clear()
