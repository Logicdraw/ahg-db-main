from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.person.coach import (
	coach_crud,
)

from main.schemas.data.person.coach import (
	CoachSchemaCreate,
	CoachSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest




@pytest.mark.asyncio
async def test_create_coach(
	db: AsyncSession,
) -> None:
	# --
	full_name = random_name()
	email = random_email()

	coach_in = CoachSchemaCreate(
		full_name=full_name,
		email=email,
	)
	coach = await coach_crud.create(
		db=db,
		obj_in=coach_in,
	)

	assert coach
	assert coach.full_name == full_name
	assert coach.email == email



@pytest.mark.asyncio
async def test_create_sync_coach(
	db: AsyncSession,
) -> None:
	# --
	full_name = random_name()
	email = random_email()

	coach_in = CoachSchemaCreate(
		full_name=full_name,
		email=email,
	)

	coach = await db.run_sync(
		coach_crud.create_sync,
		obj_in=coach_in,
	)

	assert coach
	assert coach.full_name == full_name
	assert coach.email == email



@pytest.mark.asyncio
async def test_get_coach(
	db: AsyncSession,
) -> None:
	# --
	full_name = random_name()
	email = random_email()

	coach_in = CoachSchemaCreate(
		full_name=full_name,
		email=email,
	)

	coach = await coach_crud.create(
		db=db,
		obj_in=coach_in,
	)

	coach_2 = await coach_crud.get(
		db=db,
		id=coach.id,
	)

	assert coach_2
	assert jsonable_encoder(coach) == jsonable_encoder(coach_2)



@pytest.mark.asyncio
async def test_get_sync_coach(
	db: AsyncSession,
) -> None:
	# --
	full_name = random_name()
	email = random_email()

	coach_in = CoachSchemaCreate(
		full_name=full_name,
		email=email,
	)

	coach = await db.run_sync(
		coach_crud.create_sync,
		obj_in=coach_in,
	)

	coach_2 = await db.run_sync(
		coach_crud.get_sync,
		id=coach.id,
	)

	assert coach_2
	assert jsonable_encoder(coach) == jsonable_encoder(coach_2)



@pytest.mark.asyncio
async def test_update_coach(
	db: AsyncSession,
) -> None:
	# --
	full_name = random_name()
	email = random_email()

	coach_in = CoachSchemaCreate(
		full_name=full_name,
		email=email,
	)
	coach = await coach_crud.create(
		db=db,
		obj_in=coach_in,
	)

	new_full_name = random_name()

	coach_in_update = CoachSchemaUpdate(
		full_name=new_full_name, # New Name --
	)

	coach_2 = await coach_crud.update(
		db=db,
		db_obj=coach,
		obj_in=coach_in_update,
	)

	assert coach_2
	assert coach_2.full_name
	assert coach_2.full_name == new_full_name



@pytest.mark.asyncio
async def test_update_sync_coach(
	db: AsyncSession,
) -> None:
	# --
	full_name = random_name()
	email = random_email()

	coach_in = CoachSchemaCreate(
		full_name=full_name,
		email=email,
	)

	coach = await db.run_sync(
		coach_crud.create_sync,
		obj_in=coach_in,
	)


	new_full_name = random_name()

	coach_in_update = CoachSchemaUpdate(
		full_name=new_full_name, # New Name --
	)


	coach_2 = await db.run_sync(
		coach_crud.update_sync,
		db_obj=coach,
		obj_in=coach_in_update,
	)

	assert coach_2
	assert coach_2.full_name
	assert coach_2.full_name == new_full_name



@pytest.mark.asyncio
async def test_delete_coach(
	db: AsyncSession,
) -> None:
	# --
	full_name = random_name()
	email = random_email()

	coach_in = CoachSchemaCreate(
		full_name=full_name,
		email=email,
	)
	coach = await coach_crud.create(
		db=db,
		obj_in=coach_in,
	)

	coach_2 = await coach_crud.delete(
		db=db,
		id=coach.id,
	)

	coach_3 = await coach_crud.get(
		db=db,
		id=coach.id,
	)

	assert coach_3 is None
	assert coach_2.id == coach.id



@pytest.mark.asyncio
async def test_delete_sync_coach(
	db: AsyncSession,
) -> None:
	# --
	full_name = random_name()
	email = random_email()

	coach_in = CoachSchemaCreate(
		full_name=full_name,
		email=email,
	)

	coach = await db.run_sync(
		coach_crud.create_sync,
		obj_in=coach_in,
	)

	coach_2 = await db.run_sync(
		coach_crud.delete_sync,
		id=coach.id,
	)

	coach_3 = await db.run_sync(
		coach_crud.get_sync,
		id=coach.id,
	)


	assert coach_3 is None
	assert coach_2.id == coach.id





