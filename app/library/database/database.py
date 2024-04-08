import logging
from sqlmodel import Session, SQLModel, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import Engine
from contextlib import contextmanager


class SQLLiteDatabase:

    def __init__(self, session: Session | None, envrionment: str | None):

        if session is None:
            self.session = self.get_session()
        else:
            self.session = session
        
        SQLModel.metadata.create_all(self.get_engine('sqllite'))

    def get_session(self) -> Session:
        return sessionmaker(bind=self.get_engine('sqllite'), autoflush=True)
    
    def get_engine(self, type: str | None) -> Engine:
        
        if type is None:
            raise NotImplementedError
        elif type == 'sqllite':
            sqllite_url = f"sqlite:///test.db"
            connect_args = {"check_same_thread": False}
            return create_engine(sqllite_url, echo=True, connect_args=connect_args)
