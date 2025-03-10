from dataclasses import dataclass
from typing import List

@dataclass
class BodyWebhook:
    status: int
    ids: List[str]