from sqlalchemy import Column, Integer, String
from .database import Base


class SinhVien(Base):
    __tablename__ = "sinh_vien"

    id = Column(Integer, primary_key=True, index=True)
    ho_ten = Column(String, nullable=False)
    lop = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=True)