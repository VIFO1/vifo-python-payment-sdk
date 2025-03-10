import hashlib
from typing import Union, List, Dict, Any
from modules.services.vifo_send_request import VifoSendRequest
from modules.interfaces.webhook_interface import WebhookInterface
from modules.interfaces.body_webhook import BodyWebhook
from modules.common_functions.generate_signature import generate_signature
from modules.common_functions.validate_signature_inputs import validate_signature_inputs

class Webhook(WebhookInterface):
    def __init__(self, send_request: VifoSendRequest) -> None:
        self.send_request = send_request 

    def create_signature(self, secret_key: str, timestamp: str, body: BodyWebhook) -> Union[str, List[str]]:
        errors = validate_signature_inputs(secret_key, timestamp, body)
        if errors:
            return [f"Error: {error}" for error in errors]

        return generate_signature(secret_key, timestamp, body)

    async def handle_signature(self, data: BodyWebhook, request_signature: str, secret_key: str, timestamp: str) -> bool:
        errors = validate_signature_inputs(secret_key, timestamp, data)

        if errors:
            raise ValueError('Validation errors: ' + str(errors))

        generated_signature = self.create_signature(secret_key, timestamp, data)

        if generated_signature == request_signature:
            return True
        else:
            return False