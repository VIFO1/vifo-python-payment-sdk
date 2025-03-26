from typing import List, Dict, Any

from modules.services.vifo_send_request import VifoSendRequest
from modules.interfaces.vifo_authenticate_interface import VifoAuthenticateInterface
from modules.interfaces.body_authenticate_interface import BodyAuthenticateInterface
from modules.interfaces.header_login_interface import HeaderLoginInterface

class VifoAuthenticate(VifoAuthenticateInterface):
    def __init__(self, send_request: VifoSendRequest) -> None:
        self.send_request = send_request

    def validate_login_input(self, headers: HeaderLoginInterface, body: BodyAuthenticateInterface) -> List[str]:
        errors = []

        if headers is None or not isinstance(headers, dict):
            errors.append('headers must be a non-empty object')

        if body is None or not isinstance(body, dict):
            errors.append('body must be a non-empty object')
        return errors

    async def authenticate_user(self, headers: HeaderLoginInterface, body: BodyAuthenticateInterface) -> Dict[str, Any]:
        errors_login_input = self.validate_login_input(headers, body)

        if errors_login_input:
            return {"errorsLoginInput": errors_login_input}
        
        endpoint = '/v1/clients/web/admin/login'
        return await self.send_request.send_request('POST', endpoint, headers, body)

