from passlib.context import CryptContext
from cryptography.fernet import Fernet
from fastapi import HTTPException
import secrets
import os


class SecurityUtilities:
    pwd_context = CryptContext(schemes=["argon2"], argon2__salt_size=128, argon2__rounds=10)
    temp_key = Fernet.generate_key()
    SECRET_KEY: bytes

    # this hopefully will help multiple threads end up using same key.  
    # We will see this could be a source of a BUG with mutliple processes serving app
    @classmethod
    def check_key(cls) -> bytes:
        env_key_is = os.environ.get('ltg_key_42')
        # check env key is not set and secret key is set
        if env_key_is is None and cls.SECRET_KEY is not None:
                # env key is not set but we have a secret key lets sync those
                os.environ['ltg_key_42'] = cls.SECRET_KEY.decode('utf-8')
                # return key if we need it
                return cls.SECRET_KEY
        # we have a key in env lets sync with secret key
        elif env_key_is is not None:
            # lets check the key in env.  If is not the same as our secret key return secret key
            if cls.SECRET_KEY != env_key_is.encode('utf-8') and cls.SECRET_KEY is not None:
                # sync the env and our secret.  
                # Keeps it from being tampered with while app is running, or at least affecting us
                os.environ['ltg_key_42'] = cls.SECRET_KEY.decode('utf-8')
                return cls.SECRET_KEY
            # ok we have env key, but no Secret key so lets sync to env key
            elif cls.SECRET_KEY is None:
                cls.SECRET_KEY = env_key_is.encode('utf-8')
                return cls.SECRET_KEY
            # Ok env and secret match lets agree and return
            else:
                return cls.SECRET_KEY
        # THis means we have no keys lets use our temp_key to set them both and return
        else:
            cls.SECRET_KEY = cls.temp_key
            os.environ['ltg_key_42'] = cls.SECRET_KEY.decode('utf-8')
        return cls.SECRET_KEY

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
        SecurityUtilities.check_key()
        if key is None:
            key = SecurityUtilities.SECRET_KEY
        fernet_obj = Fernet(key)
        return fernet_obj.encrypt(bytes(message, 'utf-8'))
        
    @staticmethod
    def decrypt_token_content(cyphertext: str, key: bytes | None = None) -> bytes:
        b_cyphertext = bytes(cyphertext, 'utf-8')
        SecurityUtilities.check_key()
        if key is None:
            key = SecurityUtilities.SECRET_KEY
        fernet_obj = Fernet(key)
        return fernet_obj.decrypt(b_cyphertext)
    
credentails_exception = HTTPException(
    status_code=403, 
    detail="Could not validate credentials", 
    headers={"WWW-Authenticate": "Bearer"}
    )