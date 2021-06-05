from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.instance.orders.jersey_socks import (
	team_instance_jersey_socks_order_crud,
)

from main.schemas.data.team.instance.orders.jersey_socks import (
	TeamInstanceJerseySocksOrderSchemaCreate,
	TeamInstanceJerseySocksOrderSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
	random_number,
)


import pytest





@pytest.mark.asyncio
async def test_create_team_instance_jersey_socks_order(
	db: AsyncSession,
) -> None:
	# --

	jersey_number = random_number(min_digits=1, max_digits=2)
	jersey_size = 'YXL'
	socks_size = '24in'

	team_instance_jersey_socks_order_in = TeamInstanceJerseySocksOrderSchemaCreate(
		jersey_number=jersey_number,
		jersey_size=jersey_size,
		socks_size=socks_size,
	)

	team_instance_jersey_socks_order = await team_instance_registration_jersey_sponsor_crud.create(
		db=db,
		obj_in=team_instance_jersey_socks_order_in,
	)

	assert team_instance_jersey_socks_order.jersey_number == jersey_number
	assert team_instance_jersey_socks_order.jersey_size == jersey_size




@pytest.mark.asyncio
async def test_create_sync_team_instance_jersey_socks_order(
	db: AsyncSession,
) -> None:
	# --

	jersey_number = random_number(min_digits=1, max_digits=2)
	jersey_size = 'YXL'
	socks_size = '24in'

	team_instance_jersey_socks_order_in = TeamInstanceJerseySocksOrderSchemaCreate(
		jersey_number=jersey_number,
		jersey_size=jersey_size,
		socks_size=socks_size,
	)

	team_instance_jersey_socks_order = await db.run_sync(
		team_instance_registration_jersey_sponsor_crud.create_sync,
		obj_in=team_instance_jersey_socks_order_in,
	)

	assert team_instance_jersey_socks_order.jersey_number == jersey_number
	assert team_instance_jersey_socks_order.jersey_size == jersey_size





@pytest.mark.asyncio
async def test_get_team_instance_jersey_socks_order(
	db: AsyncSession,
) -> None:
	# --

	jersey_number = random_number(min_digits=1, max_digits=2)
	jersey_size = 'YXL'
	socks_size = '24in'

	team_instance_jersey_socks_order_in = TeamInstanceJerseySocksOrderSchemaCreate(
		jersey_number=jersey_number,
		jersey_size=jersey_size,
		socks_size=socks_size,
	)

	team_instance_jersey_socks_order = await team_instance_registration_jersey_sponsor_crud.create(
		db=db,
		obj_in=team_instance_jersey_socks_order_in,
	)

	team_instance_jersey_socks_order_2 = await team_instance_registration_jersey_sponsor_crud.get(
		db=db,
		id=team_instance_jersey_socks_order.id,
	)

	assert team_instance_jersey_socks_order_2
	assert jsonable_encoder(team_instance_jersey_socks_order_2) == jsonable_encoder(team_instance_jersey_socks_order)



@pytest.mark.asyncio
async def test_get_sync_team_instance_jersey_socks_order(
	db: AsyncSession,
) -> None:
	# --

	jersey_number = random_number(min_digits=1, max_digits=2)
	jersey_size = 'YXL'
	socks_size = '24in'

	team_instance_jersey_socks_order_in = TeamInstanceJerseySocksOrderSchemaCreate(
		jersey_number=jersey_number,
		jersey_size=jersey_size,
		socks_size=socks_size,
	)

	team_instance_jersey_socks_order = await db.run_sync(
		team_instance_registration_jersey_sponsor_crud.create_sync,
		obj_in=team_instance_jersey_socks_order_in,
	)

	team_instance_jersey_socks_order_2 = await db.run_sync(
		team_instance_registration_jersey_sponsor_crud.get_sync,
		id=team_instance_jersey_socks_order.id,
	)

	assert team_instance_jersey_socks_order_2
	assert jsonable_encoder(team_instance_jersey_socks_order_2) == jsonable_encoder(team_instance_jersey_socks_order)




