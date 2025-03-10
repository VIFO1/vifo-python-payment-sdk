from abc import ABC, abstractmethod
from typing import List, Dict, Any
from .header_login_interface import HeaderLoginInterface
from .body_authenticate_interface import BodyAuthenticateInterface

class VifoAuthenticateInterface(ABC):
    @abstractmethod
    def validate_login_input(self, headers: HeaderLoginInterface, body: BodyAuthenticateInterface) -> List[str]:
        pass
    
    @abstractmethod
    async def authenticate_user(self, headers: HeaderLoginInterface, body: BodyAuthenticateInterface) -> Dict[str, Any]:
        pass