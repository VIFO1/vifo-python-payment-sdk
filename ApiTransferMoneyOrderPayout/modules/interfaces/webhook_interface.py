from abc import ABC, abstractmethod
from typing import Union, List
from .body_webhook import BodyWebhook

class WebhookInterface(ABC):
    @abstractmethod
    def create_signature(self, secret_key: str, timestamp: str, body: BodyWebhook) -> Union[str, List[str]]:
        pass
    
    @abstractmethod
    async def handle_signature(self, data: BodyWebhook, request_signature: str, 
                              secret_key: str, timestamp: str) -> bool:
        pass