from typing import TypedDict, List, Optional, Any

class ResponseDataInterface(TypedDict):
    status_code: int
    body: Optional[Any]
    errors: Optional[List[str]]