@pytest.mark.asyncio
async def test_update_team_instance_jersey_socks_order(
	db: AsyncSession,
) -> None:
	# --

	jersey_number = random_number(min_digits=1, max_digits=2)
	jersey_size = 'YXL'
	socks_size = '24in'

	team_instance_jersey_socks_order_in = TeamInstanceJerseySocksOrderSchemaCreate(
		jersey_number=jersey_number,
		jersey_size=jersey_size,
		socks_size=socks_size,
	)

	team_instance_jersey_socks_order = await team_instance_registration_jersey_sponsor_crud.create(
		db=db,
		obj_in=team_instance_jersey_socks_order_in,
	)

	new_jersey_number = random_number(min_digits=1, max_digits=2)

	while new_jersey_number == jersey_number:
		new_jersey_number = random_number(min_digits=1, max_digits=2)


	team_instance_jersey_socks_order_in_update = TeamInstanceJerseySocksOrderSchemaUpdate(
		jersey_number=new_jersey_number,
	)

	team_instance_jersey_socks_order_2 = await team_instance_registration_jersey_sponsor_crud.update(
		db=db,
		db_obj=team_instance_jersey_socks_order,
		obj_in=team_instance_jersey_socks_order_in_update,
	)

	assert team_instance_jersey_socks_order_2
	assert team_instance_jersey_socks_order_2.jersey_number
	assert team_instance_jersey_socks_order_2.jersey_number == new_jersey_number




@pytest.mark.asyncio
async def test_update_sync_team_instance_jersey_socks_order(
	db: AsyncSession,
) -> None:
	# --

	jersey_number = random_number(min_digits=1, max_digits=2)
	jersey_size = 'YXL'
	socks_size = '24in'

	team_instance_jersey_socks_order_in = TeamInstanceJerseySocksOrderSchemaCreate(
		jersey_number=jersey_number,
		jersey_size=jersey_size,
		socks_size=socks_size,
	)

	team_instance_jersey_socks_order = await db.run_sync(
		team_instance_registration_jersey_sponsor_crud.create_sync,
		obj_in=team_instance_jersey_socks_order_in,
	)


	new_jersey_number = random_number(min_digits=1, max_digits=2)

	while new_jersey_number == jersey_number:
		new_jersey_number = random_number(min_digits=1, max_digits=2)


	team_instance_jersey_socks_order_in_update = TeamInstanceJerseySocksOrderSchemaUpdate(
		jersey_number=new_jersey_number,
	)

	team_instance_jersey_socks_order_2 = await db.run_sync(
		team_instance_registration_jersey_sponsor_crud.update_sync,
		db_obj=team_instance_jersey_socks_order,
		obj_in=team_instance_jersey_socks_order_in_update,
	)

	assert team_instance_jersey_socks_order_2
	assert team_instance_jersey_socks_order_2.jersey_number
	assert team_instance_jersey_socks_order_2.jersey_number == new_jersey_number



@pytest.mark.asyncio
async def test_delete_team_instance_jersey_socks_order(
	db: AsyncSession,
) -> None:
	# --

	jersey_number = random_number(min_digits=1, max_digits=2)
	jersey_size = 'YXL'
	socks_size = '24in'

	team_instance_jersey_socks_order_in = TeamInstanceJerseySocksOrderSchemaCreate(
		jersey_number=jersey_number,
		jersey_size=jersey_size,
		socks_size=socks_size,
	)

	team_instance_jersey_socks_order = await team_instance_registration_jersey_sponsor_crud.create(
		db=db,
		obj_in=team_instance_jersey_socks_order_in,
	)

	team_instance_jersey_socks_order_2 = await team_instance_registration_jersey_sponsor_crud.delete(
		db=db,
		id=team_instance_jersey_socks_order.id,
	)

	team_instance_jersey_socks_order_3 = await team_instance_registration_jersey_sponsor_crud.get(
		db=db,
		id=team_instance_jersey_socks_order.id,
	)

	assert team_instance_jersey_socks_order_3 is None
	assert team_instance_jersey_socks_order_2.id == team_instance_jersey_socks_order.id



@pytest.mark.asyncio
async def test_delete_sync_team_instance_jersey_socks_order(
	db: AsyncSession,
) -> None:
	# --

	jersey_number = random_number(min_digits=1, max_digits=2)
	jersey_size = 'YXL'
	socks_size = '24in'

	team_instance_jersey_socks_order_in = TeamInstanceJerseySocksOrderSchemaCreate(
		jersey_number=jersey_number,
		jersey_size=jersey_size,
		socks_size=socks_size,
	)

	team_instance_jersey_socks_order = await db.run_sync(
		team_instance_registration_jersey_sponsor_crud.create_sync,
		obj_in=team_instance_jersey_socks_order_in,
	)

	team_instance_jersey_socks_order_2 = await db.run_sync(
		team_instance_registration_jersey_sponsor_crud.delete_sync,
		id=team_instance_jersey_socks_order.id,
	)

	team_instance_jersey_socks_order_3 = await db.run_sync(
		team_instance_registration_jersey_sponsor_crud.get_sync,
		id=team_instance_jersey_socks_order.id,
	)

	assert team_instance_jersey_socks_order_3 is None
	assert team_instance_jersey_socks_order_2.id == team_instance_jersey_socks_order.id






