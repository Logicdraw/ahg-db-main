from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team import (
	team_crud,
)

from main.schemas.data.team import (
	TeamSchemaCreate,
	TeamSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest




@pytest.mark.asyncio
async def test_create_team(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()
	city = random_lower_string()
	province = 'NB'
	gender = 'male'

	team_in = TeamSchemaCreate(
		name=name,
		city=city,
		province=province,
		gender=gender,
	)

	team = await team_crud.create(
		db=db,
		obj_in=team_in,
	)

	assert team.name == name
	assert team.city == city
	assert team.province == province
	assert team.gender == gender



@pytest.mark.asyncio
async def test_create_sync_team(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()
	city = random_lower_string()
	province = 'NB'
	gender = 'male'

	team_in = TeamSchemaCreate(
		name=name,
		city=city,
		province=province,
		gender=gender,
	)

	team = await db.run_sync(
		team_crud.create_sync,
		obj_in=team_in,
	)

	assert team.name == name
	assert team.city == city
	assert team.province == province
	assert team.gender == gender



@pytest.mark.asyncio
async def test_get_team(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()
	city = random_lower_string()
	province = 'NB'
	gender = 'male'

	team_in = TeamSchemaCreate(
		name=name,
		city=city,
		province=province,
		gender=gender,
	)

	team = await team_crud.create(
		db=db,
		obj_in=team_in,
	)

	team_2 = await team_crud.get(
		db=db,
		id=team.id,
	)

	assert team_2
	assert jsonable_encoder(team_2) == jsonable_encoder(team)



@pytest.mark.asyncio
async def test_get_sync_team(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()
	city = random_lower_string()
	province = 'NB'
	gender = 'male'

	team_in = TeamSchemaCreate(
		name=name,
		city=city,
		province=province,
		gender=gender,
	)

	team = await db.run_sync(
		team_crud.create_sync,
		obj_in=team_in,
	)

	team_2 = await db.run_sync(
		team_crud.get_sync,
		id=team.id,
	)

	assert team_2
	assert jsonable_encoder(team_2) == jsonable_encoder(team)




@pytest.mark.asyncio
async def test_update_team(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()
	city = random_lower_string()
	province = 'NB'
	gender = 'male'

	team_in = TeamSchemaCreate(
		name=name,
		city=city,
		province=province,
		gender=gender,
	)

	team = await team_crud.create(
		db=db,
		obj_in=team_in,
	)

	new_name = random_lower_string()
	while new_name == name:
		new_name = random_lower_string()

	team_in_update = TeamSchemaUpdate(
		name=new_name,
	)

	team_2 = await team_crud.update(
		db=db,
		db_obj=team,
		obj_in=team_in_update,
	)

	assert team_2
	assert team_2.name
	assert team_2.name == new_name



@pytest.mark.asyncio
async def test_update_sync_team(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	city = random_lower_string()
	province = 'NB'
	gender = 'male'

	team_in = TeamSchemaCreate(
		name=name,
		city=city,
		province=province,
		gender=gender,
	)

	team = await db.run_sync(
		team_crud.create_sync,
		obj_in=team_in,
	)

	new_name = random_lower_string()
	while new_name == name:
		new_name = random_lower_string()

	team_in_update = TeamSchemaUpdate(
		name=new_name,
	)

	team_2 = await db.run_sync(
		team_crud.update_sync,
		db_obj=team,
		obj_in=team_in_update,
	)

	assert team_2
	assert team_2.name
	assert team_2.name == new_name



@pytest.mark.asyncio
async def test_delete_team(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	city = random_lower_string()
	province = 'NB'
	gender = 'male'

	team_in = TeamSchemaCreate(
		name=name,
		city=city,
		province=province,
		gender=gender,
	)

	team = await team_crud.create(
		db=db,
		obj_in=team_in,
	)

	team_2 = await team_crud.delete(
		db=db,
		id=team.id,
	)

	team_3 = await team_crud.get(
		db=db,
		id=team.id,
	)

	assert team_3 is None
	assert team_2.id == team.id



@pytest.mark.asyncio
async def test_delete_sync_team(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	city = random_lower_string()
	province = 'NB'
	gender = 'male'

	team_in = TeamSchemaCreate(
		name=name,
		city=city,
		province=province,
		gender=gender,
	)

	team = await db.run_sync(
		team_crud.create_sync,
		obj_in=team_in,
	)

	team_2 = await db.run_sync(
		team_crud.delete_sync,
		id=team.id,
	)

	team_3 = await db.run_sync(
		team_crud.get_sync,
		id=team.id,
	)

	assert team_3 is None
	assert team_2.id == team.id



