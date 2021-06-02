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

	guardian_2 = await guardian_crud.get(
		db=db,
		id=guardian.id,
	)


	assert guardian_2
	assert jsonable_encoder(guardian) == jsonable_encoder(guardian_2)



@pytest.mark.asyncio
async def test_get_sync_guardian(
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

	guardian_2 = await db.run_sync(
		guardian_crud.get_sync,
		id=guardian.id,
	)

	assert guardian_2
	assert jsonable_encoder(guardian) == jsonable_encoder(guardian_2)



@pytest.mark.asyncio
async def test_update_guardian(
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

	new_full_name = random_name()

	guardian_in_update = GuardianSchemaUpdate(
		full_name=new_full_name,
	)


	guardian_2 = await guardian_crud.update(
		db=db,
		db_obj=guardian,
		obj_in=guardian_in_update,
	)

	assert guardian_2
	assert guardian_2.full_name
	assert guardian_2.full_name == new_full_name




@pytest.mark.asyncio
async def test_update_sync_guardian(
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

	new_full_name = random_name()

	guardian_in_update = GuardianSchemaUpdate(
		full_name=new_full_name,
	)


	guardian_2 = await db.run_sync(
		guardian_crud.update_sync,
		db_obj=guardian,
		obj_in=guardian_in_update,
	)

	assert guardian_2
	assert guardian_2.full_name
	assert guardian_2.full_name == new_full_name



@pytest.mark.asyncio
async def test_delete_guardian(
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

	guardian_2 = await guardian_crud.delete(
		db=db,
		id=guardian.id,
	)

	guardian_3 = await guardian_crud.get(
		db=db,
		id=guardian.id,
	)


	assert guardian_3 is None
	assert guardian_2.id == guardian.id



@pytest.mark.asyncio
async def test_delete_sync_guardian(
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


	guardian_2 = await db.run_sync(
		guardian_crud.delete_sync,
		id=guardian.id,
	)


	guardian_3 = await db.run_sync(
		guardian_crud.get_sync,
		id=guardian.id,
	)


	assert guardian_3 is None
	assert guardian_2.id == guardian.id





