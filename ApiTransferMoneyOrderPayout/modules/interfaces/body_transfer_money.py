from dataclasses import dataclass

@dataclass
class BodyTransferMoney:
    product_code: str
    phone: str
    fullname: str
    final_amount: float
    distributor_order_number: str
    benefiary_bank_code: str
    benefiary_account_no: str
    comment: str
    source_account_no: str

    def to_dict(self):
        return {
            "productCode": self.product_code,
            "phone": self.phone,
            "fullname": self.fullname,
            "finalAmount": self.final_amount,
            "distributorOrderNumber": self.distributor_order_number,
            "benefiaryBankCode": self.benefiary_bank_code,
            "benefiaryAccountNo": self.benefiary_account_no,
            "comment": self.comment,
            "sourceAccountNo": self.source_account_no
        }