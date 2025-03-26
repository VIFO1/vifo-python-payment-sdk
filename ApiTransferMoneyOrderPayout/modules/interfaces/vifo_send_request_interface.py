from abc import ABC, abstractmethod
from typing import Dict, Any
from .response_data_interface import ResponseDataInterface

class VifoSendRequestInterface(ABC):
    @abstractmethod
    async def send_request(self, method: str, endpoint: str, headers: Dict[str, Any], 
                           body: Dict[str, Any]) -> ResponseDataInterface:
        pass