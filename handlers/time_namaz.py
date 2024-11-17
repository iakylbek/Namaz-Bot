from datetime import datetime
from aiogram.types import Message


async def time_namaz_handler(message: Message) -> None:
    """
    Handler will send message about namaz times for today
    """
    now = datetime.now()
    formatted_date = now.strftime("%d.%m.%Y")
    text = (
        f"Время намазов на {formatted_date}\n"
        "В городе Москва:\n\n"
        "Утренний намаз:        05:20\n"
        "Обеденный намаз:       12:30\n"
        "Послеобеденный намаз:  15:45\n"
        "Вечерний намаз:        18:10\n"
        "Ночной намаз:          19:30"
    )
    await message.answer(text)
