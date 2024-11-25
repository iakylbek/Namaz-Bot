from aiogram.types import Message

namazs_list = [
    ["\U0001F305 Фаджр", "\U00002705\n"],
    ["\U0001F54C Зухр", "\U00002705\n"],
    ["\U0001F3D9 Аср", "\U00002705\n"],
    ["\U0001F304 Магриб", "\U0000274c\n"],
    ["\U0001F303 Иша", "\U0001f55c\n"],
]


async def statistics_handler(message: Message) -> None:
    text = "\U0001f4ca Статистика за сегодня:\n\n"

    for name, status in namazs_list:
        text += f"• *{name:<20}* {status}"

    await message.answer(text, parse_mode="Markdown")
