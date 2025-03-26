from abc import ABC, abstractmethod
from typing import List, Dict, Any
from .header_interface import HeaderInterface

class VifoOtherRequestInterface(ABC):
    @abstractmethod
    def validate_order_key(self, headers: HeaderInterface, key: str) -> List[str]:
        pass
    
    @abstractmethod
    async def check_order_status(self, headers: HeaderInterface, key: str) -> Dict[str, Any]:
        pass