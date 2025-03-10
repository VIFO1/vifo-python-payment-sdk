import asyncio
from modules.services.vifo_send_request import VifoSendRequest
from modules.services.vifo_create_seva_order import VifoCreateSevaOrder
from modules.interfaces.header_interface import HeaderInterface
from modules.interfaces.body_create_seva_order import BodyCreateSevaOrder
from modules.interfaces.body_create_seva_order import QRTypeSeva  # Nếu QRTypeSeva có thể dùng hoặc không



async def test_create_seva_order():
    send_request = VifoSendRequest("dev")
    create_seva_order_test = VifoCreateSevaOrder(send_request)
    
    headers = HeaderInterface(
        Accept="application/json",
        Content_Type="application/json",
        Authorization="Bearer sample_token",
        x_request_timestamp="2025-03-06T12:00:00Z",
        x_request_signature="sample_signature"  
    )

    body = BodyCreateSevaOrder(
        product_code="PROD12332342",
        phone="0987654321",
        fullname="Le Van Teo ",
        final_amount=500000.0,
        distributor_order_number="ORDER12as345",
        benefiary_account_no= "77338",
        benefiary_bank_code="VCB5959",
        comment="tranfermoney",
        source_account_no="89128398",
        qr_type=QRTypeSeva.QR_RAW
    )
    test = await create_seva_order_test.create_seva_order(headers, body.to_dict())
    print(test)


if __name__ == "__main__":
    asyncio.run(test_create_seva_order())
