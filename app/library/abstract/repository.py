import abc
import os
from sqlmodel import SQLModel, Session
from ..database import Database


class AbstractRepository(abc.ABC):
    
    _session = None
    _db = None
    
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
        
    def new_session(self) -> Session:

        self.close_session(AbstractRepository._session)

        # TODO: Add config load for db configs, things like type
        AbstractRepository._db = Database(session=None, envrionment=None, engine_type='sqllite')
        AbstractRepository._session = AbstractRepository._db.get_session()()
        return AbstractRepository._session


    def close_session(self, session: Session):
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
        raise NotImplementedError
    
    @abc.abstractmethod
    def get(self, model, reference):
        raise NotImplementedError
    
    @abc.abstractmethod
    def update(self, model, data: SQLModel):
        raise NotImplementedError