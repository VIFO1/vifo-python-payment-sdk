import asyncio

from modules.services.vifo_approve_transfer_money import VifoApproveTransferMoney
from modules.interfaces.header_interface import HeaderInterface
from modules.interfaces.body_approve_transfer_money import BodyApproveTransferMoney
from modules.services.vifo_send_request import VifoSendRequest

async def test_approve_transfer_money():
    send_request = VifoSendRequest()
    approve_transfer_money = VifoApproveTransferMoney(send_request)

    secret_key = 'VIFO123'
    timestamp = '2022-01-01T00:00:00Z'
    body = BodyApproveTransferMoney(
        status=1,
        ids=['txn12345', 'txn67890']  
    )
    headers = HeaderInterface(
        Accept='application/json',       
        Accept_Encoding='gzip, deflate',  
        Accept_Language='en-US',
        x_request_timestamp='',
        x_request_signature=''
    )

    result = await approve_transfer_money.approve_transfers(secret_key, timestamp, headers, body.to_dict())
    print(result)


if __name__ == "__main__":
    asyncio.run(test_approve_transfer_money())