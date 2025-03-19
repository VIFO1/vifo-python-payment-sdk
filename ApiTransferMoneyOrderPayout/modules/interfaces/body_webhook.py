from dataclasses import dataclass
from typing import Optional
from enum import Enum

class WebhookActionName(Enum):
    NEW_PAYMENT = "NEW_PAYMENT"
    SUCCESS_TRANSFER = "SUCCESS_TRANSFER"
    FAILED_TRANSFER = "FAILED_TRANSFER"
    TECHNICAL_ERROR_TRANSFER = "TECHNICAL_ERROR_TRANSFER"
    
@dataclass
class WebhookData:
    id: str
    order_number: str
    distributor_order_number: str
    amount: int
    transaction_id: Optional[str] = None
    payment_account: Optional[str] = None
    note: Optional[str] = None
    paid_at: Optional[str] = None

    def to_dict(self):
        return {
            "id": self.id,
            "order_number": self.order_number,
            "distributor_order_number": self.distributor_order_number,
            "amount": self.amount,
            "transaction_id": self.transaction_id,
            "payment_account": self.payment_account,
            "note": self.note,
            "paid_at": self.paid_at
        }

@dataclass
class WebhookBody:
    action_name: str
    data: WebhookData  
    message: Optional[str] = None

    def to_dict(self):
        return {
            "action_name": self.action_name,
            "data": self.data.to_dict(),
            "message": self.message
        }
