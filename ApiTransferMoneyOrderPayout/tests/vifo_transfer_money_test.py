import asyncio

from modules.services.vifo_transfer_money import VifoTransferMoney
from modules.services.vifo_send_request import VifoSendRequest
from modules.services.vifo_transfer_money import VifoTransferMoney
from modules.interfaces.header_interface import HeaderInterface
from modules.interfaces.body_transfer_money import BodyTransferMoney

async def test_tranfer_money():
    send_request = VifoSendRequest()
    tranfer_money = VifoTransferMoney(send_request)

    headers = HeaderInterface(
        Accept='application/json',       
        Accept_Encoding='gzip, deflate',  
        Accept_Language='en-US',
        x_request_timestamp='',
        x_request_signature=''
    )

    body = BodyTransferMoney(
        product_code="",
        phone="",
        fullname="",
        final_amount=0,
        distributor_order_number="",
        benefiary_bank_code="",
        benefiary_account_no="",
        comment="",
        source_account_no=""
    )

    result = await tranfer_money.create_transfer_money(headers, body.to_dict())
    print(result)

if __name__ == "__main__":
    asyncio.run(test_tranfer_money())