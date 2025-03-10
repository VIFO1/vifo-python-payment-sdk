from typing import List, Dict, Any

def validate_signature_inputs(secret_key: str, timestamp: str, body: Dict[str, Any]) -> List[str]:
    errors = []

    if not secret_key or not isinstance(secret_key, str):
        errors.append('Invalid secret key')

    if not timestamp:
        errors.append('Invalid timestamp')

    if not isinstance(body, dict) or not body:
        errors.append('The body must be a non-empty object')

    return errors