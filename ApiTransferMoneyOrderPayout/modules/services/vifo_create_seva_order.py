from typing import List, Dict, Any

from modules.services.vifo_send_request import VifoSendRequest
from modules.interfaces.header_interface import HeaderInterface
from modules.interfaces.vifo_create_seva_order_interface import VifoCreateSevaOrderInterface
from modules.interfaces.body_create_seva_order import BodyCreateSevaOrder

class VifoCreateSevaOrder(VifoCreateSevaOrderInterface):
    def __init__(self, send_request: VifoSendRequest) -> None:
        self.send_request = send_request

    def _validate_seva_order(self, headers: HeaderInterface, body: BodyCreateSevaOrder) -> List[str]:
        errors = []
        if not isinstance(headers, dict):
            errors.append('headers must be a non-empty object')
        if not isinstance(body, dict):
            errors.append('body must be a non-empty object')
        required_fields = [
            'product_code',
            'phone',
            'fullname',
            'final_amount',
            'distributor_order_number',
            'benefiary_bank_code',
            'benefiary_account_no',
            'comment',
        ]

        for field in required_fields:
            if not body.get(field):
                errors.append(f'{field} cannot be empty.')
        return errors

    async def create_seva_order(self, headers: HeaderInterface, body: BodyCreateSevaOrder) -> Dict[str, Any]:
        errors = self._validate_seva_order(headers, body)
        if errors:
            return {"errors": errors}
        endpoint = '/v2/finance'

        return await self.send_request.send_request('POST', endpoint, headers, body)
    

    