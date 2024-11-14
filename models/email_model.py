from xmlrpc.client import DateTime

from sqlalchemy import Column, Integer,Float, String, Date, Table, ForeignKey  # ייבוא מחלקים שונים של SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base  # ייבוא פונקציה ליצירת מודלים
from sqlalchemy.orm import relationship  # ייבוא פונקציה ליצירת קשרים בין מודלים


from models.device_info_model import DeviceInfoModel
from models.location_model import LocationModel
from models.sentence_model import SentenceModel

Base = declarative_base()

maile_device_location_sentence = Table(
    'maile_device_location_sentence',
    Base.metadata,
    Column('email_id', Integer,ForeignKey('EmailModel.email_id')),
    Column('device_id', Integer,ForeignKey('Countries.country_id')),
    Column('location_id', Integer,ForeignKey('TargetTypes.target_type_id')),
    Column('sentence_id', Integer,ForeignKey('Targets.target_id')),
)




class EmailModel(Base):
    __tablename__ = 'Emails'
    email_id = Column(Integer, primary_key=True)
    device_id = Column(Integer, ForeignKey('Devices.device_id'))
    location_id = Column(Integer, ForeignKey('Locations.location_id'))
    sentence_id = Column(Integer, ForeignKey('Sentences.sentence_id'))

    email = Column(String)
    username = Column(String)
    ip_address = Column(String)
    created_at = Column(DateTime)

    devices_info = relationship('DeviceInfoModel',
                                secondary= maile_device_location_sentence,
                                backref='Emails')
    locations = relationship('LocationInfoModel'
                             ,secondary=maile_device_location_sentence,
                             back_populates='Emails')
    sentences = relationship('SentenceModel',
                             secondary=maile_device_location_sentence,
                             backref='Emails')
