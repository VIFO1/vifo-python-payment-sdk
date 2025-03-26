from abc import ABC, abstractmethod
from typing import List, Dict, Any
from .header_interface import HeaderInterface
from .body_transfer_money import BodyTransferMoney

class VifoTransferMoneyInterface(ABC):
    @abstractmethod
    def validate_request_input(self, headers: HeaderInterface, body: BodyTransferMoney) -> List[str]:
        pass
    
    @abstractmethod
    async def create_transfer_money(self, headers: HeaderInterface, body: BodyTransferMoney) -> Dict[str, Any]:
        pass