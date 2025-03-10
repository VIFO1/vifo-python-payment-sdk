from enum import Enum
from dataclasses import dataclass
from typing import Optional

class QRTypeReva(Enum):
    RAW = "RAW"
    QR_RAW = "QR_RAW"

@dataclass
class BodyCreateRevaOrder:
    fullname: str
    product_code: Optional[str]
    distributor_order_number: str
    phone: str
    email: Optional[str]
    address: Optional[str]
    final_amount: float
    comment: str
    benefiary_account_name: str
    bank_detail: Optional[bool]
    qr_type: Optional[QRTypeReva]
    end_date: Optional[str]

    def to_dict(self) -> dict:
        return {
            "fullname": self.fullname,
            "product_code": self.product_code,
            "distributor_order_number": self.distributor_order_number,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "final_amount": self.final_amount,
            "comment": self.comment,
            "benefiary_account_name": self.benefiary_account_name,
            "bank_detail": self.bank_detail,
            "qr_type": self.qr_type.value,
            "end_date": self.end_date,
    }


