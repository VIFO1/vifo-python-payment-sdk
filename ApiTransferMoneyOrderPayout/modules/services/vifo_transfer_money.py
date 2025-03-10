from typing import List, Dict, Any

from modules.services.vifo_send_request import VifoSendRequest
from modules.interfaces.vifo_transfer_money_interface import VifoTransferMoneyInterface
from modules.interfaces.header_interface import HeaderInterface
from modules.interfaces.body_transfer_money import BodyTransferMoney

class VifoTransferMoney(VifoTransferMoneyInterface):
    def __init__(self, send_request: VifoSendRequest) -> None:
        self.send_request = send_request

    def validate_request_input(self, headers: HeaderInterface, body: BodyTransferMoney) -> List[str]:
        errors = []

        if headers is None or not isinstance(headers, dict):
            errors.append('headers must be a non-empty object')
        if body is None or not isinstance(body, dict):
            errors.append('body must be a non-empty object')
        return errors

    async def create_transfer_money(self, headers: HeaderInterface, body: BodyTransferMoney) -> Dict[str, Any]:
        endpoint = '/v2/finance'
        errors = self.validate_request_input(headers, body)
        if errors:
            return {"errors": errors}

        return await self.send_request.send_request('POST', endpoint, headers, body)