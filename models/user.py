from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.db_config import Base, init_db
from models.city import City
from models.time_notify import TimeNotify


class User(Base):
    __tablename__ = "users"

    # Primary key
    id = Column(Integer, primary_key=True, autoincrement=True)

    # User Column
    user_id = Column(Integer, unique=True, nullable=False)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)

    # Foriegn realations
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=True)
    city = relationship(City, back_populates="users")

    time_notify_id = Column(Integer, ForeignKey("time_notify.id"), nullable=True)
    time_notify = relationship(TimeNotify, back_populates="users")

    # Вывод в консоль
    def __repr__(self):
        return f"<User(id={self.id}, user_id={self.user_id}, username={self.username})>"


if __name__ == "__main__":
    init_db()
