from sqlalchemy import Column, Integer, String
from .db import Base, init_db


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, unique=True, nullable=False)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    city = Column(String, nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, user_id={self.user_id}, username={self.username})>"

if __name__ == "__main__":
    init_db()
