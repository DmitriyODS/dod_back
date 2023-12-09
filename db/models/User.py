from sqlalchemy import Integer, Column, String, Boolean

from db import db, Base


class Customer(Base):
    __tablename__ = 'demo'
    user_id = Column(Integer, primary_key=True)
    fio = Column(String(255))
    email = Column(String(255))
    city = Column(String(255))
    school = Column(String(255))
    is_finished = Column(Boolean)
    type_mk = Column(Integer)
