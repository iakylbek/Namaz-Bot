from datetime import datetime
from aiogram.types import Message
from tabulate import tabulate

namaz_times = [
        ["\U0001F305 Фаджр", "05:20"],
        ["\U0001F54C Зухр", "12:30"],
        ["\U0001F3D9 Аср", "15:45"],
        ["\U0001F304 Магриб", "18:10"],
        ["\U0001F303 Иша", "19:30"]
    ]

async def time_namaz_handler(message: Message) -> None:
    """
    Handler will send message about namaz times for today
    """
    now = datetime.now()
    formatted_date = now.strftime("%d.%m.%Y")
    text = (
        f"\U0001F55C Время намазов на {formatted_date}\n"
        f"В городе Москва:\n<pre>{tabulate(namaz_times, tablefmt="grid")}</pre>"
    )
    await message.answer(text)
