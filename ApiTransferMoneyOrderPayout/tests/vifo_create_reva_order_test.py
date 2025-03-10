import asyncio

from modules.services.vifo_send_request import VifoSendRequest
from modules.services.vifo_create_reva_order import VifoCreateRevaOrder
from modules.interfaces.header_interface import HeaderInterface
from modules.interfaces.body_create_reva_order import BodyCreateRevaOrder
from modules.interfaces.body_create_reva_order import QRTypeReva  

async def test_create_reva_order():
    send_request = VifoSendRequest("dev")
    create_reva_order_test = VifoCreateRevaOrder(send_request)

    headers = HeaderInterface(
        Accept="application/json",
        Content_Type="application/json",
        Authorization="Bearer sample_token",
        x_request_timestamp="2025-03-06T12:00:00Z",
        x_request_signature="sample_signature"
    )

    body = BodyCreateRevaOrder(
        fullname="Le Van Teo ",
        product_code="PROD12332342",
        distributor_order_number="ORDER12as345",
        phone="0987654321",
        email="test@example.com",
        address="141 Bac Hai",
        final_amount=500000.0,
        comment="Test order",
        benefiary_account_name="LeThanhPhat",
        bank_detail=True,
        qr_type=QRTypeReva.QR_RAW,
        end_date="2025-03-10"
    )

    response = await create_reva_order_test.create_reva_order(headers, body.to_dict())
    print(response)


if __name__ == "__main__":
    asyncio.run(test_create_reva_order())
