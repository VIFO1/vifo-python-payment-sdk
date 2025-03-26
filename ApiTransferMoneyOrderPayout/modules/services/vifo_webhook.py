from typing import Dict, Any, Union, List
from datetime import datetime
import json

from modules.services.vifo_send_request import VifoSendRequest
from modules.interfaces.body_webhook import WebhookData, WebhookBody
from modules.interfaces.header_interface import HeaderInterface
from modules.common_functions.validate_signature_inputs import validate_signature_inputs
from modules.common_functions.generate_signature import generate_signature

class VifoWebhookService:
    def __init__(self, send_request: VifoSendRequest) -> None:
        self.send_request = send_request

    def create_signature(self, secret_key: str, timestamp: str, body: WebhookBody) -> Union[str, List[str]]:
        """Tạo signature dựa trên secret_key, timestamp và body."""
        errors = validate_signature_inputs(secret_key, timestamp, body)
        return [f"Error: {error}" for error in errors] if errors else generate_signature(secret_key, timestamp, body)

    async def send_webhook(self, secret_key: str, timestamp: str, headers: HeaderInterface, body: WebhookBody) -> Dict[str, Any]:
        errors = validate_signature_inputs(secret_key, timestamp, body)
        if errors:
            return {"errors": [f"Error: {error}" for error in errors]}

        endpoint = "http://127.0.0.1:8000/api/v1/vifo/webhook"
        return await self.send_request.send_request('POST', endpoint, headers, body)
