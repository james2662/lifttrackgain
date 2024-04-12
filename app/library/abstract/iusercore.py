import abc

class IUserCore(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def get_user_info(username: str):
        raise NotImplementedError
    
    @abc.abstractmethod
    def authenticate_user(self, password: str):
        raise NotImplementedError
    
    def __str__(self):
        attributes_list = [a for a in dir(self.__class__) if not a.startswith('__') and not a.startswith('_') and not callable(getattr(self,a))]

        str_return = ""
        for att_prop in attributes_list:
            str_return = f"{str_return} {att_prop}={getattr(self.__class__, att_prop, 'Not Found')}"

        return str_return
    
    def __repr__(self) -> str:
        return str(self)