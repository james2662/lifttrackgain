import abc
import os
from sqlmodel import SQLModel, Session, select
from sqlalchemy.orm.session import Session as SSession
from typing import Any
from ..database import Database
from contextlib import contextmanager


class AbstractRepository(abc.ABC):
    """
    Abstract base class for repositories.

    This class provides a common interface for repositories that interact with a database.
    Subclasses should implement the abstract methods defined in this class.

    Attributes:
        _session: The current session object.
        _db: The database object.

    """    
    _session: Session | SSession | None = None
    _db: Database

    # TODO: Make a context manager here to handle exceptions and create new session on
    # DBAPIError exception, and others if needed
    @contextmanager
    def get_scoped_session(self, engine_type: str = 'sqllite'):
        """Provide a transactional scope around a series of operations."""
        session = self.new_session(engine_type=engine_type)
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            self.close_session(session)

    @property
    def session(self):
        """
        Returns the session object for the repository.

        If the session object is already set, it is returned. Otherwise, a new session object is created and returned.

        Returns:
            The session object for the repository.
        """
        if AbstractRepository._session is not None and AbstractRepository._session:
            # TODO: add session validation here at some point
            return AbstractRepository._session
        else:
            return self.new_session()
    
    @session.setter
    def session(self, session: Session):
        """Set the session for the repository.

        Args:
            session (Session): The session to set.
        """
        AbstractRepository._session = session
        
    def new_session(self, engine_type: str = 'sqllite') -> SSession | Session:

        self.close_session(AbstractRepository._session)

        # TODO: Add config load for db configs, things like type
        AbstractRepository._db = Database(session=None, envrionment=None, engine_type=engine_type)
        AbstractRepository._session = AbstractRepository._db.get_session()
        return AbstractRepository._session


    def close_session(self, session: Session | SSession | None):
        """
        Closes the given session.

        Args:
            session (Session | SSession | None): The session to be closed.

        Returns:
            None
        """
        if session and type(session) is Session | SSession:
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
        """
        Adds a model to the repository.

        Args:
            model (SQLModel): The model to be added.

        Returns:
            None
        """
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
    
    @abc.abstractmethod
    def get(self, model, reference) -> Any:
        """
        Retrieve a record from the repository based on the provided model and reference.

        Args:
            model: The model class representing the record to retrieve.
            reference: The reference value used to identify the specific record.

        Returns:
            The retrieved record, or None if no record is found.

        Raises:
            NotImplementedError: If the repository does not have an active session.
        """
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
        """
        Updates the given data object in the repository.

        Args:
            data (SQLModel): The data object to be updated.

        Raises:
            NotImplementedError: This method should be implemented by the concrete repository class.
        """
        if self.session is not None:
            self.session.add(data)
            self.session.commit()
            self.session.refresh(data)
