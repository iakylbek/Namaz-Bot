from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.db_config import Base, init_db


class TimeNotify(Base):
    __tablename__ = "time_notify"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    time = Column(String, nullable=False)

    users = relationship("User", back_populates="time_notify")

    def __repr__(self):
        return f"<TimeNotify(id={self.id}, title={self.title}, time={self.time})>"


if __name__ == "__main__":
    init_db()
