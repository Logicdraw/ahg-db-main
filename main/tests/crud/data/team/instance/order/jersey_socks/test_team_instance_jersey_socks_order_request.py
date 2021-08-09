from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.instance.order.jersey_socks.request import (
	team_instance_jersey_socks_order_request_crud,
)

from main.schemas.data.team.instance.order.jersey_socks.request import (
	TeamInstanceJerseySocksOrderRequestSchemaCreate,
	TeamInstanceJerseySocksOrderRequestSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
	random_number,
)


from uuid import uuid4


import pytest





@pytest.mark.asyncio
async def test_create_team_instance_jersey_socks_order_request(
	db: AsyncSession,
) -> None:
	# --

	player_full_name = random_lower_string()
	jersey_number = random_number(min_digits=1, max_digits=2)
	jersey_size = 'YXL'
	socks_size = '24in'
	details = random_lower_string()
	approved = False
	rejected = True
	rejected_reason = random_lower_string()

	team_instance_jersey_socks_order_request_in = TeamInstanceJerseySocksOrderRequestSchemaCreate(
		player_full_name=player_full_name,
		jersey_number=jersey_number,
		jersey_size=jersey_size,
		socks_size=socks_size,
		details=details,
		approved=approved,
		rejected=rejected,
		rejected_reason=rejected_reason,
	)

	team_instance_jersey_socks_order_request = await team_instance_jersey_socks_order_request_crud.create(
		db=db,
		obj_in=team_instance_jersey_socks_order_request_in,
	)

	assert team_instance_jersey_socks_order_request.player_full_name == player_full_name




@pytest.mark.asyncio
async def test_create_sync_team_instance_jersey_socks_order_request(
	db: AsyncSession,
) -> None:
	# --

	player_full_name = random_lower_string()
	jersey_number = random_number(min_digits=1, max_digits=2)
	jersey_size = 'YXL'
	socks_size = '24in'
	details = random_lower_string()
	approved = False
	rejected = True
	rejected_reason = random_lower_string()

	team_instance_jersey_socks_order_request_in = TeamInstanceJerseySocksOrderRequestSchemaCreate(
		player_full_name=player_full_name,
		jersey_number=jersey_number,
		jersey_size=jersey_size,
		socks_size=socks_size,
		details=details,
		approved=approved,
		rejected=rejected,
		rejected_reason=rejected_reason,
	)

	team_instance_jersey_socks_order_request = await db.run_sync(
		team_instance_jersey_socks_order_request_crud.create_sync,
		obj_in=team_instance_jersey_socks_order_request_in,
	)

	assert team_instance_jersey_socks_order_request.player_full_name == player_full_name




@pytest.mark.asyncio
async def test_get_team_instance_jersey_socks_order_request(
	db: AsyncSession,
) -> None:
	# --

	player_full_name = random_lower_string()
	jersey_number = random_number(min_digits=1, max_digits=2)
	jersey_size = 'YXL'
	socks_size = '24in'
	details = random_lower_string()
	approved = False
	rejected = True
	rejected_reason = random_lower_string()

	team_instance_jersey_socks_order_request_in = TeamInstanceJerseySocksOrderRequestSchemaCreate(
		player_full_name=player_full_name,
		jersey_number=jersey_number,
		jersey_size=jersey_size,
		socks_size=socks_size,
		details=details,
		approved=approved,
		rejected=rejected,
		rejected_reason=rejected_reason,
	)

	team_instance_jersey_socks_order_request = await team_instance_jersey_socks_order_request_crud.create(
		db=db,
		obj_in=team_instance_jersey_socks_order_request_in,
	)

	team_instance_jersey_socks_order_request_2 = await team_instance_jersey_socks_order_request_crud.get(
		db=db,
		id=team_instance_jersey_socks_order_request.id,
	)

	assert team_instance_jersey_socks_order_request_2
	assert jsonable_encoder(team_instance_jersey_socks_order_request_2) == jsonable_encoder(team_instance_jersey_socks_order_request)



