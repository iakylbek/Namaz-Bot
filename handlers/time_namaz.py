from datetime import datetime
from aiogram.types import Message

namaz_times = [
        ["\U0001F305 Фаджр", "05:20", "\U00002705"],
        ["\U0001F54C Зухр", "12:30", "\U00002705"],
        ["\U0001F3D9 Аср", "15:45", "\U0000274c"],
        ["\U0001F304 Магриб", "18:10", "\U00002705"],
        ["\U0001F303 Иша", "19:30", "\U0001f55c"]
    ]

async def time_namaz_handler(message: Message) -> None:
    formatted_date = datetime.now().strftime("%d.%m.%Y")
    text = (
        f"Время намазов на *{formatted_date}*\n"
        "В городе Москва\n\n"
    )
    text += '`'
    for name, time, status in namaz_times:
        text += f"{name:<8}: {time} {status}\n"
    text += '`'
    
    text += "\*всемирная исламская лига"

    await message.answer(text)
