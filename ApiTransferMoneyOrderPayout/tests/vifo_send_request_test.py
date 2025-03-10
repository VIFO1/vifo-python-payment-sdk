import asyncio
from modules.services.vifo_send_request import VifoSendRequest

async def test_send_request():
    send_request = VifoSendRequest()
    
    result = await send_request.send_request('POST', 'youtube.com', {}, {})
    print(result)


if __name__ == "__main__":
    asyncio.run(test_send_request())