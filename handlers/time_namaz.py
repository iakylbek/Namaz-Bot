from datetime import date

from aiogram.types import Message

from api.aladhan import AladhanAPI

namaz_names = [
    ["\U0001F54C Фаджр", "Fajr"],
    ["\U0001f305 Рассвет", "Sunrise"],
    ["\U0001f54c Зухр", "Dhuhr"],
    ["\U0001f3d9 Аср", "Asr"],
    ["\U0001f304 Магриб", "Maghrib"],
    ["\U0001f303 Иша", "Isha"],
]

async def time_namaz_handler(message: Message) -> None:
    today = date.today().strftime("%d.%m.%Y")
    data = await AladhanAPI.get_prayer_times_by_city(today, "Moscow", "RU")
    data_shia = await AladhanAPI.get_prayer_times_by_city(today, "Moscow", "RU", school=0)

    text = f"Время намазов на *{today}*\n" "В городе Москва\n\n"
    text += "`"
    for name, name_en in namaz_names:
        text += f"{name:<10}: {data["data"]["timings"][name_en]} "
        if name_en == "Asr":
            text += f"({data_shia["data"]["timings"]["Asr"]})"
        text += "\n"
    text += "`"
    await message.answer(text)
