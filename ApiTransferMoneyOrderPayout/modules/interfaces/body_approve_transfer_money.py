from dataclasses import dataclass
from typing import List

@dataclass
class BodyApproveTransferMoney:
    status: int
    ids: List[str]

    def to_dict(self) -> dict:
        return {
            "status": self.status,
            "ids": self.ids
        }

    