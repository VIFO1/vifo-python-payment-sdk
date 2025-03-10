import asyncio

from modules.services.vifo_bank import VifoBank
from modules.interfaces.header_interface import HeaderInterface
from modules.interfaces.body_beneficiary_name import BodyBeneficiaryName
from modules.services.vifo_send_request import VifoSendRequest

async def test_bank():
    send_request = VifoSendRequest()
    bank = VifoBank(send_request)
    headers = HeaderInterface(
        Accept="application/json",
        Content_Type="application/json",
        Authorization="Bearer sample_token",
        x_request_timestamp="2025-03-06T12:00:00Z",
        x_request_signature="sample_signature"
    )
    result = await bank.get_bank(headers, {})
    print(result)

async def test_beneficiary_name():
    send_request = VifoSendRequest()
    bank = VifoBank(send_request=send_request)
    headers = HeaderInterface(
        Accept="application/json",
        Content_Type="application/json",
        Authorization="Bearer sample_token",
        x_request_timestamp="2025-03-06T12:00:00Z",
        x_request_signature="sample_signature"
    )
    body = BodyBeneficiaryName(
        bank_code='',
        account_number=''
    )
    result_beneficiary_name = await bank.get_beneficiary_name(headers, body.to_dict())
    print(result_beneficiary_name)

async def main():
    await test_bank()
    await test_beneficiary_name()

if __name__ == "__main__":
    asyncio.run(main())