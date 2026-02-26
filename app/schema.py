from pydantic import BaseModel, EmailStr
from typing import Optional


class SinhVienBase(BaseModel):
    ho_ten: str
    lop: Optional[str] = None
    email: Optional[EmailStr] = None


class SinhVienCreate(SinhVienBase):
    pass


class SinhVienUpdate(BaseModel):
    ho_ten: Optional[str] = None
    lop: Optional[str] = None
    email: Optional[EmailStr] = None


class SinhVienOut(SinhVienBase):
    id: int

    class Config:
        orm_mode = True