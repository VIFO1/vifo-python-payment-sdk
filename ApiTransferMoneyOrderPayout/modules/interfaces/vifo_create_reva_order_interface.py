from abc import ABC, abstractmethod
from typing import Dict, Any
from .header_interface import HeaderInterface
from .body_create_reva_order import BodyCreateRevaOrder

class VifoCreateRevaOrderInterface(ABC):
    @abstractmethod
    async def create_reva_order(self, headers: HeaderInterface, body: BodyCreateRevaOrder) -> Dict[str, Any]:
        pass