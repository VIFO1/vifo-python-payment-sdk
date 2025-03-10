from typing import Dict, Any, Optional, Union, List

from modules.services.vifo_send_request import VifoSendRequest
from modules.services.vifo_authenticate import VifoAuthenticate
from modules.services.vifo_bank import VifoBank
from modules.services.vifo_transfer_money import VifoTransferMoney
from modules.services.vifo_approve_transfer_money import VifoApproveTransferMoney
from modules.services.webhook import Webhook
from modules.services.vifo_other_request import VifoOtherRequest
from modules.services.vifo_create_seva_order import VifoCreateSevaOrder
from modules.services.vifo_create_reva_order import VifoCreateRevaOrder
from modules.interfaces.vifo_service_factory_interface import VifoServiceFactoryInterface
from modules.interfaces.header_interface import HeaderInterface
from modules.interfaces.header_login_interface import HeaderLoginInterface
from modules.interfaces.body_authenticate_interface import BodyAuthenticateInterface
from modules.interfaces.body_beneficiary_name import BodyBeneficiaryName
from modules.interfaces.body_transfer_money import BodyTransferMoney
from modules.interfaces.body_approve_transfer_money import BodyApproveTransferMoney
from modules.interfaces.body_webhook import BodyWebhook
from modules.interfaces.body_create_reva_order import BodyCreateRevaOrder, QRTypeReva
from modules.interfaces.body_create_seva_order import BodyCreateSevaOrder, QRTypeSeva


