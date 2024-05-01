from sqlmodel import SQLModel, Session, select
from sqlalchemy.orm.session import Session as SSession
from typing import Any
from library.abstract.repository import AbstractRepository
from models.security.token import TokenTracker
from sqlalchemy.types import Uuid
from typing import List, Optional
from uuid import UUID as pyUUID
import uuid

class TokenRepository(AbstractRepository):

    def __init__(self, engine_type: str | None = 'sqllite'):
        if engine_type is not None:
            self.session = self.new_session(engine_type=engine_type)
            self.engine_type = engine_type
        if engine_type == 'sqllite':
            with self._db.get_scoped_session() as session:
                self.session = session
    
    def add(self, model: TokenTracker) -> TokenTracker:
        """
        Adds a TokenTracker model to the repository.

        Args:
            model (TokenTracker): The TokenTracker model to be added.

        Returns:
            TokenTracker: The added TokenTracker model.
        """
        self.session.add(model)
        self.session.commit()
        self.session.flush()
        return model
    
    def get(self, model, reference: str) -> TokenTracker | None:
        """
        Retrieve a TokenTracker object from the database based on the provided reference.

        Args:
            model: The model class representing the TokenTracker table.
            reference: The access token reference to search for.

        Returns:
            The TokenTracker object matching the reference, or None if not found.
        """
        statement = select(TokenTracker).where(TokenTracker.access_token == reference)
        # Despite below error this would be an instance of SQLModels Session and not SQLAlchemy
        result = self.session.query(TokenTracker).where(TokenTracker.access_token == reference).first()
        return result
    
    def update(self, data: TokenTracker) -> TokenTracker:
        """
        Updates the token repository with the given data.

        Args:
            data (TokenTracker): The data to update the repository with.

        Returns:
            TokenTracker: The updated token repository.
        """
        super().update(data)
        return data

    def remove(self, data: TokenTracker) -> None:
        """
        Removes the given TokenTracker object from the database.

        Args:
            data (TokenTracker): The TokenTracker object to be removed.

        Returns:
            None
        """
        self.session.delete(data)
        self.session.commit()
        self.session.flush()
        return None