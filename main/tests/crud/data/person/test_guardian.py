from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.person.guardian import (
	guardian_crud,
)

from main.schemas.data.person.guardian import (
	GuardianSchemaCreate,
	GuardianSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest




@pytest.mark.asyncio
async def test_create_guardian(
	db: AsyncSession,
) -> None:
	# --
	full_name = random_name()
	mobile_phone = random_lower_string()
	home_phone = random_lower_string()
	work_phone = random_lower_string()
	email = random_email()

	guardian_in = GuardianSchemaCreate(
		full_name=full_name,
		mobile_phone=mobile_phone,
		home_phone=home_phone,
		work_phone=work_phone,
		email=email,
	)

	guardian = await guardian_crud.create(
		db=db,
		obj_in=guardian_in,
	)

	assert guardian
	assert guardian.full_name == full_name
	assert guardian.email == email



@pytest.mark.asyncio
async def test_create_sync_guardian(
	db: AsyncSession,
) -> None:
	# --
	full_name = random_name()
	mobile_phone = random_lower_string()
	home_phone = random_lower_string()
	work_phone = random_lower_string()
	email = random_email()

	guardian_in = GuardianSchemaCreate(
		full_name=full_name,
		mobile_phone=mobile_phone,
		home_phone=home_phone,
		work_phone=work_phone,
		email=email,
	)

	guardian = await db.run_sync(
		guardian_crud.create_sync,
		obj_in=guardian_in,
	)

	assert guardian
	assert guardian.full_name == full_name
	assert guardian.email == email



@pytest.mark.asyncio
async def test_get_guardian(
	db: AsyncSession,
) -> None:
	# --
	pass



@pytest.mark.asyncio
async def test_get_sync_guardian(
	db: AsyncSession,
) -> None:
	# --
	pass



@pytest.mark.asyncio
async def test_update_guardian(
	db: AsyncSession,
) -> None:
	# --
	pass



@pytest.mark.asyncio
async def test_update_sync_guardian(
	db: AsyncSession,
) -> None:
	# --
	pass



@pytest.mark.asyncio
async def test_delete_guardian(
	db: AsyncSession,
) -> None:
	# --
	pass



@pytest.mark.asyncio
async def test_delete_sync_guardian(
	db: AsyncSession,
) -> None:
	# --
	pass





