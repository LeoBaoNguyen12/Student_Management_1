from sqlalchemy.orm import Session
from typing import List, Optional

from app import models, schemas


def get_all(db: Session) -> List[models.SinhVien]:
    return db.query(models.SinhVien).all()


def get_by_id(db: Session, sinh_vien_id: int) -> Optional[models.SinhVien]:
    return db.query(models.SinhVien).filter(models.SinhVien.id == sinh_vien_id).first()


def create(db: Session, data: schemas.SinhVienCreate) -> models.SinhVien:
    sv = models.SinhVien(**data.dict())
    db.add(sv)
    db.commit()
    db.refresh(sv)
    return sv


def update(db: Session, sinh_vien_id: int, data: schemas.SinhVienUpdate) -> Optional[models.SinhVien]:
    sv = get_by_id(db, sinh_vien_id)
    if not sv:
        return None

    update_data = data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(sv, field, value)

    db.commit()
    db.refresh(sv)
    return sv


def delete(db: Session, sinh_vien_id: int) -> bool:
    sv = get_by_id(db, sinh_vien_id)
    if not sv:
        return False
    db.delete(sv)
    db.commit()
    return True