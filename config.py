from os import getenv
from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv("TOKEN")

DATABASE_URL = getenv("DATABASE_URL")

if not DATABASE_URL or not TOKEN:
    raise ValueError("Не заданы переменные окружения!")
