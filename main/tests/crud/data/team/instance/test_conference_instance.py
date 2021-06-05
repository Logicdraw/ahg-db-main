from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.instance.conference import (
	conference_instance_crud,
)

from main.schemas.data.team.instance.conference import (
	ConferenceInstanceSchemaCreate,
	ConferenceInstanceSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest




@pytest.mark.asyncio
async def test_create_conference_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	conference_instance_in = ConferenceInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	conference_instance = await conference_instance_crud.create(
		db=db,
		obj_in=conference_instance_in,
	)

	assert conference_instance.year_start == year_start
	assert conference_instance.year_end == year_end



@pytest.mark.asyncio
async def test_create_sync_conference_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	conference_instance_in = ConferenceInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	conference_instance = await db.run_sync(
		conference_instance_crud.create_sync,
		obj_in=conference_instance_in,
	)

	assert conference_instance.year_start == year_start
	assert conference_instance.year_end == year_end



@pytest.mark.asyncio
async def test_get_conference_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	conference_instance_in = ConferenceInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	conference_instance = await conference_instance_crud.create(
		db=db,
		obj_in=conference_instance_in,
	)

	conference_instance_2 = await conference_instance_crud.get(
		db=db,
		id=conference_instance.id,
	)

	assert conference_instance_2
	assert jsonable_encoder(conference_instance_2) == jsonable_encoder(conference_instance)



@pytest.mark.asyncio
async def test_get_sync_conference_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	conference_instance_in = ConferenceInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	conference_instance = await db.run_sync(
		conference_instance_crud.create_sync,
		obj_in=conference_instance_in,
	)

	conference_instance_2 = await db.run_sync(
		conference_instance_crud.get_sync,
		id=conference_instance.id,
	)

	assert conference_instance_2
	assert jsonable_encoder(conference_instance_2) == jsonable_encoder(conference_instance)



@pytest.mark.asyncio
async def test_update_conference_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	conference_instance_in = ConferenceInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	conference_instance = await conference_instance_crud.create(
		db=db,
		obj_in=conference_instance_in,
	)

	new_year_start = 2022

	conference_instance_in_update = ConferenceInstanceSchemaUpdate(
		year_start=new_year_start,
	)

	conference_instance_2 = await conference_instance_crud.update(
		db=db,
		db_obj=conference_instance,
		obj_in=conference_instance_in_update,
	)

	assert conference_instance_2
	assert conference_instance_2.year_start
	assert conference_instance_2.year_start == new_year_start



@pytest.mark.asyncio
async def test_update_sync_conference_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	conference_instance_in = ConferenceInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	conference_instance = await db.run_sync(
		conference_instance_crud.create_sync,
		obj_in=conference_instance_in,
	)

	new_year_start = 2022

	conference_instance_in_update = ConferenceInstanceSchemaUpdate(
		year_start=new_year_start,
	)

	conference_instance_2 = await db.run_sync(
		conference_instance_crud.update_sync,
		db_obj=conference_instance,
		obj_in=conference_instance_in_update,
	)

	assert conference_instance_2
	assert conference_instance_2.year_start
	assert conference_instance_2.year_start == new_year_start




@pytest.mark.asyncio
async def test_delete_conference_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	conference_instance_in = ConferenceInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	conference_instance = await conference_instance_crud.create(
		db=db,
		obj_in=conference_instance_in,
	)

	conference_instance_2 = await conference_instance_crud.delete(
		db=db,
		id=conference_instance.id,
	)

	conference_instance_3 = await conference_instance_crud.get(
		db=db,
		id=conference_instance.id,
	)

	assert conference_instance_3 is None
	assert conference_instance_2.id == conference_instance.id


@pytest.mark.asyncio
async def test_delete_sync_conference_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	conference_instance_in = ConferenceInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	conference_instance = await db.run_sync(
		conference_instance_crud.create_sync,
		obj_in=conference_instance_in,
	)

	conference_instance_2 = await db.run_sync(
		conference_instance_crud.delete_sync,
		id=conference_instance.id,
	)

	conference_instance_3 = await db.run_sync(
		conference_instance_crud.get_sync,
		id=conference_instance.id,
	)

	assert conference_instance_3 is None
	assert conference_instance_2.id == conference_instance.id





