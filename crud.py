from sqlalchemy.orm import Session
from . import models
from schemas import schemas

def get_phone(db: Session, phone_id: int):
    return db.query(models.Phone).filter(models.Phone.id == phone_id).first()

def get_phones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Phone).offset(skip).limit(limit).all()

def create_phone(db: Session, phone: schemas.PhoneCreate):
    db_phone = models.Phone(name=phone.name, year=phone.year, ram=phone.ram, color=phone.color)
    db.add(db_phone)
    db.commit()
    db.refresh(db_phone)
    return db_phone

def update_phone(db: Session, phone_id: int, phone: schemas.PhoneUpdate):
    db_phone = db.query(models.Phone).filter(models.Phone.id == phone_id).first()
    if db_phone:
        for key, value in phone.dict(exclude_unset=True).items():
            setattr(db_phone, key, value)
        db.commit()
        db.refresh(db_phone)
    return db_phone

def delete_phone(db: Session, phone_id: int):
    db_phone = db.query(models.Phone).filter(models.Phone.id == phone_id).first()
    if db_phone:
        db.delete(db_phone)
        db.commit()
        return True
    return False