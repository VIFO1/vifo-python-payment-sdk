import asyncio

from modules.services.vifo_service_factory import VifoServiceFactory 
from modules.interfaces.body_beneficiary_name import BodyBeneficiaryName

async def test_service_factory():
    service_factory = VifoServiceFactory('dev')

    body = BodyBeneficiaryName(
        bank_code = 'string',
        account_number = 'string'
    )

    bank = await service_factory.fetch_bank_information({})
    get_bank_name = await service_factory.fetch_beneficiary_name(body.to_dict())

    print(bank)
    print(get_bank_name)

if __name__ == "__main__":
    asyncio.run(test_service_factory())
