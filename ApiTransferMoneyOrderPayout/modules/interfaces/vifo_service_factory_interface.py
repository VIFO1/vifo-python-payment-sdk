from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, Union
from .body_authenticate_interface import BodyAuthenticateInterface
from .header_interface import HeaderInterface
from .body_beneficiary_name import BodyBeneficiaryName
from .body_approve_transfer_money import BodyApproveTransferMoney
from .body_transfer_money import BodyTransferMoney
from .body_webhook import BodyWebhook
from .body_create_reva_order import QRTypeReva

class VifoServiceFactoryInterface(ABC):
    @abstractmethod
    def set_token_user(self, token: str) -> None:
        pass
    
    @abstractmethod
    def set_token_admin(self, token: str) -> None:
        pass
    
    @abstractmethod
    def get_authorization_headers(self, type_: str) -> HeaderInterface:
        pass
    
    @abstractmethod
    async def perform_user_authentication(self, body: BodyAuthenticateInterface) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    async def fetch_bank_information(self, body: Dict[str, Any]) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    async def fetch_beneficiary_name(self, body: BodyBeneficiaryName) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    async def execute_money_transfer(self, body: BodyTransferMoney) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    async def approve_money_transfer(self, secret_key: str, timestamp: str, 
                                    body: BodyApproveTransferMoney) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    async def verify_webhook_signature(self, data: BodyWebhook, request_signature: str, 
                                      secret_key: str, timestamp: str) -> bool:
        pass
    
    @abstractmethod
    async def process_other_request(self, key: str) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    async def create_reva_order(
        self,
        fullname: str,
        benefiary_account_name: str,
        product_code: Optional[str],
        distributor_order_number: str,
        phone: str,
        email: str,
        address: str,
        final_amount: float,
        comment: str,
        bank_detail: bool,
        qr_type: Optional[QRTypeReva],
        end_date: Optional[str]
    ) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    async def create_seva_order(
        self,
        product_code: Optional[str],
        phone: str,
        fullname: str,
        final_amount: float,
        distributor_order_number: str,
        benefiary_bank_code: str,
        benefiary_account_no: str,
        comment: str,
        source_account_no: str
    ) -> Dict[str, Any]:
        pass