from typing import List, Dict, Any

from modules.services.vifo_send_request import VifoSendRequest
from modules.interfaces.vifo_other_request_interface import VifoOtherRequestInterface
from modules.interfaces.header_interface import HeaderInterface

class VifoOtherRequest(VifoOtherRequestInterface):
    def __init__(self, send_request: VifoSendRequest) -> None:
        self.send_request = send_request

    async def validate_order_key(self, headers: HeaderInterface, key: str) -> List[str]:
        errors = []

        if not isinstance(headers, dict):
            errors.append('headers must be a non-empty object')

        if not isinstance(key, str) or not key:
            errors.append('Order key must be a string and cannot be empty')

        return errors

    async def check_order_status(self, headers: HeaderInterface, key: str) -> Dict[str, Any]:
        errors = self.validate_order_key(headers, key)
        if errors:
            return {"errors": errors}
        endpoint = f'/v2/finance/{key}/status'
        return await self.send_request.send_request('GET', endpoint, headers, {})