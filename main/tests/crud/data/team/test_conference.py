from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.conference import (
	conference_crud,
)

from main.schemas.data.team.conference import (
	ConferenceSchemaCreate,
	ConferenceSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest




@pytest.mark.asyncio
async def test_create_conference(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()

	conference_in = ConferenceSchemaCreate(
		name=name,
	)

	conference = await conference_crud.create(
		db=db,
		obj_in=conference_in,
	)

	assert conference.name == name


@pytest.mark.asyncio
async def test_create_sync_conference(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()

	conference_in = ConferenceSchemaCreate(
		name=name,
	)

	conference = await db.run_sync(
		conference_crud.create_sync,
		obj_in=conference_in,
	)

	assert conference.name == name



@pytest.mark.asyncio
async def test_get_conference(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	conference_in = ConferenceSchemaCreate(
		name=name,
	)

	conference = await conference_crud.create(
		db=db,
		obj_in=conference_in,
	)

	conference_2 = await conference_crud.get(
		db=db,
		id=conference.id,
	)

	assert conference_2
	assert jsonable_encoder(conference_2) == jsonable_encoder(conference)



@pytest.mark.asyncio
async def test_get_sync_conference(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	conference_in = ConferenceSchemaCreate(
		name=name,
	)

	conference = await db.run_sync(
		conference_crud.create_sync,
		obj_in=conference_in,
	)

	conference_2 = await db.run_sync(
		conference_crud.get_sync,
		id=conference.id,
	)

	assert conference_2
	assert jsonable_encoder(conference_2) == jsonable_encoder(conference)



@pytest.mark.asyncio
async def test_update_conference(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	conference_in = ConferenceSchemaCreate(
		name=name,
	)

	conference = await conference_crud.create(
		db=db,
		obj_in=conference_in,
	)

	new_name = random_lower_string()
	while new_name == name:
		new_name = random_lower_string()

	conference_in_update = ConferenceSchemaUpdate(
		name=new_name,
	)

	conference_2 = await conference_crud.update(
		db=db,
		db_obj=conference,
		obj_in=conference_in_update,
	)

	assert conference_2
	assert conference_2.name
	assert conference_2.name == new_name



@pytest.mark.asyncio
async def test_update_sync_conference(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	conference_in = ConferenceSchemaCreate(
		name=name,
	)

	conference = await db.run_sync(
		conference_crud.create_sync,
		obj_in=conference_in,
	)

	new_name = random_lower_string()
	while new_name == name:
		new_name = random_lower_string()

	conference_in_update = ConferenceSchemaUpdate(
		name=new_name,
	)

	conference_2 = await db.run_sync(
		conference_crud.update_sync,
		db_obj=conference,
		obj_in=conference_in_update,
	)

	assert conference_2
	assert conference_2.name
	assert conference_2.name == new_name



@pytest.mark.asyncio
async def test_delete_conference(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	conference_in = ConferenceSchemaCreate(
		name=name,
	)

	conference = await conference_crud.create(
		db=db,
		obj_in=conference_in,
	)

	conference_2 = await conference_crud.delete(
		db=db,
		id=conference.id,
	)

	conference_3 = await conference_crud.get(
		db=db,
		id=conference.id,
	)

	assert conference_3 is None
	assert conference_2.id == conference.id



@pytest.mark.asyncio
async def test_delete_sync_conference(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	conference_in = ConferenceSchemaCreate(
		name=name,
	)

	conference = await db.run_sync(
		conference_crud.create_sync,
		obj_in=conference_in,
	)

	conference_2 = await db.run_sync(
		conference_crud.delete_sync,
		id=conference.id,
	)

	conference_3 = await db.run_sync(
		conference_crud.get_sync,
		id=conference.id,
	)

	assert conference_3 is None
	assert conference_2.id == conference.id










