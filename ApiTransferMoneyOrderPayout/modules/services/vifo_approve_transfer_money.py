from typing import Union, List, Dict, Any

from modules.services.vifo_send_request import VifoSendRequest
from modules.interfaces.vifo_approve_transfer_money_interface import VifoApproveTransferMoneyInterface
from modules.interfaces.header_interface import HeaderInterface
from modules.interfaces.body_approve_transfer_money import BodyApproveTransferMoney
from modules.common_functions.generate_signature import generate_signature
from modules.common_functions.validate_signature_inputs import validate_signature_inputs

class VifoApproveTransferMoney(VifoApproveTransferMoneyInterface):
    def __init__(self, send_request: VifoSendRequest) -> None:
        self.send_request = send_request

    def create_signature(self, secret_key: str, timestamp: str, body: BodyApproveTransferMoney) -> Union[str, List[str]]:
        errors = validate_signature_inputs(secret_key, timestamp, body)
        if errors:
            return [f"Error: {error}" for error in errors]

        return generate_signature(secret_key, timestamp, body)

    async def approve_transfers(self, secret_key: str, timestamp: str, headers: HeaderInterface, body: BodyApproveTransferMoney) -> Dict[str, Any]:
        errors = validate_signature_inputs(secret_key, timestamp, body)
        if errors:
            return {"errors": [f"Error: {error}" for error in errors]}

        endpoint = '/v2/finance/confirm'
        return await self.send_request.send_request('POST', endpoint, headers, body)