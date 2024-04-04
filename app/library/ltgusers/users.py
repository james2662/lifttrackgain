from ..utilities.security import SecurityUtilities

class LTGUser:

    def __init__():
        raise NotImplementedError

    def get_user_info():
        raise NotImplementedError
    
    def _hash_password(plain_test: str) -> bytes:
        return SecurityUtilities.get_a2_hash(plain_text=plain_test)
    
    def validate_user():
        raise NotImplementedError
    
    def create_user():
        raise NotImplementedError
    
    def edit_user():
        raise NotImplementedError
    
    def login_user():
        raise NotImplementedError

