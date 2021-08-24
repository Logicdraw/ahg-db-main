from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.instance.order.jersey_socks.update import (
	team_instance_jersey_socks_order_update_crud,
)

from main.schemas.data.team.instance.order.jersey_socks.update import (
	TeamInstanceJerseySocksOrderUpdateSchemaCreate,
	TeamInstanceJerseySocksOrderUpdateSchemaUpdate,
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
async def test_create_team_instance_jersey_socks_order_update(
	db: AsyncSession,
) -> None:
	# --

	new_player_full_name = random_lower_string()
	new_jersey_number = random_number(min_digits=1, max_digits=2)
	new_jersey_size = 'YXL'
	new_socks_size = '24in'

	team_instance_jersey_socks_order_update_in = TeamInstanceJerseySocksOrderUpdateSchemaCreate(
		new_player_full_name=new_player_full_name,
		new_jersey_number=new_jersey_number,
		new_jersey_size=new_jersey_size,
		new_socks_size=new_socks_size,
	)

	team_instance_jersey_socks_order_update = await team_instance_jersey_socks_order_update_crud.create(
		db=db,
		obj_in=team_instance_jersey_socks_order_update_in,
	)

	assert team_instance_jersey_socks_order_update.new_player_full_name == new_player_full_name




@pytest.mark.asyncio
async def test_create_sync_team_instance_jersey_socks_order_update(
	db: AsyncSession,
) -> None:
	# --

	new_player_full_name = random_lower_string()
	new_jersey_number = random_number(min_digits=1, max_digits=2)
	new_jersey_size = 'YXL'
	new_socks_size = '24in'

	team_instance_jersey_socks_order_update_in = TeamInstanceJerseySocksOrderUpdateSchemaCreate(
		new_player_full_name=new_player_full_name,
		new_jersey_number=new_jersey_number,
		new_jersey_size=new_jersey_size,
		new_socks_size=new_socks_size,
	)

	team_instance_jersey_socks_order_update = await db.run_sync(
		team_instance_jersey_socks_order_update_crud.create_sync,
		obj_in=team_instance_jersey_socks_order_update_in,
	)

	assert team_instance_jersey_socks_order_update.new_player_full_name == new_player_full_name




@pytest.mark.asyncio
async def test_get_team_instance_jersey_socks_order_update(
	db: AsyncSession,
) -> None:
	# --

	new_player_full_name = random_lower_string()
	new_jersey_number = random_number(min_digits=1, max_digits=2)
	new_jersey_size = 'YXL'
	new_socks_size = '24in'

	team_instance_jersey_socks_order_update_in = TeamInstanceJerseySocksOrderUpdateSchemaCreate(
		new_player_full_name=new_player_full_name,
		new_jersey_number=new_jersey_number,
		new_jersey_size=new_jersey_size,
		new_socks_size=new_socks_size,
	)

	team_instance_jersey_socks_order_update = await team_instance_jersey_socks_order_update_crud.create(
		db=db,
		obj_in=team_instance_jersey_socks_order_update_in,
	)

	team_instance_jersey_socks_order_update_2 = await team_instance_jersey_socks_order_update_crud.get(
		db=db,
		id=team_instance_jersey_socks_order_update.id,
	)

	assert team_instance_jersey_socks_order_update_2
	assert jsonable_encoder(team_instance_jersey_socks_order_update_2) == jsonable_encoder(team_instance_jersey_socks_order_update)



@pytest.mark.asyncio
async def test_get_sync_team_instance_jersey_socks_order_update(
	db: AsyncSession,
) -> None:
	# --

	new_player_full_name = random_lower_string()
	new_jersey_number = random_number(min_digits=1, max_digits=2)
	new_jersey_size = 'YXL'
	new_socks_size = '24in'

	team_instance_jersey_socks_order_update_in = TeamInstanceJerseySocksOrderUpdateSchemaCreate(
		new_player_full_name=new_player_full_name,
		new_jersey_number=new_jersey_number,
		new_jersey_size=new_jersey_size,
		new_socks_size=new_socks_size,
	)

	team_instance_jersey_socks_order_update = await db.run_sync(
		team_instance_jersey_socks_order_update_crud.create_sync,
		obj_in=team_instance_jersey_socks_order_update_in,
	)

	team_instance_jersey_socks_order_update_2 = await db.run_sync(
		team_instance_jersey_socks_order_update_crud.get_sync,
		id=team_instance_jersey_socks_order_update.id,
	)

	assert team_instance_jersey_socks_order_update_2
	assert jsonable_encoder(team_instance_jersey_socks_order_update_2) == jsonable_encoder(team_instance_jersey_socks_order_update)




@pytest.mark.asyncio
async def test_update_team_instance_jersey_socks_order_update(
	db: AsyncSession,
) -> None:
	# --

	new_player_full_name = random_lower_string()
	new_jersey_number = random_number(min_digits=1, max_digits=2)
	new_jersey_size = 'YXL'
	new_socks_size = '24in'

	team_instance_jersey_socks_order_update_in = TeamInstanceJerseySocksOrderUpdateSchemaCreate(
		new_player_full_name=new_player_full_name,
		new_jersey_number=new_jersey_number,
		new_jersey_size=new_jersey_size,
		new_socks_size=new_socks_size,
	)

	team_instance_jersey_socks_order_update = await team_instance_jersey_socks_order_update_crud.create(
		db=db,
		obj_in=team_instance_jersey_socks_order_update_in,
	)

	new_new_player_full_name = random_lower_string()

	team_instance_jersey_socks_order_update_in_update = TeamInstanceJerseySocksOrderUpdateSchemaUpdate(
		new_player_full_name=new_new_player_full_name,
	)

	team_instance_jersey_socks_order_update_2 = await team_instance_jersey_socks_order_update_crud.update(
		db=db,
		db_obj=team_instance_jersey_socks_order_update,
		obj_in=team_instance_jersey_socks_order_update_in_update,
	)

	assert team_instance_jersey_socks_order_update_2
	assert team_instance_jersey_socks_order_update_2.new_player_full_name == new_new_player_full_name




@pytest.mark.asyncio
async def test_update_sync_team_instance_jersey_socks_order_update(
	db: AsyncSession,
) -> None:
	# --

	new_player_full_name = random_lower_string()
	new_jersey_number = random_number(min_digits=1, max_digits=2)
	new_jersey_size = 'YXL'
	new_socks_size = '24in'

	team_instance_jersey_socks_order_update_in = TeamInstanceJerseySocksOrderUpdateSchemaCreate(
		new_player_full_name=new_player_full_name,
		new_jersey_number=new_jersey_number,
		new_jersey_size=new_jersey_size,
		new_socks_size=new_socks_size,
	)

	team_instance_jersey_socks_order_update = await db.run_sync(
		team_instance_jersey_socks_order_update_crud.create_sync,
		obj_in=team_instance_jersey_socks_order_update_in,
	)


	new_new_player_full_name = random_lower_string()

	team_instance_jersey_socks_order_update_in_update = TeamInstanceJerseySocksOrderUpdateSchemaUpdate(
		new_player_full_name=new_new_player_full_name,
	)

	team_instance_jersey_socks_order_update_2 = await db.run_sync(
		team_instance_jersey_socks_order_update_crud.update_sync,
		db_obj=team_instance_jersey_socks_order_update,
		obj_in=team_instance_jersey_socks_order_update_in_update,
	)

	assert team_instance_jersey_socks_order_update_2
	assert team_instance_jersey_socks_order_update_2.new_player_full_name == new_new_player_full_name



@pytest.mark.asyncio
async def test_delete_team_instance_jersey_socks_order_update(
	db: AsyncSession,
) -> None:
	# --

	new_player_full_name = random_lower_string()
	new_jersey_number = random_number(min_digits=1, max_digits=2)
	new_jersey_size = 'YXL'
	new_socks_size = '24in'

	team_instance_jersey_socks_order_update_in = TeamInstanceJerseySocksOrderUpdateSchemaCreate(
		new_player_full_name=new_player_full_name,
		new_jersey_number=new_jersey_number,
		new_jersey_size=new_jersey_size,
		new_socks_size=new_socks_size,
	)

	team_instance_jersey_socks_order_update = await team_instance_jersey_socks_order_update_crud.create(
		db=db,
		obj_in=team_instance_jersey_socks_order_update_in,
	)

	team_instance_jersey_socks_order_update_2 = await team_instance_jersey_socks_order_update_crud.delete(
		db=db,
		id=team_instance_jersey_socks_order_update.id,
	)

	team_instance_jersey_socks_order_update_3 = await team_instance_jersey_socks_order_update_crud.get(
		db=db,
		id=team_instance_jersey_socks_order_update.id,
	)

	assert team_instance_jersey_socks_order_update_3 is None
	assert team_instance_jersey_socks_order_update_2.id == team_instance_jersey_socks_order_update.id



@pytest.mark.asyncio
async def test_delete_sync_team_instance_jersey_socks_order_update(
	db: AsyncSession,
) -> None:
	# --

	new_player_full_name = random_lower_string()
	new_jersey_number = random_number(min_digits=1, max_digits=2)
	new_jersey_size = 'YXL'
	new_socks_size = '24in'

	team_instance_jersey_socks_order_update_in = TeamInstanceJerseySocksOrderUpdateSchemaCreate(
		new_player_full_name=new_player_full_name,
		new_jersey_number=new_jersey_number,
		new_jersey_size=new_jersey_size,
		new_socks_size=new_socks_size,
	)

	team_instance_jersey_socks_order_update = await db.run_sync(
		team_instance_jersey_socks_order_update_crud.create_sync,
		obj_in=team_instance_jersey_socks_order_update_in,
	)

	team_instance_jersey_socks_order_update_2 = await db.run_sync(
		team_instance_jersey_socks_order_update_crud.delete_sync,
		id=team_instance_jersey_socks_order_update.id,
	)

	team_instance_jersey_socks_order_update_3 = await db.run_sync(
		team_instance_jersey_socks_order_update_crud.get_sync,
		id=team_instance_jersey_socks_order_update.id,
	)

	assert team_instance_jersey_socks_order_update_3 is None
	assert team_instance_jersey_socks_order_update_2.id == team_instance_jersey_socks_order_update.id






