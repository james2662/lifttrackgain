import logging
from h11 import Data
from sqlmodel import Session, SQLModel, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session as SSession
from sqlalchemy.future import Engine
from contextlib import contextmanager
from models import *


class Database:

    engine_types = ('sqllite')
    db_session: SSession | None

    def __init__(self, session: SSession | Session | None, envrionment: str | None, engine_type: str | None):
        # testing engine_type is 'sqllite'
        if engine_type is None or engine_type not in Database.engine_types:
            raise NotImplementedError
        
        self.engine_type = engine_type
        
        if session is None:
            Database.db_session = self.get_new_session()
        else:
            Database.db_ession = session
        
        SQLModel.metadata.create_all(self.get_engine(engine_type))

    def get_new_session(self) -> sessionmaker[SSession]:
        return sessionmaker(bind=self.get_engine(self.engine_type), autoflush=True)
    
    def get_session(self) -> SSession:
        if Database.db_session is not None:
            return Database.db_session
        else: 
            Database.db_session = self.get_new_session()
            return Database.db_session()
    
    def get_engine(self, engine_type: str | None) -> Engine:
        
        if engine_type != 'sqllite':
            # TODO update to different SQL Types to return eninge or raise NotImplementedError
            raise NotImplementedError
        else:
            sqllite_url = f"sqlite:///test.db"
            connect_args = {"check_same_thread": False}
            return create_engine(sqllite_url, echo=True, connect_args=connect_args)