class VifoServiceFactory(VifoServiceFactoryInterface):
    def __init__(self, env: str) -> None:
        self.env = env
        self.send_request = VifoSendRequest(self.env)
        self.webhook = Webhook(self.send_request)
        self.other_request = VifoOtherRequest(self.send_request)
        self.login_authenticate_user = VifoAuthenticate(self.send_request)
        self.bank = VifoBank(self.send_request)
        self.transfer_money = VifoTransferMoney(self.send_request)
        self.approve_transfer_money = VifoApproveTransferMoney(self.send_request)
        self.order_seva = VifoCreateSevaOrder(self.send_request)
        self.order_reva = VifoCreateRevaOrder(self.send_request)

        self.headers: HeaderInterface = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': None,
            'x-request-timestamp': None,
            'x-request-signature': None,
        }
        self.headers_login: HeaderLoginInterface = {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip',
            'Accept-Language': '*/*',
        }
        self.admin_token: Optional[str] = None
        self.user_token: Optional[str] = None 

    def set_token_user(self, token: str) -> None:
        self.user_token = token

    def set_token_admin(self, token: str) -> None:
        self.admin_token = token

    def get_authorization_headers(self, type: str) -> HeaderInterface:
        token = self.user_token if type == 'user' else self.admin_token
        headers = self.headers.copy()

        if token:
            headers['Authorization'] = f'Bearer {token}'
        headers['x-request-timestamp'] = None
        headers['x-request-signature'] = None
        return headers

    async def perform_user_authentication(self, body: BodyAuthenticateInterface) -> Dict[str, Any]:
        response = await self.login_authenticate_user.authenticate_user(self.headers_login, body)

        if 'body' in response:
            return {
                'status_code': response.get('status_code', ''),
                'body': response.get('body')
            }
        return response

    async def fetch_bank_information(self, body: Dict[str, Any]) -> Dict[str, Any]:
        headers = self.get_authorization_headers('user')
        response = await self.bank.get_bank(headers, body)
        if 'success' in response: 
            return {
                'body': response.get('body', ''),
                'status_code': response.get('status_code', '')
            }
        return response

    async def fetch_beneficiary_name(self, body: BodyBeneficiaryName) -> Dict[str, Any]:
        headers = self.get_authorization_headers('user')

        if (not('bank_code' in body) or not('account_number' in body)):
            return {
                'status': 'errors',
                'message': 'Required fields missing: bank_code or account_number.'
            }

        response = await self.bank.get_beneficiary_name(headers, body)
        return response

    async def execute_money_transfer(self, body: BodyTransferMoney) -> Dict[str, Any]:
        headers = self.get_authorization_headers('user')
        response = await self.transfer_money.create_transfer_money(headers, body)
        if 'success' in response:
            return {
                'message': response.get('body', '')
                }
        return response

    async def approve_money_transfer(self, secret_key: str, timestamp: str, body: BodyApproveTransferMoney) -> Dict[str, Any]:
        headers: HeaderInterface = self.get_authorization_headers('admin')
        request_signature = self.approve_transfer_money.create_signature(secret_key, timestamp, body)

        headers['x-request-timestamp'] = timestamp
        headers['x-request-signature'] = request_signature
        # if isinstance(request_signature, str) else request_signature[0] # Assuming first error or signature

        response = await self.approve_transfer_money.approve_transfers(secret_key, timestamp, headers, body)
        if 'errors' in response:
            return {
                'errors': response.get('errors'),
                'body': response.get('body', '')
            }
        return response

    async def verify_webhook_signature(self, data: BodyWebhook, request_signature: str, secret_key: str, timestamp: str) -> bool:
        result = await self.webhook.handle_signature(data, request_signature, secret_key, timestamp)
        return result is True

    async def process_other_request(self, key: str) -> Dict[str, Any]:
        headers = self.get_authorization_headers('user')
        response = await self.other_request.check_order_status(headers, key)
        if 'errors' in response:
            return {
                'errors': response.get('errors'),
                'status_code': response.get('status_code', ''),
                'body': response.get('body', '')
            }
        return response

    async def create_reva_order(
        self,
        fullname: str,
        benefiary_account_name: str,
        product_code: Optional[str] = None,
        distributor_order_number: str = "",
        phone: str = "",
        email: str = "",
        address: str = "",
        final_amount: float = 0.0,
        comment: str = "",
        bank_detail: bool = False,
        qr_type: Optional[QRTypeReva] = None,
        end_date: Optional[str] = None
    ) -> Dict[str, Any]:
        actual_product_code_reva = product_code or 'REVAVF240101'
        body: BodyCreateRevaOrder = {
            'fullname': fullname,
            'benefiary_account_name': benefiary_account_name,
            'product_code': actual_product_code_reva,
            'distributor_order_number': distributor_order_number,
            'phone': phone,
            'email': email,
            'address': address,
            'final_amount': final_amount,
            'comment': comment,
            'bank_detail': bank_detail,
            'qr_type': qr_type,
            'end_date': end_date,
        }

        headers = self.get_authorization_headers('user')
        response = await self.order_reva.create_reva_order(headers, body)
        if 'status_code' in response:
            return {
                'status_code': response.get('status_code'),
                'body': response.get('body', '')
            }
        return response

    async def create_seva_order(
        self,
        product_code: Optional[str] = None,
        phone: str = "",
        fullname: str = "",
        final_amount: float = 0.0,
        distributor_order_number: str = "",
        benefiary_bank_code: str = "",
        benefiary_account_no: str = "",
        comment: str = "",
        source_account_no: str = ""
    ) -> Dict[str, Any]:
        actual_product_code_seva = product_code or 'SEVAVF240101'
        body: BodyCreateSevaOrder = {
            'product_code': actual_product_code_seva,
            'phone': phone,
            'fullname': fullname,
            'final_amount': final_amount,
            'distributor_order_number': distributor_order_number,
            'benefiary_bank_code': benefiary_bank_code,
            'benefiary_account_no': benefiary_account_no,
            'comment': comment,
            'source_account_no': source_account_no
        }

        header = self.get_authorization_headers("user")
        response = await self.order_seva.create_seva_order(header, body)
        if 'status_code' in response:
            return{
                'status_code': response.get('status_code'),
                'body': response.get('body', '')
            }
        return response