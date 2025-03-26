from abc import ABC, abstractmethod
from typing import Union, List, Dict, Any
from .header_interface import HeaderInterface
from .body_approve_transfer_money import BodyApproveTransferMoney

class VifoApproveTransferMoneyInterface(ABC):
    @abstractmethod
    def create_signature(self, 
                         secret_key: str, 
                         timestamp: str, 
                         body: BodyApproveTransferMoney) -> Union[str, List[str]]:
        pass
    
    @abstractmethod
    async def approve_transfers(self, 
                                secret_key: str, 
                                timestamp: str, 
                                headers: HeaderInterface, 
                                body: BodyApproveTransferMoney) -> Dict[str, Any]:
        pass
