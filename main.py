from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import models, crud, database
from database.database import engine, get_db
from schemas import schemas

# ایجاد جداول پایگاه داده
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/phones/", response_model=schemas.Phone)
def create_phone(phone: schemas.PhoneCreate, db: Session = Depends(get_db)):
    return crud.create_phone(db=db, phone=phone)

@app.get("/phones/", response_model=list[schemas.Phone])
def read_phones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_phones(db, skip=skip, limit=limit)

@app.get("/phones/{phone_id}", response_model=schemas.Phone)
def read_phone(phone_id: int, db: Session = Depends(get_db)):
    db_phone = crud.get_phone(db, phone_id=phone_id)
    if db_phone is None:
        raise HTTPException(status_code=404, detail="Phone not found")
    return db_phone

@app.put("/phones/{phone_id}", response_model=schemas.Phone)
def update_phone(phone_id: int, phone: schemas.PhoneUpdate, db: Session = Depends(get_db)):
    db_phone = crud.update_phone(db, phone_id=phone_id, phone=phone)
    if db_phone is None:
        raise HTTPException(status_code=404, detail="Phone not found")
    return db_phone

@app.delete("/phones/{phone_id}")
def delete_phone(phone_id: int, db: Session = Depends(get_db)):
    success = crud.delete_phone(db, phone_id=phone_id)
    if not success:
        raise HTTPException(status_code=404, detail="Phone not found")
    return {"message": "Phone deleted successfully"}