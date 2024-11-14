from sqlalchemy import Column, Integer,Float, String, Date, Table, ForeignKey  # ייבוא מחלקים שונים של SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base  # ייבוא פונקציה ליצירת מודלים
from sqlalchemy.orm import relationship  # ייבוא פונקציה ליצירת קשרים בין מודלים

from models.email_model import maile_device_location_sentence

Base = declarative_base()





class DeviceInfoModel(Base):
    __tablename__ = 'DevicesInfo'
    device_id = Column(Integer, ForeignKey('Devices.device_id'), primary_key=True)
    browser = Column(String)
    os = Column(String)

    countries = relationship('Countries',
                             secondary=maile_device_location_sentence,
                             backref='DevicesInfo',
                             )

