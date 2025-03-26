from typing import Dict, Any, Optional, Union, List
import os
from dotenv import load_dotenv
load_dotenv()

from modules.services.vifo_send_request import VifoSendRequest
from modules.services.vifo_authenticate import VifoAuthenticate
from modules.services.vifo_bank import VifoBank
from modules.services.vifo_approve_transfer_money import VifoApproveTransferMoney
from modules.services.vifo_webhook import VifoWebhookService
from modules.services.vifo_create_seva_order import VifoCreateSevaOrder
from modules.services.vifo_create_reva_order import VifoCreateRevaOrder
from modules.interfaces.header_interface import HeaderInterface
from modules.interfaces.header_login_interface import HeaderLoginInterface
from modules.interfaces.body_authenticate_interface import BodyAuthenticateInterface
from modules.interfaces.body_approve_transfer_money import BodyApproveTransferMoney
from modules.interfaces.body_webhook import WebhookBody
from modules.interfaces.body_create_reva_order import BodyCreateRevaOrder
from modules.interfaces.body_create_seva_order import BodyCreateSevaOrder

class VifoServiceFactory:
    def __init__(self, env: str) -> None:
        self.env = env
        self.send_request = VifoSendRequest(self.env)
        self.webhook = VifoWebhookService(self.send_request)
        self.auth = VifoAuthenticate(self.send_request)
        self.bank = VifoBank(self.send_request)
        self.approve_transfer = VifoApproveTransferMoney(self.send_request)
        self.order_seva = VifoCreateSevaOrder(self.send_request)
        self.order_reva = VifoCreateRevaOrder(self.send_request)

        access_token = os.getenv("ACCESS_TOKEN")
        self.headers = HeaderInterface(
            Accept="application/json",
            Content_Type="application/json",
            Authorization=f"Bearer {access_token}",
            x_request_timestamp="2025-03-06T12:00:00Z",
            x_request_signature="sample_signature"
        )

        self.headers_login = HeaderLoginInterface(
            Accept='application/json',
            Accept_Encoding='gzip, deflate',
            Accept_Language='en-US',
        )
        
        self.user_token: Optional[str] = None

    def set_token(self, token: str) -> None:
        self.user_token = token

    def get_authorization_headers(self) -> HeaderInterface:
        headers = self.headers.copy()
        if self.user_token:
            headers['Authorization'] = f'Bearer {self.user_token}'
        headers['x-request-timestamp'] = None
        headers['x-request-signature'] = None
        return headers

    async def authenticate_user(self, body: BodyAuthenticateInterface,headers: HeaderLoginInterface ) -> Dict[str, Any]:
        response = await self.auth.authenticate_user(headers, body)
        return response

    async def fetch_bank_info(self, body: Dict[str, Any]) -> Dict[str, Any]:
        headers = self.get_authorization_headers()
        return await self.bank.get_bank(headers, body)

    async def approve_money_transfer(self, secret_key: str, timestamp: str, body: BodyApproveTransferMoney) -> Dict[str, Any]:
        headers = self.get_authorization_headers()
        request_signature = self.approve_transfer.create_signature(secret_key, timestamp, body)
        headers['x-request-timestamp'] = timestamp
        headers['x-request-signature'] = request_signature
        return await self.approve_transfer.approve_transfers(secret_key, timestamp, headers, body)

    async def send_webhook(self, secret_key: str, timestamp: str, body: WebhookBody) -> Dict[str, Any]:
        headers = self.get_authorization_headers()
        request_signature = self.webhook.create_signature(secret_key, timestamp, body)
        headers['x-request-timestamp'] = timestamp
        headers['x-request-signature'] = request_signature
        return await self.webhook.send_webhook(secret_key, timestamp, headers, body)

    async def create_seva_order(self, body: BodyCreateSevaOrder) -> Dict[str, Any]:
        headers = self.get_authorization_headers()
        return await self.order_seva.create_seva_order(headers, body)

    async def create_reva_order(self, body: BodyCreateRevaOrder) -> Dict[str, Any]:
        headers = self.get_authorization_headers()
        return await self.order_reva.create_reva_order(headers, body)
