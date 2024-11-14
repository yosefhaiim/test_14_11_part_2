from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.email_model import Base
connection_url = "postgresql://admin:1234@localhost:5437/emails"

engine = create_engine(connection_url, convert_unicode=True)

b_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
def init_db():
    import models
    Base.metadata.create_all(bind=engine)
