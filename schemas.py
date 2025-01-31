from pydantic import BaseModel
from typing import Optional

class PhoneBase(BaseModel):
    name: str
    year: int
    ram: str
    color: str

class PhoneCreate(PhoneBase):
    pass

class PhoneUpdate(BaseModel):
    name: Optional[str] = None
    year: Optional[int] = None
    ram: Optional[str] = None
    color: Optional[str] = None


class Phone(PhoneBase):
    id: int

    class Config:
        orm_mode = True