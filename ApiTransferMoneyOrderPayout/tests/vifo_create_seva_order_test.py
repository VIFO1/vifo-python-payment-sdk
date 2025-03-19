import asyncio
import os
from dotenv import load_dotenv
from modules.services.vifo_send_request import VifoSendRequest
from modules.services.vifo_create_seva_order import VifoCreateSevaOrder
from modules.interfaces.body_create_seva_order import BodyCreateSevaOrder
from modules.services.vifo_approve_transfer_money import VifoApproveTransferMoney
from modules.common_functions.generate_signature import generate_signature
load_dotenv(override=True)

send_request = VifoSendRequest("dev")
create_seva_order_test = VifoCreateSevaOrder(send_request)

async def get_token(username: str, password: str):
    login_response = await send_request.send_request(
        "POST", "/v1/clients/web/admin/login",
        headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
        body={"username": username, "password": password}
    )
    access_token = login_response.get('body', {}).get('access_token')
    return access_token

async def test_create_seva_order():
    user_token = await get_token(os.getenv("USERNAME"), os.getenv("PASSWORD"))
    admin_token = await get_token(os.getenv("ADMIN_USERNAME"), os.getenv("ADMIN_PASSWORD"))

    headers_user = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {user_token}'
    }
    body = BodyCreateSevaOrder(
        product_code="SEVAVF240101",
        phone="0987654321",
        fullname="Le Van Teo ",
        final_amount=500000,
        distributor_order_number="S3U3ePeededERe1e23",
        benefiary_account_no="0129837294",
        benefiary_bank_code="970406",
        comment="transfermoney",
        source_account_no="",
    )
    create_order_response = await create_seva_order_test.create_seva_order(headers_user, body.to_dict())
    print("Create SEVA Order Response:", create_order_response)
    
    if create_order_response.get("body",{}).get("status") == "success":
        order_id = create_order_response["body"]["data"]["id"]
        body_approve = {
        "status": 6,  
        "ids": [order_id]  
        }
        secret_key = os.getenv('SECRET_KEY')
        timestamp = '2025-11-17 10:00:00'
        signature = generate_signature(secret_key, timestamp, body_approve)
        headers_admin = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {admin_token}',
            'x-request-signature':signature,
            'x-request-timestamp': timestamp
        }
        
        approve_transfer_money = VifoApproveTransferMoney(send_request)
        approve_response = await approve_transfer_money.approve_transfers(secret_key, timestamp, headers_admin, body_approve)
        print("Approve SEVA Order Response:", approve_response)
    else:
        print("Approve SEVA Order failed")

if __name__ == "__main__":
    asyncio.run(test_create_seva_order())
