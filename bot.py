import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import TOKEN
from keyboards.notification_keyboard import MarkingCallback
from handlers import *

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

# Register handlares
dp.message.register(command_start_handler, CommandStart())
dp.message.register(command_help_handler, Command("help"))

dp.message.register(time_namaz_handler, F.text == "Время намаза")
dp.message.register(statistics_handler, F.text == "Статистика за сегодня")
dp.message.register(settings_handler, F.text == "Настройки")
dp.message.register(missed_namaz_handler, F.text == "Пропущенные намазы")
dp.callback_query.register(missed_action_handler, PrayerCallback.filter())
dp.message.register(notification_handler, F.text == "Пример")
dp.callback_query.register(marking_namaz_handler, MarkingCallback.filter())

dp.callback_query.register(city_chosen_handler, UserSettings.city)
dp.callback_query.register(madhab_chosen_handler, UserSettings.madhab)
dp.callback_query.register(notification_chosen, UserSettings.notification)

dp.message.register(echo_handler)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
