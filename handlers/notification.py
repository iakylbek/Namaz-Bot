from aiogram.types import Message, CallbackQuery
from keyboards.notification_keyboard import (
    notification_kb,
    last_notification_kb,
    MarkingCallback,
)


async def notification_handler(message: Message) -> None:
    text = "\U0001f55c 5:43\nНаступило время Фаджра"
    await message.answer(text, reply_markup=notification_kb())

    text_2 = "\U00002757 Последнее напоминание:"
    await message.answer(text_2, reply_markup=last_notification_kb())


async def marking_namaz_handler(call: CallbackQuery, callback_data: MarkingCallback):
    if callback_data.status == "mark":
        await call.message.answer("Фаджр намаз прочитан")
    elif callback_data.status == "missed":
        await call.message.answer("Фаджр намаз пропущен")
    elif callback_data.status == "postpone":
        await call.message.answer("Фаджр намаз отложен на 30 мин")
