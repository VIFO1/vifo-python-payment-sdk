import asyncio
import os
from dotenv import load_dotenv
load_dotenv()
from modules.services.vifo_other_request import VifoOtherRequest
from modules.interfaces.header_interface import HeaderInterface
from modules.services.vifo_send_request import VifoSendRequest

async def test_other_request():
    send_request = VifoSendRequest()
    other_request = VifoOtherRequest(send_request)
    token = os.getenv('ACCESS_TOKEN')
    
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'     
    }
    key = os.getenv('KEY')
    print(key)  
    result = await other_request.check_order_status(headers, key)
    print(result)

if __name__ == "__main__":
    asyncio.run(test_other_request())