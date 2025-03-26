from abc import ABC, abstractmethod
from typing import Dict, Any, List
from .header_interface import HeaderInterface
from .body_create_reva_order import BodyCreateRevaOrder

class VifoCreateRevaOrderInterface(ABC):
    @abstractmethod
    def validate_reva_order(self, headers: HeaderInterface, body: BodyCreateRevaOrder) -> List[str]:
        pass
    
    @abstractmethod
    async def create_reva_order(self, headers: HeaderInterface, body: BodyCreateRevaOrder) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    async def terminate_va(self, headers, id):
        pass