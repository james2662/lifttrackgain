import abc
import os
from sqlmodel import SQLModel, Session, select
from sqlalchemy.orm.session import Session as SSession
from typing import Any
from ..database import Database


class AbstractRepository(abc.ABC):
    
    _session: Session | SSession | None = None
    _db: Database

    # TODO: Make a context manager here to handle exceptions and create new session on
    # DBAPIError exception, and others if needed

    @property
    def session(self):
        if AbstractRepository._session is not None and AbstractRepository._session:
            # TODO: add session validation here at some point
            return AbstractRepository._session
        else:
            return self.new_session()
    
    @session.setter
    def session(self, session: Session):
        AbstractRepository._session = session
        
    def new_session(self, engine_type: str = 'sqllite') -> SSession | Session:

        self.close_session(AbstractRepository._session)

        # TODO: Add config load for db configs, things like type
        AbstractRepository._db = Database(session=None, envrionment=None, engine_type=engine_type)
        AbstractRepository._session = AbstractRepository._db.get_session()
        return AbstractRepository._session


    def close_session(self, session: Session | SSession | None):
        if session and type(session) is Session:
            try: 
                session.flush()
            except Exception as e:
                # TODO: logging
                pass
            try:
                session.close()
            except Exception as e:
                # TODO: logging
                pass
        else:
            pass
    
    def __del__(self):
        self.close_session(self.session)

    @abc.abstractmethod
    def add(self, model: SQLModel):
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
    
    @abc.abstractmethod
    def get(self, model, reference) -> Any:
        model_type = type(model)
        statement = select(type(model)).where(type(model).id == reference)
        if self.session is not None:
            # SQLModel session is used, not SQLAlchemy, so error below is not true
            result = self.session.exec(statement=statement)
            return result.first()
        else:
            raise NotImplementedError
    
    @abc.abstractmethod
    def update(self, data: SQLModel):
        if self.session is not None:
            self.session.add(data)
            self.session.commit()
            self.session.refresh(data)
