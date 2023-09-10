from abc import ABC, abstractclassmethod, abstractproperty, abstractmethod
from sqlalchemy.orm import Session
from typing import Any

class Repository(ABC):

    # set up Session here
    @property
    def session(self) -> Session:
        return self._session
    
    @session.setter
    def session(self, session: Session) -> None:
        self._session = session

    @session.deleter
    def session(self) -> None:
        if self._session is not None and type(self._session) == Session:
            self._session.close()
        self._session = None
        return self._session
    
    @abstractmethod
    def get(self, schema, reference) -> Any:
        return NotImplementedError
    
    @abstractmethod
    def add(self, schema, reference) -> Any:
        return NotImplementedError
    
    @abstractmethod
    def update(self, schema, reference) -> Any:
        return NotImplementedError
    
    def __del__(self) -> None:
        if self._session is not None and type(self._session) == Session:
            self._session.close()
