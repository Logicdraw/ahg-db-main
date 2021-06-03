from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.season import (
	season_crud,
)

from main.schemas.data.team.season import (
	SeasonSchemaCreate,
	SeasonSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest





@pytest.mark.asyncio
async def test_create_season(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()

	season_in = SeasonSchemaCreate(
		name=name,
	)

	season = await season_crud.create(
		db=db,
		obj_in=season_in,
	)

	assert season.name == name


@pytest.mark.asyncio
async def test_create_sync_season(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()

	season_in = SeasonSchemaCreate(
		name=name,
	)

	season = await db.run_sync(
		season_crud.create_sync,
		obj_in=season_in,
	)

	assert season.name == name



@pytest.mark.asyncio
async def test_get_season(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	season_in = SeasonSchemaCreate(
		name=name,
	)

	season = await season_crud.create(
		db=db,
		obj_in=season_in,
	)

	season_2 = await season_crud.get(
		db=db,
		id=season.id,
	)

	assert season_2
	assert jsonable_encoder(season_2) == jsonable_encoder(season)



@pytest.mark.asyncio
async def test_get_sync_season(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	season_in = SeasonSchemaCreate(
		name=name,
	)

	season = await db.run_sync(
		season_crud.create_sync,
		obj_in=season_in,
	)

	season_2 = await db.run_sync(
		season_crud.get_sync,
		id=season.id,
	)

	assert season_2
	assert jsonable_encoder(season_2) == jsonable_encoder(season)



@pytest.mark.asyncio
async def test_update_season(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	season_in = SeasonSchemaCreate(
		name=name,
	)

	season = await season_crud.create(
		db=db,
		obj_in=season_in,
	)

	new_name = random_lower_string()
	while new_name == name:
		new_name = random_lower_string()

	season_in_update = SeasonSchemaUpdate(
		name=new_name,
	)

	season_2 = await season_crud.update(
		db=db,
		db_obj=season,
		obj_in=season_in_update,
	)

	assert season_2
	assert season_2.name
	assert season_2.name == new_name



@pytest.mark.asyncio
async def test_update_sync_season(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	season_in = SeasonSchemaCreate(
		name=name,
	)

	season = await db.run_sync(
		season_crud.create_sync,
		obj_in=season_in,
	)

	new_name = random_lower_string()
	while new_name == name:
		new_name = random_lower_string()

	season_in_update = SeasonSchemaUpdate(
		name=new_name,
	)

	season_2 = await db.run_sync(
		season_crud.update_sync,
		db_obj=season,
		obj_in=season_in_update,
	)

	assert season_2
	assert season_2.name
	assert season_2.name == new_name



@pytest.mark.asyncio
async def test_delete_season(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	season_in = SeasonSchemaCreate(
		name=name,
	)

	season = await season_crud.create(
		db=db,
		obj_in=season_in,
	)

	season_2 = await season_crud.delete(
		db=db,
		id=season.id,
	)

	season_3 = await season_crud.get(
		db=db,
		id=season.id,
	)

	assert season_3 is None
	assert season_2.id == season.id



@pytest.mark.asyncio
async def test_delete_sync_season(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	season_in = SeasonSchemaCreate(
		name=name,
	)

	season = await db.run_sync(
		season_crud.create_sync,
		obj_in=season_in,
	)

	season_2 = await db.run_sync(
		season_crud.delete_sync,
		id=season.id,
	)

	season_3 = await db.run_sync(
		season_crud.get_sync,
		id=season.id,
	)

	assert season_3 is None
	assert season_2.id == season.id




