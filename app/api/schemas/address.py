from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..libs.database import Base
from ..security.schemas.oauthuser import OauthUser


class UserAddress(Base):
    __tablename__ = "useraddresses"
    
    id = Column(Integer, primary_key=True, index=True)
    street_1 = Column(String, nullable=False)
    street_2 = Column(String, nullable=True)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)
    primary = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey=OauthUser.id)
    