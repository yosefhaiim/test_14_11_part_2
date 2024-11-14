from sqlalchemy import Column, Integer,Float, String, Date, Table, ForeignKey  # ייבוא מחלקים שונים של SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base  # ייבוא פונקציה ליצירת מודלים
from sqlalchemy.orm import relationship  # ייבוא פונקציה ליצירת קשרים בין מודלים

from email_model import maile_device_location_sentence

Base = declarative_base()


class SentenceModel(Base):
    __tablename__ = 'Sentence'
    id = Column(Integer, primary_key=True)
    sentences = Column(String)

    relationship('EmailModel',
                 secondary=maile_device_location_sentence,
                 backref='Sentences',
                 )