from aiogram.types import Message


async def command_help_handler(message: Message) -> None:
    """
    This handler receives messages with `/help` command
    """
    help_text = ("Как работает бот?\n"
                 "1. Бот присылает напоминание о времени намаза согласно вашим настройкам.\n"
                 "2. Вы можете отслеживать свои намазы и отмечать пропущенные.\n"
                 "3. Настройки можно изменить с помощью команды \"Настройки\".")
    await message.answer(help_text)
