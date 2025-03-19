from dataclasses import dataclass
from typing import Optional

@dataclass
class BodyCreateSevaOrder:
    product_code: str
    phone: str
    fullname: str
    final_amount: float
    distributor_order_number: str
    benefiary_bank_code: str
    benefiary_account_no: str
    comment: str
    source_account_no: Optional[str] 

    def to_dict(self) -> dict:
        return {
            "product_code": self.product_code,
            "phone": self.phone,
            "fullname": self.fullname,
            "final_amount": self.final_amount,
            "distributor_order_number": self.distributor_order_number,
            "benefiary_bank_code": self.benefiary_bank_code,
            "benefiary_account_no": self.benefiary_account_no,
            "comment": self.comment,
            "source_account_no": self.source_account_no,
        }


