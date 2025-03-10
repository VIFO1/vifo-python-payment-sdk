from abc import ABC, abstractmethod
from typing import List, Dict, Any
from .header_interface import HeaderInterface
from .body_beneficiary_name import BodyBeneficiaryName

class VifoBankInterface(ABC):
    @abstractmethod
    def validate_body(self, headers: HeaderInterface, body: object) -> List[str]:
        pass
    
    @abstractmethod
    async def get_bank(self, headers: HeaderInterface, body: BodyBeneficiaryName) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    async def get_beneficiary_name(self, headers: HeaderInterface, body: BodyBeneficiaryName) -> Dict[str, Any]:
        pass