from aiogram.types import Message
from keyboards.notification_keyboard import notification_kb, last_notification_kb


async def notification_handler(message: Message) -> None:
    text = "\U0001f55c 5:43\nНаступило время Фаджра"
    await message.answer(text, reply_markup=notification_kb())

    text_2 = "Последнее напоминание:"
    await message.answer(text_2, reply_markup=last_notification_kb())
