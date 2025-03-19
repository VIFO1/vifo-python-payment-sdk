import os
import asyncio
from dotenv import load_dotenv
from modules.services.vifo_service_factory import VifoServiceFactory
from modules.interfaces.body_authenticate_interface import BodyAuthenticateInterface
from modules.interfaces.body_approve_transfer_money import BodyApproveTransferMoney
from modules.interfaces.body_webhook import WebhookBody, WebhookData
from modules.interfaces.body_create_seva_order import BodyCreateSevaOrder
from modules.interfaces.body_create_reva_order import BodyCreateRevaOrder
from modules.interfaces.header_login_interface import HeaderLoginInterface

load_dotenv()

service_factory = VifoServiceFactory(env="dev")

async def test_authenticate_user():
    body = BodyAuthenticateInterface(
        username=os.getenv("USERNAME"),
        password=os.getenv("PASSWORD")
    )
    
    headers = HeaderLoginInterface(
        Accept="application/json",
        Accept_Encoding="gzip, deflate",
        Accept_Language="en-US"
    )

    result = await service_factory.authenticate_user(body, headers)
    print("Test Authenticate User:", result)

async def test_approve_money_transfer():
    secret_key = os.getenv("SECRET_KEY")
    timestamp = "2025-03-06T12:00:00Z"
    id = os.getenv('IDS')

    body = BodyApproveTransferMoney(
        status=6,
        ids=[id]
    )

    result = await service_factory.approve_money_transfer(secret_key, timestamp, body)
    print("Test Approve Money Transfer:", result)

async def test_send_webhook():
    secret_key = os.getenv("SECRET_KEY")
    timestamp = "2025-03-06T12:00:00Z"

    body = WebhookBody(
        action_name="SUCCESS_TRANSFER",
        message="Webhook test",
        data=WebhookData(
            id="vmg6q369ndr3b8kz",
            order_number="VF240102001025148",
            distributor_order_number="XXX123",
            amount=18000,
            transaction_id="FT240014955"
        )
    )

    result = await service_factory.send_webhook(secret_key, timestamp, body)
    print(f"Test Send Webhook:", result)

async def test_create_seva_order():
    body = BodyCreateSevaOrder(
        product_code="SEVA001",
        phone="0123456789",
        fullname="Test User",
        final_amount=50000,
        distributor_order_number="ORDER123",
        benefiary_bank_code="VCB",
        benefiary_account_no="123456789",
        comment="Payment for services",
        source_account_no="987654321"
    )

    result = await service_factory.create_seva_order(body)
    print("Test Create SEVA Order:", result)

async def test_create_reva_order():
    body = BodyCreateRevaOrder(
        fullname="Test User",
        benefiary_account_name="Test Bank",
        product_code="REVA001",
        distributor_order_number="ORDER456",
        phone="0123456789",
        email="test@example.com",
        address="123 Test Street",
        final_amount=75000,
        comment="Payment for REVA service",
        bank_detail=True,
        qr_type=None,
        end_date="2025-12-31"
    )

    result = await service_factory.create_reva_order(body)
    print("Test Create REVA Order:", result)

async def main_test():
    await test_authenticate_user()
    await test_approve_money_transfer()
    await test_send_webhook()
    await test_create_seva_order()
    await test_create_reva_order()

if __name__ == "__main__":
    asyncio.run(main_test())
