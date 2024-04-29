from sqlmodel import SQLModel, Session, select
from sqlalchemy.orm.session import Session as SSession
from typing import Any
from abstract.repository import AbstractRepository
from models.security.token import TokenTracker
from sqlalchemy.types import Uuid
from typing import List, Optional
from uuid import UUID as pyUUID
import uuid

class TokenRepository(AbstractRepository):

    def __init__(self, engine_type: str | None = None):
        if engine_type is not None:
            self.new_session(engine_type=engine_type)

    
    def add(self, model: TokenTracker) -> TokenTracker:
        """
        Adds a TokenTracker model to the repository.

        Args:
            model (TokenTracker): The TokenTracker model to be added.

        Returns:
            TokenTracker: The added TokenTracker model.
        """
        super().add(model=model)
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
        result = self.session.exec(statement=statement)
        return result.first()
    
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