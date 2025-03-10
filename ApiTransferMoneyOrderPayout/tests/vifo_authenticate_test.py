import asyncio

from modules.services.vifo_send_request import VifoSendRequest
from modules.services.vifo_authenticate import VifoAuthenticate
from modules.interfaces.header_login_interface import HeaderLoginInterface
from modules.interfaces.body_authenticate_interface import BodyAuthenticateInterface


async def test_login():
    send_request = VifoSendRequest()
    login_result = VifoAuthenticate(send_request)
    
    headers = HeaderLoginInterface(
        Accept='application/json',       
        Accept_Encoding='gzip, deflate',  
        Accept_Language='en-US'
    )
    body = BodyAuthenticateInterface(
        username='user123',
        password='123456'
    )
    result = await login_result.authenticate_user(headers, body.to_dict())

    print(result)

if __name__ == "__main__":
    asyncio.run(test_login())