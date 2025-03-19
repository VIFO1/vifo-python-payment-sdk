import asyncio
import os
from dotenv import load_dotenv
load_dotenv()
from modules.services.vifo_send_request import VifoSendRequest
from modules.services.vifo_create_reva_order import VifoCreateRevaOrder
from modules.interfaces.header_interface import HeaderInterface
from modules.interfaces.body_create_reva_order import BodyCreateRevaOrder
from modules.interfaces.body_create_reva_order import QRTypeReva  

async def test_create_reva_order():
    send_request = VifoSendRequest("dev")
    create_reva_order_test = VifoCreateRevaOrder(send_request)

    token = os.getenv('ACCESS_TOKEN')
    
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'     
    }
    body = BodyCreateRevaOrder(
        fullname="Le Van Teo ",
        product_code="REVAVF240101",
        distributor_order_number="ORDER12as345",
        phone="0987654321",
        email="test@example.com",
        address="141 Bac Hai",
        final_amount=500000.0,
        comment="Test order",
        benefiary_account_name="SPR VA TEST",
        bank_detail=True,
        qr_type=None,
        end_date=None
    )

    test = await create_reva_order_test.create_reva_order(headers, body.to_dict())
    print(test)

if __name__ == "__main__":
    asyncio.run(test_create_reva_order())
