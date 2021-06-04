from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud._many.team_instances_players import (
	team_instances_players_crud,
)

from main.schemas._many.team_instances_players import (
	TeamInstancesPlayersSchemaCreate,
	TeamInstancesPlayersSchemaUpdate,
)



from main.crud.data.team.instance import (
	team_instance_crud,
)

from main.schemas.data.team.instance import (
	TeamInstanceSchemaCreate,
	TeamInstanceSchemaUpdate,
)


from main.crud.data.person.player import (
	player_crud,
)

from main.schemas.data.person.player import (
	PlayerSchemaCreate,
	PlayerSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)



import pytest





@pytest.mark.asyncio
async def test_create_team_instance_player(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await team_instance_crud.create(
		db=db,
		obj_in=team_instance_in,
	)


	player_in = PlayerSchemaCreate()

	player = await player_crud.create(
		db=db,
		obj_in=player_in,
	)


	team_instance_player_in = TeamInstancesPlayersSchemaCreate(
		team_instance_id=team_instance.id,
		player_id=player.id,
		position='banana',
	)

	team_instance_player = await team_instances_players_crud.create(
		db=db,
		obj_in=team_instance_player_in,
	)


	assert team_instance_player.team_instance_id == team_instance.id
	assert team_instance_player.player_id == player.id



@pytest.mark.asyncio
async def test_create_sync_team_instance_player(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await db.run_sync(
		team_instance_crud.create_sync,
		obj_in=team_instance_in,
	)


	player_in = PlayerSchemaCreate()

	player = await db.run_sync(
		player_crud.create_sync,
		obj_in=player_in,
	)


	team_instance_player_in = TeamInstancesPlayersSchemaCreate(
		team_instance_id=team_instance.id,
		player_id=player.id,
		position='banana',
	)

	team_instance_player = await db.run_sync(
		team_instances_players_crud.create_sync,
		obj_in=team_instance_player_in,
	)


	assert team_instance_player.team_instance_id == team_instance.id
	assert team_instance_player.player_id == player.id



@pytest.mark.asyncio
async def test_get_team_instance_player(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await team_instance_crud.create(
		db=db,
		obj_in=team_instance_in,
	)


	player_in = PlayerSchemaCreate()

	player = await player_crud.create(
		db=db,
		obj_in=player_in,
	)


	team_instance_player_in = TeamInstancesPlayersSchemaCreate(
		team_instance_id=team_instance.id,
		player_id=player.id,
		position='banana',
	)

	team_instance_player = await team_instances_players_crud.create(
		db=db,
		obj_in=team_instance_player_in,
	)


	team_instance_player_2 = await team_instances_players_crud.get(
		db=db,
		team_instance_id=team_instance_player.team_instance_id,
		player_id=team_instance_player.player_id,
	)

	assert team_instance_player_2
	assert jsonable_encoder(team_instance_player) == jsonable_encoder(team_instance_player_2)



@pytest.mark.asyncio
async def test_get_sync_team_instance_player(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await db.run_sync(
		team_instance_crud.create_sync,
		obj_in=team_instance_in,
	)


	player_in = PlayerSchemaCreate()

	player = await db.run_sync(
		player_crud.create_sync,
		obj_in=player_in,
	)


	team_instance_player_in = TeamInstancesPlayersSchemaCreate(
		team_instance_id=team_instance.id,
		player_id=player.id,
		position='banana',
	)

	team_instance_player = await db.run_sync(
		team_instances_players_crud.create_sync,
		obj_in=team_instance_player_in,
	)


	team_instance_player_2 = await db.run_sync(
		team_instances_players_crud.get_sync,
		team_instance_id=team_instance_player.team_instance_id,
		player_id=team_instance_player.player_id,
	)

	assert team_instance_player_2
	assert jsonable_encoder(team_instance_player) == jsonable_encoder(team_instance_player_2)



@pytest.mark.asyncio
async def test_update_team_instance_player(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await team_instance_crud.create(
		db=db,
		obj_in=team_instance_in,
	)


	player_in = PlayerSchemaCreate()

	player = await player_crud.create(
		db=db,
		obj_in=player_in,
	)


	team_instance_player_in = TeamInstancesPlayersSchemaCreate(
		team_instance_id=team_instance.id,
		player_id=player.id,
		position='banana',
	)

	team_instance_player = await team_instances_players_crud.create(
		db=db,
		obj_in=team_instance_player_in,
	)

	new_position = 'apple'

	team_instance_player_in_update = TeamInstancesPlayersSchemaUpdate(
		position=new_position,
	)

	team_instance_player_2 = await team_instances_players_crud.update(
		db=db,
		db_obj=team_instance_player,
		obj_in=team_instance_player_in_update,
	)

	assert team_instance_player_2
	assert team_instance_player_2.position is not None
	assert team_instance_player_2.position == new_position




@pytest.mark.asyncio
async def test_update_sync_team_instance_player(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await db.run_sync(
		team_instance_crud.create_sync,
		obj_in=team_instance_in,
	)


	player_in = PlayerSchemaCreate()

	player = await db.run_sync(
		player_crud.create_sync,
		obj_in=player_in,
	)


	team_instance_player_in = TeamInstancesPlayersSchemaCreate(
		team_instance_id=team_instance.id,
		player_id=player.id,
		position='banana',
	)

	team_instance_player = await db.run_sync(
		team_instances_players_crud.create_sync,
		obj_in=team_instance_player_in,
	)


	new_position = 'apple'

	team_instance_player_in_update = TeamInstancesPlayersSchemaUpdate(
		position=new_position,
	)

	team_instance_player_2 = await db.run_sync(
		team_instances_players_crud.update_sync,
		db_obj=team_instance_player,
		obj_in=team_instance_player_in_update,
	)

	assert team_instance_player_2
	assert team_instance_player_2.position is not None
	assert team_instance_player_2.position == new_position




@pytest.mark.asyncio
async def test_delete_team_instance_player(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await team_instance_crud.create(
		db=db,
		obj_in=team_instance_in,
	)


	player_in = PlayerSchemaCreate()

	player = await player_crud.create(
		db=db,
		obj_in=player_in,
	)


	team_instance_player_in = TeamInstancesPlayersSchemaCreate(
		team_instance_id=team_instance.id,
		player_id=player.id,
		position='banana',
	)

	team_instance_player = await team_instances_players_crud.create(
		db=db,
		obj_in=team_instance_player_in,
	)

	team_instance_player_2 = await team_instances_players_crud.delete(
		db=db,
		team_instance_id=team_instance.id,
		player_id=player.id,
	)

	team_instance_player_3 = await team_instances_players_crud.get(
		db=db,
		team_instance_id=team_instance.id,
		player_id=player.id,
	)

	assert team_instance_player_3 is None
	assert team_instance_player_2.team_instance_id == team_instance_player.team_instance_id
	assert team_instance_player_2.player_id == team_instance_player.player_id



@pytest.mark.asyncio
async def test_delete_sync_team_instance_player(
	db: AsyncSession,
) -> None:
	# --

	team_instance_in = TeamInstanceSchemaCreate()

	team_instance = await db.run_sync(
		team_instance_crud.create_sync,
		obj_in=team_instance_in,
	)


	player_in = PlayerSchemaCreate()

	player = await db.run_sync(
		player_crud.create_sync,
		obj_in=player_in,
	)


	team_instance_player_in = TeamInstancesPlayersSchemaCreate(
		team_instance_id=team_instance.id,
		player_id=player.id,
		position='banana',
	)

	team_instance_player = await db.run_sync(
		team_instances_players_crud.create_sync,
		obj_in=team_instance_player_in,
	)

	team_instance_player_2 = await db.run_sync(
		team_instances_players_crud.delete_sync,
		team_instance_id=team_instance.id,
		player_id=player.id,
	)

	team_instance_player_3 = await db.run_sync(
		team_instances_players_crud.get_sync,
		team_instance_id=team_instance.id,
		player_id=player.id,
	)

	assert team_instance_player_3 is None
	assert team_instance_player_2.team_instance_id == team_instance_player.team_instance_id
	assert team_instance_player_2.player_id == team_instance_player.player_id




