from aiogram.types import Message


async def statistics_handler(message: Message) -> None:
    text = (
        f"Статистика намазов за сегодня:\n\n"
        "Утренний намаз:        \U00002705\n"
        "Обеденный намаз:       \U00002705\n"
        "Послеобеденный намаз:  \U0000274C\n"
        "Вечерний намаз:        \U0001F55C\n"
        "Ночной намаз:          \U0001F55C"
    )
    await message.answer(text)
