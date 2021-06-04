from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud._many.guardians_players import (
	guardians_players_crud,
)

from main.schemas._many.guardians_players import (
	GuardiansPlayersSchemaCreate,
	GuardiansPlayersSchemaUpdate,
)


from main.crud.data.person.guardian import (
	guardian_crud,
)

from main.schemas.data.person.guardian import (
	GuardianSchemaCreate,
	GuardianSchemaUpdate,
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
async def test_create_guardian_player(
	db: AsyncSession,
) -> None:
	# --

	guardian_in = GuardianSchemaCreate()

	guardian = await guardian_crud.create(
		db=db,
		obj_in=guardian_in,
	)


	player_in = PlayerSchemaCreate()

	player = await player_crud.create(
		db=db,
		obj_in=player_in,
	)


	guardian_player_in = GuardiansPlayersSchemaCreate(
		guardian_id=guardian.id,
		player_id=player.id,
		role='banana',
		is_emergency_contact=True,
	)

	guardian_player = await guardians_players_crud.create(
		db=db,
		obj_in=guardian_player_in,
	)


	assert guardian_player.guardian_id == guardian.id
	assert guardian_player.player_id == player.id




@pytest.mark.asyncio
async def test_create_sync_guardian_player(
	db: AsyncSession,
) -> None:
	# --

	guardian_in = GuardianSchemaCreate()

	guardian = await db.run_sync(
		guardian_crud.create_sync,
		obj_in=guardian_in,
	)


	player_in = PlayerSchemaCreate()

	player = await db.run_sync(
		player_crud.create_sync,
		obj_in=player_in,
	)


	guardian_player_in = GuardiansPlayersSchemaCreate(
		guardian_id=guardian.id,
		player_id=player.id,
		role='banana',
		is_emergency_contact=True,
	)

	guardian_player = await db.run_sync(
		guardians_players_crud.create_sync,
		obj_in=guardian_player_in,
	)


	assert guardian_player.guardian_id == guardian.id
	assert guardian_player.player_id == player.id




@pytest.mark.asyncio
async def test_get_guardian_player(
	db: AsyncSession,
) -> None:
	# --

	guardian_in = GuardianSchemaCreate()

	guardian = await guardian_crud.create(
		db=db,
		obj_in=guardian_in,
	)


	player_in = PlayerSchemaCreate()

	player = await player_crud.create(
		db=db,
		obj_in=player_in,
	)


	guardian_player_in = GuardiansPlayersSchemaCreate(
		guardian_id=guardian.id,
		player_id=player.id,
		role='banana',
		is_emergency_contact=True,
	)

	guardian_player = await guardians_players_crud.create(
		db=db,
		obj_in=guardian_player_in,
	)

	guardian_player_2 = await guardians_players_crud.get(
		db=db,
		guardian_id=guardian.id,
		player_id=player.id,
	)

	assert guardian_player_2
	assert jsonable_encoder(guardian_player) == jsonable_encoder(guardian_player_2)




@pytest.mark.asyncio
async def test_get_sync_guardian_player(
	db: AsyncSession,
) -> None:
	# --

	guardian_in = GuardianSchemaCreate()

	guardian = await db.run_sync(
		guardian_crud.create_sync,
		obj_in=guardian_in,
	)


	player_in = PlayerSchemaCreate()

	player = await db.run_sync(
		player_crud.create_sync,
		obj_in=player_in,
	)


	guardian_player_in = GuardiansPlayersSchemaCreate(
		guardian_id=guardian.id,
		player_id=player.id,
		role='banana',
		is_emergency_contact=True,
	)

	guardian_player = await db.run_sync(
		guardians_players_crud.create_sync,
		obj_in=guardian_player_in,
	)

	guardian_player_2 = await db.run_sync(
		guardians_players_crud.get_sync,
		guardian_id=guardian.id,
		player_id=player.id,
	)

	assert guardian_player_2
	assert jsonable_encoder(guardian_player) == jsonable_encoder(guardian_player_2)



@pytest.mark.asyncio
async def test_update_guardian_player(
	db: AsyncSession,
) -> None:
	# --

	guardian_in = GuardianSchemaCreate()

	guardian = await guardian_crud.create(
		db=db,
		obj_in=guardian_in,
	)


	player_in = PlayerSchemaCreate()

	player = await player_crud.create(
		db=db,
		obj_in=player_in,
	)


	guardian_player_in = GuardiansPlayersSchemaCreate(
		guardian_id=guardian.id,
		player_id=player.id,
		role='banana',
		is_emergency_contact=True,
	)

	guardian_player = await guardians_players_crud.create(
		db=db,
		obj_in=guardian_player_in,
	)

	new_role = 'apple'

	guardian_player_in_update = GuardiansPlayersSchemaUpdate(
		role=new_role,
	)

	guardian_player_2 = await guardians_players_crud.update(
		db=db,
		obj_in=guardian_player_in_update,
	)

	assert guardian_player_2
	assert guardian_player_2.role is not None
	assert guardian_player_2.role == new_role




@pytest.mark.asyncio
async def test_update_sync_guardian_player(
	db: AsyncSession,
) -> None:
	# --

	guardian_in = GuardianSchemaCreate()

	guardian = await db.run_sync(
		guardian_crud.create_sync,
		obj_in=guardian_in,
	)


	player_in = PlayerSchemaCreate()

	player = await db.run_sync(
		player_crud.create_sync,
		obj_in=player_in,
	)


	guardian_player_in = GuardiansPlayersSchemaCreate(
		guardian_id=guardian.id,
		player_id=player.id,
		role='banana',
		is_emergency_contact=True,
	)

	guardian_player = await db.run_sync(
		guardians_players_crud.create_sync,
		obj_in=guardian_player_in,
	)

	new_role = 'apple'

	guardian_player_in_update = GuardiansPlayersSchemaUpdate(
		role=new_role,
	)

	guardian_player_2 = await db.run_sync(
		guardians_players_crud.update_sync,
		obj_in=guardian_player_in_update,
	)

	assert guardian_player_2
	assert guardian_player_2.role is not None
	assert guardian_player_2.role == new_role



@pytest.mark.asyncio
async def test_delete_guardian_player(
	db: AsyncSession,
) -> None:
	# --

	guardian_in = GuardianSchemaCreate()

	guardian = await guardian_crud.create(
		db=db,
		obj_in=guardian_in,
	)


	player_in = PlayerSchemaCreate()

	player = await player_crud.create(
		db=db,
		obj_in=player_in,
	)


	guardian_player_in = GuardiansPlayersSchemaCreate(
		guardian_id=guardian.id,
		player_id=player.id,
		role='banana',
		is_emergency_contact=True,
	)

	guardian_player = await guardians_players_crud.create(
		db=db,
		obj_in=guardian_player_in,
	)

	guardian_player_2 = await guardians_players_crud.delete(
		db=db,
		guardian_id=guardian.id,
		player_id=player.id,
	)

	guardian_player_3 = await guardians_players_crud.get(
		db=db,
		guardian_id=guardian.id,
		player_id=player.id,
	)

	assert guardian_player_3 is None
	assert guardian_player_2.guardian_id == guardian_player.guardian_id
	assert guardian_player_2.player_id == guardian_player.player_id



@pytest.mark.asyncio
async def test_delete_sync_guardian_player(
	db: AsyncSession,
) -> None:
	# --

	guardian_in = GuardianSchemaCreate()

	guardian = await db.run_sync(
		guardian_crud.create_sync,
		obj_in=guardian_in,
	)


	player_in = PlayerSchemaCreate()

	player = await db.run_sync(
		player_crud.create_sync,
		obj_in=player_in,
	)


	guardian_player_in = GuardiansPlayersSchemaCreate(
		guardian_id=guardian.id,
		player_id=player.id,
		role='banana',
		is_emergency_contact=True,
	)

	guardian_player = await db.run_sync(
		guardians_players_crud.create_sync,
		obj_in=guardian_player_in,
	)

	guardian_player_2 = await db.run_sync(
		guardians_players_crud.delete_sync,
		guardian_id=guardian.id,
		player_id=player.id,
	)

	guardian_player_3 = await db.run_sync(
		guardians_players_crud.get_sync,
		guardian_id=guardian.id,
		player_id=player.id,
	)

	assert guardian_player_3 is None
	assert guardian_player_2.guardian_id == guardian_player.guardian_id
	assert guardian_player_2.player_id == guardian_player.player_id





