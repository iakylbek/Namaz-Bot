from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:postgres-password@localhost/namaz_bot"

Base = declarative_base()

# Создаем подключение к базе данных
engine = create_engine(DATABASE_URL)

# Создаем сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Функция для создания всех таблиц
def init_db():
    Base.metadata.create_all(bind=engine)
