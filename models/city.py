from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.db_config import Base, init_db


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=True)

    # Relationship
    users = relationship("User", back_populates="city")

    def __repr__(self):
        return f"<City(id={self.id}, name={self.name}, country={self.country})>"


if __name__ == "__main__":
    init_db()
