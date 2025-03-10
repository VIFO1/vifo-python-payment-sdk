import hashlib
import hmac
import json
from typing import Union, List, Dict, Any

def generate_signature(secret_key: str, timestamp: str, body: Dict[str, Any]) -> Union[str, List[str]]:
    errors = []

    if not secret_key or not isinstance(secret_key, str):
        errors.append('Invalid secret key')

    if not timestamp:
        errors.append('Invalid timestamp')

    if not isinstance(body, dict) or not body:
        errors.append('The body must be a non-empty object')

    if errors:
        return [f"Error: {error}" for error in errors]

    # sort boby by key
    sorted_body = dict(sorted(body.items()))
    payload = json.dumps(sorted_body, separators=(',', ':')) # Eliminate gaps
    signature_string = timestamp + payload

    signature = hmac.new(
        secret_key.encode('utf-8'),
        signature_string.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

    return signature