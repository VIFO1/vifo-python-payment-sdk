# Python Finance Integration SDK
Python SDK finance of VIFO

## Purpose
This Python file uses services from VifoServiceFactory to perform banking, money transfer and other requests. The following guide provides detailed information on how to use and understand the functions of the code.

## Requirements

- **Python**: Version 3.7 or higher.
- **pip**: Version 25.0.1 or higher.

# Import SDK
from modules.vifo_service_factory import VifoServiceFactory

## Code Structure

```python
1. Initialize SDK
vifo_service: VifoServiceFactory = VifoServiceFactory(env: str)

2. User Authentication
authenticate_user: dict = await vifo_service.perform_user_authentication(body: BodyAuthenticateInterface)

2.1 Methods for Token Setup
vifo_service.set_token_user(token: str) -> None  # This method is used to set the authentication token for user-based requests.
vifo_service.set_token_admin(token: str) -> None  # This method is used to set the authentication token for admin-based requests.

# Using Tokens in Requests
# Once the tokens are set using the above methods, they will be automatically included in the headers for their respective requests.

3. Prepare Data
3.1 Get List of Available Banks:
banks: dict = await vifo_service.fetch_bank_information(body: dict)

3.2 Get NAPAS Beneficiary Name:
beneficiary_name: dict = await vifo_service.fetch_beneficiary_name(body: BodyBeneficiaryName)

4. Create Transfer Money API:
transfer_money: dict = await vifo_service.execute_money_transfer(body: BodyTransferMoneyInterface)

5. Bulk Approve Transfer Money API:
approve_money_transfer: dict = await vifo_service.approve_money_transfer(secret_key: str, timestamp: str, body: BodyApproveTransferMoney)

6. Webhook to inform the result of transfer / pay out request:
webhook: bool = await vifo_service.verify_webhook_signature(data: BodyWebhookInterface, request_signature: str, secret_key: str, timestamp: str)

7. Others Request:
other_request: dict = await vifo_service.process_other_request(key: str)

8. Create Reva Order:
create_reva_order: dict = await vifo_service.create_reva_order(
    fullname: str,
    benefiary_account_name: str,
    product_code: Optional[str],
    distributor_order_number: str,
    phone: str,
    email: str,
    address: str,
    final_amount: float,
    comment: str,
    bank_detail: bool,
    qr_type: Optional[QRTypeReva],
    end_date: Optional[str]
)

9. Create Seva Order:
create_seva_order: dict = await vifo_service.create_seva_order(
    product_code: Optional[str],
    phone: str,
    fullname: str,
    final_amount: float,
    distributor_order_number: str,
    benefiary_bank_code: str,
    benefiary_account_no: str,
    comment: str,
    source_account_no: str
)