@pytest.mark.asyncio
async def test_get_sync_team_instance_jersey_socks_order_request(
	db: AsyncSession,
) -> None:
	# --

	player_full_name = random_lower_string()
	jersey_number = random_number(min_digits=1, max_digits=2)
	jersey_size = 'YXL'
	socks_size = '24in'
	details = random_lower_string()
	approved = False
	rejected = True
	rejected_reason = random_lower_string()

	team_instance_jersey_socks_order_request_in = TeamInstanceJerseySocksOrderRequestSchemaCreate(
		player_full_name=player_full_name,
		jersey_number=jersey_number,
		jersey_size=jersey_size,
		socks_size=socks_size,
		details=details,
		approved=approved,
		rejected=rejected,
		rejected_reason=rejected_reason,
	)

	team_instance_jersey_socks_order_request = await db.run_sync(
		team_instance_jersey_socks_order_request_crud.create_sync,
		obj_in=team_instance_jersey_socks_order_request_in,
	)

	team_instance_jersey_socks_order_request_2 = await db.run_sync(
		team_instance_jersey_socks_order_request_crud.get_sync,
		id=team_instance_jersey_socks_order_request.id,
	)

	assert team_instance_jersey_socks_order_request_2
	assert jsonable_encoder(team_instance_jersey_socks_order_request_2) == jsonable_encoder(team_instance_jersey_socks_order_request)




@pytest.mark.asyncio
async def test_update_team_instance_jersey_socks_order_request(
	db: AsyncSession,
) -> None:
	# --

	player_full_name = random_lower_string()
	jersey_number = random_number(min_digits=1, max_digits=2)
	jersey_size = 'YXL'
	socks_size = '24in'
	details = random_lower_string()
	approved = False
	rejected = True
	rejected_reason = random_lower_string()

	team_instance_jersey_socks_order_request_in = TeamInstanceJerseySocksOrderRequestSchemaCreate(
		player_full_name=player_full_name,
		jersey_number=jersey_number,
		jersey_size=jersey_size,
		socks_size=socks_size,
		details=details,
		approved=approved,
		rejected=rejected,
		rejected_reason=rejected_reason,
	)

	team_instance_jersey_socks_order_request = await team_instance_jersey_socks_order_request_crud.create(
		db=db,
		obj_in=team_instance_jersey_socks_order_request_in,
	)

	new_player_full_name = random_lower_string()

	team_instance_jersey_socks_order_request_in_update = TeamInstanceJerseySocksOrderRequestSchemaUpdate(
		player_full_name=new_player_full_name,
	)

	team_instance_jersey_socks_order_request_2 = await team_instance_jersey_socks_order_request_crud.update(
		db=db,
		db_obj=team_instance_jersey_socks_order_request,
		obj_in=team_instance_jersey_socks_order_request_in_update,
	)

	assert team_instance_jersey_socks_order_request_2
	assert team_instance_jersey_socks_order_request_2.player_full_name
	assert team_instance_jersey_socks_order_request_2.player_full_name == new_player_full_name




@pytest.mark.asyncio
async def test_update_sync_team_instance_jersey_socks_order_request(
	db: AsyncSession,
) -> None:
	# --

	player_full_name = random_lower_string()
	jersey_number = random_number(min_digits=1, max_digits=2)
	jersey_size = 'YXL'
	socks_size = '24in'
	details = random_lower_string()
	approved = False
	rejected = True
	rejected_reason = random_lower_string()

	team_instance_jersey_socks_order_request_in = TeamInstanceJerseySocksOrderRequestSchemaCreate(
		player_full_name=player_full_name,
		jersey_number=jersey_number,
		jersey_size=jersey_size,
		socks_size=socks_size,
		details=details,
		approved=approved,
		rejected=rejected,
		rejected_reason=rejected_reason,
	)

	team_instance_jersey_socks_order_request = await db.run_sync(
		team_instance_jersey_socks_order_request_crud.create_sync,
		obj_in=team_instance_jersey_socks_order_request_in,
	)


	new_player_full_name = random_lower_string()
	jersey_number = random_number(min_digits=1, max_digits=2)
	jersey_size = 'YXL'
	socks_size = '24in'
	details = random_lower_string()
	approved = False
	rejected = True
	rejected_reason = random_lower_string()


	team_instance_jersey_socks_order_request_in_update = TeamInstanceJerseySocksOrderRequestSchemaUpdate(
		player_full_name=new_player_full_name,
	)

	team_instance_jersey_socks_order_request_2 = await db.run_sync(
		team_instance_jersey_socks_order_request_crud.update_sync,
		db_obj=team_instance_jersey_socks_order_request,
		obj_in=team_instance_jersey_socks_order_request_in_update,
	)

	assert team_instance_jersey_socks_order_request_2
	assert team_instance_jersey_socks_order_request_2.player_full_name
	assert team_instance_jersey_socks_order_request_2.player_full_name == new_player_full_name



