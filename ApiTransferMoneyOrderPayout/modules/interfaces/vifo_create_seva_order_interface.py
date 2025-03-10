from abc import ABC, abstractmethod
from typing import Dict, Any
from .header_interface import HeaderInterface
from .body_create_seva_order import BodyCreateSevaOrder

class VifoCreateSevaOrderInterface(ABC):
    @abstractmethod
    async def create_seva_order(self, headers: HeaderInterface, body: BodyCreateSevaOrder) -> Dict[str, Any]:
        pass