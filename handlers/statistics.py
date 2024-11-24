from aiogram.types import Message
from tabulate import tabulate

namazs_list = [
    ["Фаджр", "\U00002705\n"],
    ["Зухр", "\U00002705\n"],
    ["Аср", "\U00002705\n"],
    ["Магриб", "\U0000274C\n"],
    ["Иша", "\U0001F55C\n"]
]
text = (f"\U0001F4CA Статистика намазов за сегодня:\n\n")

async def statistics_handler(message: Message) -> None:

    await message.answer(text + f"<pre>{tabulate(namazs_list, tablefmt="grid")}</pre>")
