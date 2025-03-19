import os
import asyncio
from dotenv import load_dotenv
from modules.services.vifo_webhook import VifoWebhookService
from modules.services.vifo_send_request import VifoSendRequest
from modules.interfaces.body_webhook import WebhookBody, WebhookData
from modules.interfaces.header_interface import HeaderInterface
from modules.common_functions.generate_signature import generate_signature

load_dotenv()

send_request = VifoSendRequest()
webhook_service = VifoWebhookService(send_request)
timestamp = "2025-03-06 12:00:00"
secret_key = os.getenv("SECRET_KEY")

def create_webhook_body(action_name: str, transaction_id=None, message=None, payment_account=None, note=None, paid_at=None):
    body_data = WebhookData(
        id="vmg6q369ndr3b8kz",
        order_number="VF240102001025148",
        distributor_order_number="XXX123",
        amount=18000,
        transaction_id=transaction_id,
        payment_account=payment_account,  
        note=note,
        paid_at=paid_at
    )
    return WebhookBody(
        action_name=action_name,
        message=message,
        data=body_data
    )

def create_headers(body: WebhookBody):
    signature = generate_signature(secret_key, timestamp, body.to_dict())
    return {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x-request-signature': signature,
        'x-request-timestamp': timestamp
    }

async def test_webhook_seva():
    for action, transaction_id, message in [
        ("SUCCESS_TRANSFER", "FT240014955", ""),
        # ("FAILED_TRANSFER", None, "reason fail"),
        # ("TECHNICAL_ERROR_TRANSFER", None, "<ERROR MESSAGE DEPENDING ON STATUS>")
         ]:
        body = create_webhook_body(action, transaction_id, message, 
                                payment_account="VFC02001025148",
                                note="Test webhook",
                                paid_at="2025-03-06 12:00:00")
        headers = create_headers(body) 
        response = await webhook_service.send_webhook(secret_key, timestamp, headers, body.to_dict())
        # print(body.to_dict())
        print(f"Test SEVA {action}:", response)

async def test_webhook_reva():
    body = create_webhook_body("NEW_PAYMENT", "FT240014955")
    headers = create_headers(body)  
    response = await webhook_service.send_webhook(secret_key, timestamp, headers, body.to_dict())
    # print(body.to_dict())
    print("Test REVA NEW_PAYMENT:", response)

async def main():
    await test_webhook_seva()
    await test_webhook_reva()

if __name__ == "__main__":
    asyncio.run(main())
