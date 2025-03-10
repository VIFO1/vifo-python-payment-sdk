from typing import TypedDict, Union, List, Optional

class HeaderInterface(TypedDict):
    Accept: str
    Content_Type: str
    Authorization: Optional[str]
    x_request_timestamp: Optional[str]
    x_request_signature: Union[str, None, List[str]]