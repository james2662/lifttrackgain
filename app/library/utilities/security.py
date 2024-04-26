from passlib.context import CryptContext
from cryptography.fernet import Fernet
from fastapi import HTTPException
import secrets

class SecurityUtilities:
    pwd_context = CryptContext(schemes=["argon2"], argon2__salt_size=128, argon2__rounds=10)
    temp_key = Fernet.generate_key()

    @staticmethod
    def verify_a2_hash(plain_text, hashed_text) -> bool:
        try:
            if SecurityUtilities.pwd_context.verify(plain_text, hashed_text):
                return True
        except Exception as e:
            # TODO: log exceptions here
            return False
        return False
    
    @staticmethod
    def get_a2_hash(plain_text) -> str:
        return SecurityUtilities.pwd_context.hash(plain_text)
    
    @staticmethod
    def encrypt_token_content(message: str, key: bytes | None = None) -> bytes:
        if key is None:
            key = SecurityUtilities.temp_key
        fernet_obj = Fernet(key)
        return fernet_obj.encrypt(bytes(message, 'utf-8'))
        
    @staticmethod
    def decrypt_token_content(cyphertext: str, key: bytes | None = None) -> bytes:
        b_cyphertext = bytes(cyphertext, 'utf-8')
        if key is None:
            key = SecurityUtilities.temp_key
        fernet_obj = Fernet(key)
        return fernet_obj.decrypt(b_cyphertext)
    
credentails_exception = HTTPException(
    status_code=403, 
    detail="Could not validate credentials", 
    headers={"WWW-Authenticate": "Bearer"}
    )