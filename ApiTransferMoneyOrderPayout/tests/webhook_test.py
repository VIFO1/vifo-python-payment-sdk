import asyncio

from modules.services.webhook import Webhook
from modules.services.vifo_send_request import VifoSendRequest

async def test_webhook():
    send_request = VifoSendRequest()
    webhook = Webhook(send_request)
    
    result = await webhook.handle_signature({'status': 1,'ids':['123']},"VIFO123","pass123","2022-11-11")
    print(result)

if __name__ == "__main__":
    asyncio.run(test_webhook())