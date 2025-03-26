import asyncio
import os
from dotenv import load_dotenv
load_dotenv()
from modules.services.vifo_bank import VifoBank
from modules.interfaces.header_interface import HeaderInterface
from modules.interfaces.body_beneficiary_name import BodyBeneficiaryName
from modules.services.vifo_send_request import VifoSendRequest

token = os.getenv('ACCESS_TOKEN')
    
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'     
    }
    
async def test_bank():
    send_request = VifoSendRequest()
    bank = VifoBank(send_request)
    
    result = await bank.get_bank(headers, {})
    print(result)

async def test_beneficiary_name():
    send_request = VifoSendRequest()
    bank = VifoBank(send_request=send_request)
    
    body = BodyBeneficiaryName(
        bank_code='970406',
        account_number='0129837294'
    )
    result_beneficiary_name = await bank.get_beneficiary_name(headers, body.to_dict())
    print(result_beneficiary_name)

async def main():
    await test_bank()
    await test_beneficiary_name()

if __name__ == "__main__":
    asyncio.run(main())