from sqlalchemy import Column, Integer, String
from .database import Base
class Phone(Base):
    __tablename__ = "phones"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    year = Column(Integer)
    ram = Column(String)
    color = Column(String)