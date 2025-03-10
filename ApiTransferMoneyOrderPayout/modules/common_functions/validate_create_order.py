from typing import List, Dict, Any
from interfaces.header_interface import HeaderInterface

def validate_create_order(headers: HeaderInterface, body: Dict[str, Any]) -> List[str]:
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
        'benefiary_account_no',
        'benefiary_bank_code',
        'comment',
    ]

    for field in required_fields:
        if field not in body:
            errors.append(f'{field} is required.')

    return errors