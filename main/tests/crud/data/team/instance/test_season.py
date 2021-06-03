from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.instance.season import (
	season_instance_crud,
)

from main.schemas.data.team.instance.season import (
	SeasonInstanceSchemaCreate,
	SeasonInstanceSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest





@pytest.mark.asyncio
async def test_create_season_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	season_instance_in = SeasonInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	season_instance = await season_instance_crud.create(
		db=db,
		obj_in=season_instance_in,
	)

	assert season_instance.year_start == year_start
	assert season_instance.year_end == year_end



@pytest.mark.asyncio
async def test_create_sync_season_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	season_instance_in = SeasonInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	season_instance = await db.run_sync(
		season_instance_crud.create_sync,
		obj_in=season_instance_in,
	)

	assert season_instance.year_start == year_start
	assert season_instance.year_end == year_end



@pytest.mark.asyncio
async def test_get_season_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	season_instance_in = SeasonInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	season_instance = await season_instance_crud.create(
		db=db,
		obj_in=season_instance_in,
	)

	season_instance_2 = await season_instance_crud.get(
		db=db,
		id=season_instance.id,
	)

	assert season_instance_2
	assert jsonable_encoder(season_instance_2) == jsonable_encoder(season_instance)



@pytest.mark.asyncio
async def test_get_sync_season_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	season_instance_in = SeasonInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	season_instance = await db.run_sync(
		season_instance_crud.create_sync,
		obj_in=season_instance_in,
	)

	season_instance_2 = await db.run_sync(
		season_instance_crud.get_sync,
		id=season_instance.id,
	)

	assert season_instance_2
	assert jsonable_encoder(season_instance_2) == jsonable_encoder(season_instance)



@pytest.mark.asyncio
async def test_update_season_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	season_instance_in = SeasonInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	season_instance = await season_instance_crud.create(
		db=db,
		obj_in=season_instance_in,
	)

	new_year_start = 2022

	season_instance_in_update = SeasonInstanceSchemaUpdate(
		year_start=new_year_start,
	)

	season_instance_2 = await season_instance_crud.update(
		db=db,
		db_obj=season_instance,
		obj_in=season_instance_in_update,
	)

	assert season_instance_2
	assert season_instance_2.year_start
	assert season_instance_2.year_start == new_year_start



@pytest.mark.asyncio
async def test_update_sync_season_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	season_instance_in = SeasonInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	season_instance = await db.run_sync(
		season_instance_crud.create_sync,
		obj_in=season_instance_in,
	)

	new_year_start = 2022

	season_instance_in_update = SeasonInstanceSchemaUpdate(
		year_start=new_year_start,
	)

	season_instance_2 = await db.run_sync(
		season_instance_crud.update_sync,
		db_obj=season_instance,
		obj_in=season_instance_in_update,
	)

	assert season_instance_2
	assert season_instance_2.year_start
	assert season_instance_2.year_start == new_year_start




@pytest.mark.asyncio
async def test_delete_season_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	season_instance_in = SeasonInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	season_instance = await season_instance_crud.create(
		db=db,
		obj_in=season_instance_in,
	)

	season_instance_2 = await season_instance_crud.delete(
		db=db,
		id=season_instance.id,
	)

	season_instance_3 = await season_instance_crud.get(
		db=db,
		id=season_instance.id,
	)

	assert season_instance_3 is None
	assert season_instance_2.id == season_instance.id


@pytest.mark.asyncio
async def test_delete_sync_season_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	season_instance_in = SeasonInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	season_instance = await db.run_sync(
		season_instance_crud.create_sync,
		obj_in=season_instance_in,
	)

	season_instance_2 = await db.run_sync(
		season_instance_crud.delete_sync,
		id=season_instance.id,
	)

	season_instance_3 = await db.run_sync(
		season_instance_crud.get_sync,
		id=season_instance.id,
	)

	assert season_instance_3 is None
	assert season_instance_2.id == season_instance.id



