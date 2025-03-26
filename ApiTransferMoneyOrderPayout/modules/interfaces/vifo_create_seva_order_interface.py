from abc import ABC, abstractmethod
from typing import Dict, Any, List
from .header_interface import HeaderInterface
from .body_create_seva_order import BodyCreateSevaOrder

class VifoCreateSevaOrderInterface(ABC):
    @abstractmethod
    def validate_seva_order(self, headers: HeaderInterface, body: BodyCreateSevaOrder) -> List[str]:
        pass
    
    @abstractmethod
    async def create_seva_order(self, headers: HeaderInterface, body: BodyCreateSevaOrder) -> Dict[str, Any]:
        pass
    
    
