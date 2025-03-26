import asyncio
import os
from dotenv import load_dotenv
load_dotenv()
from modules.services.vifo_send_request import VifoSendRequest
from modules.services.vifo_create_reva_order import VifoCreateRevaOrder
from modules.interfaces.header_interface import HeaderInterface
from modules.interfaces.body_create_reva_order import BodyCreateRevaOrder
from modules.interfaces.body_create_reva_order import QRTypeReva
from modules.common_functions.generate_signature import generate_signature 
from modules.services.vifo_webhook import VifoWebhookService
from modules.interfaces.body_webhook import WebhookActionName
load_dotenv(override=True)

send_request = VifoSendRequest("dev")
create_reva_order_test = VifoCreateRevaOrder(send_request)

async def get_token(username: str, password: str):
    
    login_response = await send_request.send_request(
        "POST", "/v1/clients/web/admin/login",
        headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
        body={"username": username, "password": password}
    )
    access_token = login_response.get('body', {}).get('access_token')
    return access_token

async def test_create_reva_order():
    user_token = await get_token(os.getenv("USERNAME"), os.getenv("PASSWORD"))
    headers_user = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {user_token}'
    }
    body = BodyCreateRevaOrder(
        fullname="Le Van Teo ",
        product_code="REVAVF240101",
        distributor_order_number="ORDER12ads345",
        phone="0987654321",
        email="test@example.com",
        address="141 Bac Hai",
        final_amount=500000,
        comment="Test order",
        benefiary_account_name="SPR VA TEST",
        bank_detail=True,
        qr_type=None,
        end_date=None
    )
    create_order_response = await create_reva_order_test.create_reva_order(headers_user, body.to_dict())
    print("Create REVA Order Response:", create_order_response)
    
    if create_order_response.get("body", {}).get("status") == "success":
        order_id = create_order_response["body"]["data"]["id"]
        order_number = create_order_response["body"]["data"]["order_number"]
        amount = create_order_response["body"]["data"]["amount"]
        distributor_order_number = create_order_response["body"]["data"]["distributor_order_number"]
        action = WebhookActionName.NEW_PAYMENT

        body_webhook = {
            "action_name": action.value,
            "message": "Test webhook",
            "data": {
            "id": order_id,
            "order_number": order_number,
            "distributor_order_number": distributor_order_number,
            "amount": amount,
            "transaction_id": "FT240014955",
            "payment_account": "VFC02001025148",
            "note": "Payment webhook test",
            "paid_at": None
            }
        }
        secret_key = os.getenv('SECRET_KEY')
        timestamp = '2025-11-17 10:00:00'
        signature = generate_signature(secret_key, timestamp, body_webhook)
        header = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x-request-signature':signature,
            'x-request-timestamp': timestamp
        }
        webhook_service = VifoWebhookService(send_request)
        webhook_response = await webhook_service.send_webhook(secret_key, timestamp, header, body_webhook)
        print(f"REVA {action.value}:", webhook_response)

        if os.getenv("AUTO_TERMINATE") == "true":
            headers_user = {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {user_token}'
            }
            terminate_response = await create_reva_order_test.terminate_va(headers_user, order_id)
            print("Terminate REVA Order Response:", terminate_response)
            
if __name__ == "__main__":
    asyncio.run(test_create_reva_order())