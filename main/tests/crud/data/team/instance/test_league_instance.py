from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.instance.league import (
	league_instance_crud,
)

from main.schemas.data.team.instance.league import (
	LeagueInstanceSchemaCreate,
	LeagueInstanceSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest




@pytest.mark.asyncio
async def test_create_league_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	league_instance_in = LeagueInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	league_instance = await league_instance_crud.create(
		db=db,
		obj_in=league_instance_in,
	)

	assert league_instance.year_start == year_start
	assert league_instance.year_end == year_end



@pytest.mark.asyncio
async def test_create_sync_league_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	league_instance_in = LeagueInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	league_instance = await db.run_sync(
		league_instance_crud.create_sync,
		obj_in=league_instance_in,
	)

	assert league_instance.year_start == year_start
	assert league_instance.year_end == year_end



@pytest.mark.asyncio
async def test_get_league_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	league_instance_in = LeagueInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	league_instance = await league_instance_crud.create(
		db=db,
		obj_in=league_instance_in,
	)

	league_instance_2 = await league_instance_crud.get(
		db=db,
		id=league_instance.id,
	)

	assert league_instance_2
	assert jsonable_encoder(league_instance_2) == jsonable_encoder(league_instance)



@pytest.mark.asyncio
async def test_get_sync_league_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	league_instance_in = LeagueInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	league_instance = await db.run_sync(
		league_instance_crud.create_sync,
		obj_in=league_instance_in,
	)

	league_instance_2 = await db.run_sync(
		league_instance_crud.get_sync,
		id=league_instance.id,
	)

	assert league_instance_2
	assert jsonable_encoder(league_instance_2) == jsonable_encoder(league_instance)



@pytest.mark.asyncio
async def test_update_league_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	league_instance_in = LeagueInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	league_instance = await league_instance_crud.create(
		db=db,
		obj_in=league_instance_in,
	)

	new_year_start = 2022

	league_instance_in_update = LeagueInstanceSchemaUpdate(
		year_start=new_year_start,
	)

	league_instance_2 = await league_instance_crud.update(
		db=db,
		db_obj=league_instance,
		obj_in=league_instance_in_update,
	)

	assert league_instance_2
	assert league_instance_2.year_start
	assert league_instance_2.year_start == new_year_start



@pytest.mark.asyncio
async def test_update_sync_league_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	league_instance_in = LeagueInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	league_instance = await db.run_sync(
		league_instance_crud.create_sync,
		obj_in=league_instance_in,
	)

	new_year_start = 2022

	league_instance_in_update = LeagueInstanceSchemaUpdate(
		year_start=new_year_start,
	)

	league_instance_2 = await db.run_sync(
		league_instance_crud.update_sync,
		db_obj=league_instance,
		obj_in=league_instance_in_update,
	)

	assert league_instance_2
	assert league_instance_2.year_start
	assert league_instance_2.year_start == new_year_start




@pytest.mark.asyncio
async def test_delete_league_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	league_instance_in = LeagueInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	league_instance = await league_instance_crud.create(
		db=db,
		obj_in=league_instance_in,
	)

	league_instance_2 = await league_instance_crud.delete(
		db=db,
		id=league_instance.id,
	)

	league_instance_3 = await league_instance_crud.get(
		db=db,
		id=league_instance.id,
	)

	assert league_instance_3 is None
	assert league_instance_2.id == league_instance.id


@pytest.mark.asyncio
async def test_delete_sync_league_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	league_instance_in = LeagueInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	league_instance = await db.run_sync(
		league_instance_crud.create_sync,
		obj_in=league_instance_in,
	)

	league_instance_2 = await db.run_sync(
		league_instance_crud.delete_sync,
		id=league_instance.id,
	)

	league_instance_3 = await db.run_sync(
		league_instance_crud.get_sync,
		id=league_instance.id,
	)

	assert league_instance_3 is None
	assert league_instance_2.id == league_instance.id





