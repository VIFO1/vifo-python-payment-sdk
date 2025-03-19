from typing import List, Dict, Any

from modules.services.vifo_send_request import VifoSendRequest
from modules.interfaces.header_interface import HeaderInterface
from modules.interfaces.vifo_create_reva_order_interface import VifoCreateRevaOrderInterface
from modules.interfaces.body_create_reva_order import BodyCreateRevaOrder

class VifoCreateRevaOrder(VifoCreateRevaOrderInterface):
    def __init__(self, send_request: VifoSendRequest) -> None:
        self.send_request = send_request

    def validate_reva_order(self, headers: HeaderInterface, body: BodyCreateRevaOrder) -> List[str]:
        errors = []

        if not isinstance(headers, dict): 
            errors.append('headers must be a non-empty object')
        if not isinstance(body, dict):
            errors.append('body must be a non-empty object')
        required_fields = [
            'product_code',
            'distributor_order_number',
            'phone',
            'fullname',
            'final_amount',
            'benefiary_account_name',
            'comment',
        ]
        
        for field in required_fields:
            if not getattr(body, field, None):
                errors.append(f'{field} cannot be empty.')
        return errors

    async def create_reva_order(self, headers: HeaderInterface, body: BodyCreateRevaOrder) -> Dict[str, Any]:
        errors = self.validate_reva_order(headers, body)
        if errors:
            return {"errors": errors}
        endpoint = '/v2/finance'

        return await self.send_request.send_request('POST', endpoint, headers, body)
    
    async def terminate_va(self, headers, id):
        endpoint = f'/v2/finance/{id}/terminate'
        
        return await self.send_request.send_request('PUT', endpoint, headers, {})
