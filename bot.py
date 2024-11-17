import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command

from config import TOKEN
from handlers import *

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

# Register handlares
dp.message.register(command_start_handler, CommandStart())
dp.message.register(command_help_handler, Command("help"))

dp.message.register(time_namaz_handler, F.text == 'Время намаза')
dp.message.register(statistics_handler, F.text == 'Статистика за сегодня')
dp.message.register(settings_handler, F.text == 'Настройки')
dp.message.register(notification_handler, F.text == 'Пример')

dp.callback_query.register(city_chosen_handler, UserSettings.city)
dp.callback_query.register(madhab_chosen_handler, UserSettings.madhab)
dp.callback_query.register(notification_chosen, UserSettings.notification)

dp.message.register(echo_handler)

async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
