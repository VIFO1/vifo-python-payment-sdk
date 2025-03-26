from typing import List, Dict, Any

from modules.services.vifo_send_request import VifoSendRequest
from modules.interfaces.vifo_bank_interface import VifoBankInterface
from modules.interfaces.header_interface import HeaderInterface
from modules.interfaces.body_beneficiary_name import BodyBeneficiaryName

class VifoBank(VifoBankInterface):
    def __init__(self, send_request: VifoSendRequest) -> None:
        self.send_request = send_request

    def validate_body(self, headers: HeaderInterface, body: Dict[str, Any]) -> List[str]:
        errors = []

        if headers is None or not isinstance(headers, dict):
            errors.append('headers must be a non-empty object')
        if body is None or not isinstance(body, dict):
            errors.append('body must be a non-empty object')

        return errors

    async def get_bank(self, headers: HeaderInterface, body: Dict[str, Any]) -> Dict[str, Any]:
        endpoint = '/v2/data/banks/napas'
        errors = self.validate_body(headers, body)
        if errors:
            return {"errors": errors}

        return await self.send_request.send_request('GET', endpoint, headers, body)

    async def get_beneficiary_name(self, headers: HeaderInterface, body: BodyBeneficiaryName) -> Dict[str, Any]:
        endpoint = '/v2/finance/napas/receiver'
        errors = self.validate_body(headers, body)

        if errors:
            return {"errors": errors}
        return await self.send_request.send_request('POST', endpoint, headers, body)
