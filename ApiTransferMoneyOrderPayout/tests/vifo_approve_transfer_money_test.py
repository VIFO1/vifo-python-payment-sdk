import asyncio
from inspect import signature
import os
import time
import token
from dotenv import load_dotenv
load_dotenv()
from modules.services.vifo_approve_transfer_money import VifoApproveTransferMoney
from modules.interfaces.header_interface import HeaderInterface
from modules.interfaces.body_approve_transfer_money import BodyApproveTransferMoney
from modules.services.vifo_send_request import VifoSendRequest
from modules.common_functions.generate_signature import generate_signature

async def test_approve_transfer_money():
    send_request = VifoSendRequest()
    approve_transfer_money = VifoApproveTransferMoney(send_request)
    
    timestamp = '2025-11-17 10:00:00'
    id = os.getenv('IDS')
    body = BodyApproveTransferMoney(
        status=6,
        ids=[id]  
    )
    token = os.getenv('ACCESS_TOKEN')
    secret_key = os.getenv('SECRET_KEY')
    signature = generate_signature(secret_key, timestamp, body.to_dict())
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
        'x-request-signature':signature,
        'x-request-timestamp': timestamp
    }

    result = await approve_transfer_money.approve_transfers(secret_key, timestamp, headers, body.to_dict())
    print(result)

if __name__ == "__main__":
    asyncio.run(test_approve_transfer_money())