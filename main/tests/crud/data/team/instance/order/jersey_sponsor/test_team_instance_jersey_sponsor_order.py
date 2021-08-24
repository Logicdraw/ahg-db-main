from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.instance.order.jersey_sponsor import (
	team_instance_jersey_sponsor_order_crud,
)

from main.schemas.data.team.instance.order.jersey_sponsor import (
	TeamInstanceJerseySponsorOrderSchemaCreate,
	TeamInstanceJerseySponsorOrderSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
	random_number,
)


import pytest





@pytest.mark.asyncio
async def test_create_team_instance_jersey_sponsor_order(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	amount = random_number()

	team_instance_jersey_sponsor_order_in = TeamInstanceJerseySponsorOrderSchemaCreate(
		name=name,
		amount=amount,
	)

	team_instance_jersey_sponsor_order = await team_instance_jersey_sponsor_order_crud.create(
		db=db,
		obj_in=team_instance_jersey_sponsor_order_in,
	)

	assert team_instance_jersey_sponsor_order.amount == amount
	assert team_instance_jersey_sponsor_order.jersey_size == jersey_size




@pytest.mark.asyncio
async def test_create_sync_team_instance_jersey_sponsor_order(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	amount = random_number()

	team_instance_jersey_sponsor_order_in = TeamInstanceJerseySponsorOrderSchemaCreate(
		name=name,
		amount=amount,
	)

	team_instance_jersey_sponsor_order = await db.run_sync(
		team_instance_jersey_sponsor_order_crud.create_sync,
		obj_in=team_instance_jersey_sponsor_order_in,
	)

	assert team_instance_jersey_sponsor_order.amount == amount
	assert team_instance_jersey_sponsor_order.jersey_size == jersey_size





@pytest.mark.asyncio
async def test_get_team_instance_jersey_sponsor_order(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	amount = random_number()

	team_instance_jersey_sponsor_order_in = TeamInstanceJerseySponsorOrderSchemaCreate(
		name=name,
		amount=amount,
	)

	team_instance_jersey_sponsor_order = await team_instance_jersey_sponsor_order_crud.create(
		db=db,
		obj_in=team_instance_jersey_sponsor_order_in,
	)

	team_instance_jersey_sponsor_order_2 = await team_instance_jersey_sponsor_order_crud.get(
		db=db,
		id=team_instance_jersey_sponsor_order.id,
	)

	assert team_instance_jersey_sponsor_order_2
	assert jsonable_encoder(team_instance_jersey_sponsor_order_2) == jsonable_encoder(team_instance_jersey_sponsor_order)



@pytest.mark.asyncio
async def test_get_sync_team_instance_jersey_sponsor_order(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	amount = random_number()

	team_instance_jersey_sponsor_order_in = TeamInstanceJerseySponsorOrderSchemaCreate(
		name=name,
		amount=amount,
	)

	team_instance_jersey_sponsor_order = await db.run_sync(
		team_instance_jersey_sponsor_order_crud.create_sync,
		obj_in=team_instance_jersey_sponsor_order_in,
	)

	team_instance_jersey_sponsor_order_2 = await db.run_sync(
		team_instance_jersey_sponsor_order_crud.get_sync,
		id=team_instance_jersey_sponsor_order.id,
	)

	assert team_instance_jersey_sponsor_order_2
	assert jsonable_encoder(team_instance_jersey_sponsor_order_2) == jsonable_encoder(team_instance_jersey_sponsor_order)




@pytest.mark.asyncio
async def test_update_team_instance_jersey_sponsor_order(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	amount = random_number()

	team_instance_jersey_sponsor_order_in = TeamInstanceJerseySponsorOrderSchemaCreate(
		name=name,
		amount=amount,
	)

	team_instance_jersey_sponsor_order = await team_instance_jersey_sponsor_order_crud.create(
		db=db,
		obj_in=team_instance_jersey_sponsor_order_in,
	)

	new_amount = random_number(min_digits=1, max_digits=2)

	while new_amount == amount:
		new_amount = random_number(min_digits=1, max_digits=2)


	team_instance_jersey_sponsor_order_in_update = TeamInstanceJerseySponsorOrderSchemaUpdate(
		amount=new_amount,
	)

	team_instance_jersey_sponsor_order_2 = await team_instance_jersey_sponsor_order_crud.update(
		db=db,
		db_obj=team_instance_jersey_sponsor_order,
		obj_in=team_instance_jersey_sponsor_order_in_update,
	)

	assert team_instance_jersey_sponsor_order_2
	assert team_instance_jersey_sponsor_order_2.amount
	assert team_instance_jersey_sponsor_order_2.amount == new_amount




@pytest.mark.asyncio
async def test_update_sync_team_instance_jersey_sponsor_order(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	amount = random_number()

	team_instance_jersey_sponsor_order_in = TeamInstanceJerseySponsorOrderSchemaCreate(
		name=name,
		amount=amount,
	)

	team_instance_jersey_sponsor_order = await db.run_sync(
		team_instance_jersey_sponsor_order_crud.create_sync,
		obj_in=team_instance_jersey_sponsor_order_in,
	)


	new_amount = random_number(min_digits=1, max_digits=2)

	while new_amount == amount:
		new_amount = random_number(min_digits=1, max_digits=2)


	team_instance_jersey_sponsor_order_in_update = TeamInstanceJerseySponsorOrderSchemaUpdate(
		amount=new_amount,
	)

	team_instance_jersey_sponsor_order_2 = await db.run_sync(
		team_instance_jersey_sponsor_order_crud.update_sync,
		db_obj=team_instance_jersey_sponsor_order,
		obj_in=team_instance_jersey_sponsor_order_in_update,
	)

	assert team_instance_jersey_sponsor_order_2
	assert team_instance_jersey_sponsor_order_2.amount
	assert team_instance_jersey_sponsor_order_2.amount == new_amount



@pytest.mark.asyncio
async def test_delete_team_instance_jersey_sponsor_order(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	amount = random_number()

	team_instance_jersey_sponsor_order_in = TeamInstanceJerseySponsorOrderSchemaCreate(
		name=name,
		amount=amount,
	)

	team_instance_jersey_sponsor_order = await team_instance_jersey_sponsor_order_crud.create(
		db=db,
		obj_in=team_instance_jersey_sponsor_order_in,
	)

	team_instance_jersey_sponsor_order_2 = await team_instance_jersey_sponsor_order_crud.delete(
		db=db,
		id=team_instance_jersey_sponsor_order.id,
	)

	team_instance_jersey_sponsor_order_3 = await team_instance_jersey_sponsor_order_crud.get(
		db=db,
		id=team_instance_jersey_sponsor_order.id,
	)

	assert team_instance_jersey_sponsor_order_3 is None
	assert team_instance_jersey_sponsor_order_2.id == team_instance_jersey_sponsor_order.id



@pytest.mark.asyncio
async def test_delete_sync_team_instance_jersey_sponsor_order(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	amount = random_number()

	team_instance_jersey_sponsor_order_in = TeamInstanceJerseySponsorOrderSchemaCreate(
		name=name,
		amount=amount,
	)

	team_instance_jersey_sponsor_order = await db.run_sync(
		team_instance_jersey_sponsor_order_crud.create_sync,
		obj_in=team_instance_jersey_sponsor_order_in,
	)

	team_instance_jersey_sponsor_order_2 = await db.run_sync(
		team_instance_jersey_sponsor_order_crud.delete_sync,
		id=team_instance_jersey_sponsor_order.id,
	)

	team_instance_jersey_sponsor_order_3 = await db.run_sync(
		team_instance_jersey_sponsor_order_crud.get_sync,
		id=team_instance_jersey_sponsor_order.id,
	)

	assert team_instance_jersey_sponsor_order_3 is None
	assert team_instance_jersey_sponsor_order_2.id == team_instance_jersey_sponsor_order.id






