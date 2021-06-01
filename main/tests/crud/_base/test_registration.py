from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud._base.registration import (
	registration_base_crud,
)

from main.schemas._base.registration import (
	RegistrationBaseSchemaCreate,
	RegistrationBaseSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest



@pytest.mark.asyncio
async def test_create_registration_base(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_get_registration_base(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_registration_base(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_registration_base(
	db: AsyncSession,
) -> None:
	pass





