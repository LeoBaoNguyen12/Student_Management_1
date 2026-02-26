from sqlalchemy.orm import Session
from typing import List

from app import schemas
from app.repository import repository


def list_sinh_vien(db: Session) -> List[schemas.SinhVienOut]:
    sinh_viens = repository.get_all(db)
    return sinh_viens


def get_sinh_vien(db: Session, sinh_vien_id: int):
    return repository.get_by_id(db, sinh_vien_id) 


def create_sinh_vien(db: Session, data: schemas.SinhVienCreate):
    return repository.create(db, data) 


def update_sinh_vien(db: Session, sinh_vien_id: int, data: schemas.SinhVienUpdate):
    return repository.update(db, sinh_vien_id, data)


def delete_sinh_vien(db: Session, sinh_vien_id: int) -> bool:
    return repository.delete(db, sinh_vien_id)