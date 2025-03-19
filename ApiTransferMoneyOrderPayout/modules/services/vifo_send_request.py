import requests 
from typing import Dict, Optional, Any, List, Union
from modules.interfaces.vifo_send_request_interface import VifoSendRequestInterface
from modules.interfaces.response_data_interface import ResponseDataInterface

class VifoSendRequest(VifoSendRequestInterface):
    def __init__(self, env: str = 'dev') -> None:
        if env == 'dev':
            self.base_url = 'https://sapi.vifo.vn'
        elif env == 'stg':
            self.base_url = 'https://sapi.vifo.vn'
        elif env == 'production':
            self.base_url = 'https://api.vifo.vn'
        else:
            raise ValueError(f"Invalid environment: {env}")

    async def send_request(self, method: str, endpoint: str, headers: Dict[str, Any], body: Dict[str, Any]) -> ResponseDataInterface:
        url = endpoint if endpoint.startswith("http") else f"{self.base_url}{endpoint}"

        try:
            if method.upper() == 'GET':
                response = requests.request(method, url, headers=headers)
            else:
                response = requests.request(method, url, headers=headers, json=body)
            response.raise_for_status()
            return {
                "errors": None,
                "status_code": response.status_code,
                "body": response.json()
            }
        except requests.exceptions.RequestException as e:
            error_messages: List[str] = [f"Request Exception: {e}"]
            status_code = 500
            response_body = None
            if isinstance(e, requests.exceptions.HTTPError) and e.response is not None:
                status_code = e.response.status_code
                try:
                    response_body = e.response.json()
                except Exception:
                    response_body = e.response.text
            elif isinstance(e, requests.exceptions.ConnectionError):
                error_messages.append("Connection Error")
            elif isinstance(e, requests.exceptions.Timeout):
                error_messages.append("Request Timeout")

            return {
                "status_code": status_code,
                "body": response_body,
                "errors": error_messages
            }
        except Exception as e: 
            return {
                "status_code": 500,
                "body": None,
                "errors": [f"An unexpected error occurred: {e}"]
            }
