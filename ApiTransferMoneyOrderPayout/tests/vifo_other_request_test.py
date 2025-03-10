import asyncio

from modules.services.vifo_other_request import VifoOtherRequest
from modules.interfaces.header_interface import HeaderInterface
from modules.services.vifo_send_request import VifoSendRequest

async def test_other_request():
    send_request = VifoSendRequest()
    other_request = VifoOtherRequest(send_request)
    headers = HeaderInterface(
        Accept='',
        Content_Type='',
        Authorization='',
        x_request_timestamp='',
        x_request_signature=''
    )
    result = await other_request.validate_order_key(headers, 'test123')
    print(result)

if __name__ == "__main__":
    asyncio.run(test_other_request())