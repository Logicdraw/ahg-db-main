from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.league import (
	league_crud,
)

from main.schemas.data.team.league import (
	LeagueSchemaCreate,
	LeagueSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest




@pytest.mark.asyncio
async def test_create_league(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()

	league_in = LeagueSchemaCreate(
		name=name,
	)

	league = await league_crud.create(
		db=db,
		obj_in=league_in,
	)

	assert league.name == name


@pytest.mark.asyncio
async def test_create_sync_league(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()

	league_in = LeagueSchemaCreate(
		name=name,
	)

	league = await db.run_sync(
		league_crud.create_sync,
		obj_in=league_in,
	)

	assert league.name == name



@pytest.mark.asyncio
async def test_get_league(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	league_in = LeagueSchemaCreate(
		name=name,
	)

	league = await league_crud.create(
		db=db,
		obj_in=league_in,
	)

	league_2 = await league_crud.get(
		db=db,
		id=league.id,
	)

	assert league_2
	assert jsonable_encoder(league_2) == jsonable_encoder(league)



@pytest.mark.asyncio
async def test_get_sync_league(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	league_in = LeagueSchemaCreate(
		name=name,
	)

	league = await db.run_sync(
		league_crud.create_sync,
		obj_in=league_in,
	)

	league_2 = await db.run_sync(
		league_crud.get_sync,
		id=league.id,
	)

	assert league_2
	assert jsonable_encoder(league_2) == jsonable_encoder(league)



@pytest.mark.asyncio
async def test_update_league(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	league_in = LeagueSchemaCreate(
		name=name,
	)

	league = await league_crud.create(
		db=db,
		obj_in=league_in,
	)

	new_name = random_lower_string()
	while new_name == name:
		new_name = random_lower_string()

	league_in_update = LeagueSchemaUpdate(
		name=new_name,
	)

	league_2 = await league_crud.update(
		db=db,
		db_obj=league,
		obj_in=league_in_update,
	)

	assert league_2
	assert league_2.name
	assert league_2.name == new_name



@pytest.mark.asyncio
async def test_update_sync_league(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	league_in = LeagueSchemaCreate(
		name=name,
	)

	league = await db.run_sync(
		league_crud.create_sync,
		obj_in=league_in,
	)

	new_name = random_lower_string()
	while new_name == name:
		new_name = random_lower_string()

	league_in_update = LeagueSchemaUpdate(
		name=new_name,
	)

	league_2 = await db.run_sync(
		league_crud.update_sync,
		db_obj=league,
		obj_in=league_in_update,
	)

	assert league_2
	assert league_2.name
	assert league_2.name == new_name



@pytest.mark.asyncio
async def test_delete_league(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	league_in = LeagueSchemaCreate(
		name=name,
	)

	league = await league_crud.create(
		db=db,
		obj_in=league_in,
	)

	league_2 = await league_crud.delete(
		db=db,
		id=league.id,
	)

	league_3 = await league_crud.get(
		db=db,
		id=league.id,
	)

	assert league_3 is None
	assert league_2.id == league.id



@pytest.mark.asyncio
async def test_delete_sync_league(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	league_in = LeagueSchemaCreate(
		name=name,
	)

	league = await db.run_sync(
		league_crud.create_sync,
		obj_in=league_in,
	)

	league_2 = await db.run_sync(
		league_crud.delete_sync,
		id=league.id,
	)

	league_3 = await db.run_sync(
		league_crud.get_sync,
		id=league.id,
	)

	assert league_3 is None
	assert league_2.id == league.id