@pytest.mark.asyncio
async def test_delete_team_instance_jersey_socks_order_request(
	db: AsyncSession,
) -> None:
	# --

	player_full_name = random_lower_string()
	jersey_number = random_number(min_digits=1, max_digits=2)
	jersey_size = 'YXL'
	socks_size = '24in'
	details = random_lower_string()
	approved = False
	rejected = True
	rejected_reason = random_lower_string()

	team_instance_jersey_socks_order_request_in = TeamInstanceJerseySocksOrderRequestSchemaCreate(
		player_full_name=player_full_name,
		jersey_number=jersey_number,
		jersey_size=jersey_size,
		socks_size=socks_size,
		details=details,
		approved=approved,
		rejected=rejected,
		rejected_reason=rejected_reason,
	)

	team_instance_jersey_socks_order_request = await team_instance_jersey_socks_order_request_crud.create(
		db=db,
		obj_in=team_instance_jersey_socks_order_request_in,
	)

	team_instance_jersey_socks_order_request_2 = await team_instance_jersey_socks_order_request_crud.delete(
		db=db,
		id=team_instance_jersey_socks_order_request.id,
	)

	team_instance_jersey_socks_order_request_3 = await team_instance_jersey_socks_order_request_crud.get(
		db=db,
		id=team_instance_jersey_socks_order_request.id,
	)

	assert team_instance_jersey_socks_order_request_3 is None
	assert team_instance_jersey_socks_order_request_2.id == team_instance_jersey_socks_order_request.id



@pytest.mark.asyncio
async def test_delete_sync_team_instance_jersey_socks_order_request(
	db: AsyncSession,
) -> None:
	# --

	player_full_name = random_lower_string()
	jersey_number = random_number(min_digits=1, max_digits=2)
	jersey_size = 'YXL'
	socks_size = '24in'
	details = random_lower_string()
	approved = False
	rejected = True
	rejected_reason = random_lower_string()

	team_instance_jersey_socks_order_request_in = TeamInstanceJerseySocksOrderRequestSchemaCreate(
		player_full_name=player_full_name,
		jersey_number=jersey_number,
		jersey_size=jersey_size,
		socks_size=socks_size,
		details=details,
		approved=approved,
		rejected=rejected,
		rejected_reason=rejected_reason,
	)

	team_instance_jersey_socks_order_request = await db.run_sync(
		team_instance_jersey_socks_order_request_crud.create_sync,
		obj_in=team_instance_jersey_socks_order_request_in,
	)

	team_instance_jersey_socks_order_request_2 = await db.run_sync(
		team_instance_jersey_socks_order_request_crud.delete_sync,
		id=team_instance_jersey_socks_order_request.id,
	)

	team_instance_jersey_socks_order_request_3 = await db.run_sync(
		team_instance_jersey_socks_order_request_crud.get_sync,
		id=team_instance_jersey_socks_order_request.id,
	)

	assert team_instance_jersey_socks_order_request_3 is None
	assert team_instance_jersey_socks_order_request_2.id == team_instance_jersey_socks_order_request.id






