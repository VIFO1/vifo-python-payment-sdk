import asyncio
import os
from dotenv import load_dotenv
load_dotenv()
from modules.services.vifo_send_request import VifoSendRequest
from modules.services.vifo_create_seva_order import VifoCreateSevaOrder
from modules.interfaces.header_interface import HeaderInterface
from modules.interfaces.body_create_seva_order import BodyCreateSevaOrder

async def test_create_seva_order():
    send_request = VifoSendRequest("dev")
    create_seva_order_test = VifoCreateSevaOrder(send_request)
    
    token = os.getenv('ACCESS_TOKEN')
    
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'     
    }

    body = BodyCreateSevaOrder(
        product_code="SEVAVF240101",
        phone="0987654321",
        fullname="Le Van Teo ",
        final_amount=500000,
        distributor_order_number="ORDER12as345",
        benefiary_account_no= "0129837294",
        benefiary_bank_code="970406",
        comment="tranfermoney",
        source_account_no="",
    )
    test = await create_seva_order_test.create_seva_order(headers, body.to_dict())
    print(test)


if __name__ == "__main__":
    asyncio.run(test_create_seva_order())
