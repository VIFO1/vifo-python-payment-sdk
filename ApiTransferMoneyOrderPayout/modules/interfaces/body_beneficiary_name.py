from dataclasses import dataclass

@dataclass
class BodyBeneficiaryName:
    bank_code: str
    account_number: str

    def to_dict(self) -> dict:
        return {
            "bank_code": self.bank_code,
            "account_number": self.account_number
        }
