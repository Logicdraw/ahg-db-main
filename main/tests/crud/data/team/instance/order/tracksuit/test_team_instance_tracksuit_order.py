from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.instance.order.tracksuit import (
	team_instance_tracksuit_order_crud,
)

from main.schemas.data.team.instance.order.tracksuit import (
	TeamInstanceTracksuitOrderSchemaCreate,
	TeamInstanceTracksuitOrderSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)



import pytest





@pytest.mark.asyncio
async def test_create_team_instance_tracksuit_order(
	db: AsyncSession,
) -> None:
	# --

	jacket_size = 'XXL'
	pants_size = 'XL'

	team_instance_tracksuit_order_in = TeamInstanceTracksuitOrderSchemaCreate(
		jacket_size=jacket_size,
		pants_size=pants_size,
	)

	team_instance_tracksuit_order = await team_instance_tracksuit_order_crud.create(
		db=db,
		obj_in=team_instance_tracksuit_order_in,
	)

	assert team_instance_tracksuit_order.jacket_size == jacket_size
	assert team_instance_tracksuit_order.pants_size == pants_size




@pytest.mark.asyncio
async def test_create_sync_team_instance_tracksuit_order(
	db: AsyncSession,
) -> None:
	# --

	jacket_size = 'XXL'
	pants_size = 'XL'

	team_instance_tracksuit_order_in = TeamInstanceTracksuitOrderSchemaCreate(
		jacket_size=jacket_size,
		pants_size=pants_size,
	)

	team_instance_tracksuit_order = await db.run_sync(
		team_instance_tracksuit_order_crud.create_sync,
		obj_in=team_instance_tracksuit_order_in,
	)

	assert team_instance_tracksuit_order.jacket_size == jacket_size
	assert team_instance_tracksuit_order.pants_size == pants_size



@pytest.mark.asyncio
async def test_get_team_instance_tracksuit_order(
	db: AsyncSession,
) -> None:
	# --

	jacket_size = 'XXL'
	pants_size = 'XL'

	team_instance_tracksuit_order_in = TeamInstanceTracksuitOrderSchemaCreate(
		jacket_size=jacket_size,
		pants_size=pants_size,
	)

	team_instance_tracksuit_order = await team_instance_tracksuit_order_crud.create(
		db=db,
		obj_in=team_instance_tracksuit_order_in,
	)

	team_instance_tracksuit_order_2 = await team_instance_tracksuit_order_crud.get(
		db=db,
		id=team_instance_tracksuit_order.id,
	)

	assert team_instance_tracksuit_order
	assert jsonable_encoder(team_instance_tracksuit_order_2) == jsonable_encoder(team_instance_tracksuit_order)



@pytest.mark.asyncio
async def test_get_sync_team_instance_tracksuit_order(
	db: AsyncSession,
) -> None:
	# --

	jacket_size = 'XXL'
	pants_size = 'XL'

	team_instance_tracksuit_order_in = TeamInstanceTracksuitOrderSchemaCreate(
		jacket_size=jacket_size,
		pants_size=pants_size,
	)

	team_instance_tracksuit_order = await db.run_sync(
		team_instance_tracksuit_order_crud.create_sync,
		obj_in=team_instance_tracksuit_order_in,
	)

	team_instance_tracksuit_order_2 = await db.run_sync(
		team_instance_tracksuit_order_crud.get_sync,
		id=team_instance_tracksuit_order.id,
	)

	assert team_instance_tracksuit_order
	assert jsonable_encoder(team_instance_tracksuit_order_2) == jsonable_encoder(team_instance_tracksuit_order)




@pytest.mark.asyncio
async def test_update_team_instance_tracksuit_order(
	db: AsyncSession,
) -> None:
	# --

	jacket_size = 'XXL'
	pants_size = 'XL'

	team_instance_tracksuit_order_in = TeamInstanceTracksuitOrderSchemaCreate(
		jacket_size=jacket_size,
		pants_size=pants_size,
	)

	team_instance_tracksuit_order = await team_instance_tracksuit_order_crud.create(
		db=db,
		obj_in=team_instance_tracksuit_order_in,
	)

	new_jacket_size = 'XL'

	team_instance_tracksuit_order_in_update = TeamInstanceTracksuitOrderSchemaUpdate(
		jacket_size=new_jacket_size,
	)

	team_instance_tracksuit_order_2 = await team_instance_tracksuit_order_crud.update(
		db=db,
		db_obj=team_instance_tracksuit_order,
		obj_in=team_instance_tracksuit_order_in_update,
	)

	assert team_instance_tracksuit_order_2
	assert team_instance_tracksuit_order_2.jacket_size
	assert team_instance_tracksuit_order_2.jacket_size == new_jacket_size




@pytest.mark.asyncio
async def test_update_sync_team_instance_tracksuit_order(
	db: AsyncSession,
) -> None:
	# --

	jacket_size = 'XXL'
	pants_size = 'XL'

	team_instance_tracksuit_order_in = TeamInstanceTracksuitOrderSchemaCreate(
		jacket_size=jacket_size,
		pants_size=pants_size,
	)

	team_instance_tracksuit_order = await db.run_sync(
		team_instance_tracksuit_order_crud.create_sync,
		obj_in=team_instance_tracksuit_order_in,
	)

	new_jacket_size = 'XL'

	team_instance_tracksuit_order_in_update = TeamInstanceTracksuitOrderSchemaUpdate(
		jacket_size=new_jacket_size,
	)

	team_instance_tracksuit_order_2 = await db.run_sync(
		team_instance_tracksuit_order_crud.update_sync,
		db_obj=team_instance_tracksuit_order,
		obj_in=team_instance_tracksuit_order_in_update,
	)

	assert team_instance_tracksuit_order_2
	assert team_instance_tracksuit_order_2.jacket_size
	assert team_instance_tracksuit_order_2.jacket_size == new_jacket_size



@pytest.mark.asyncio
async def test_delete_team_instance_tracksuit_order(
	db: AsyncSession,
) -> None:
	# --

	jacket_size = 'XXL'
	pants_size = 'XL'

	team_instance_tracksuit_order_in = TeamInstanceTracksuitOrderSchemaCreate(
		jacket_size=jacket_size,
		pants_size=pants_size,
	)

	team_instance_tracksuit_order = await team_instance_tracksuit_order_crud.create(
		db=db,
		obj_in=team_instance_tracksuit_order_in,
	)

	team_instance_tracksuit_order_2 = await team_instance_tracksuit_order_crud.delete(
		db=db,
		id=team_instance_tracksuit_order.id,
	)

	team_instance_tracksuit_order_3 = await team_instance_tracksuit_order_crud.get(
		db=db,
		id=team_instance_tracksuit_order.id,
	)

	assert team_instance_tracksuit_order_3 is None
	assert team_instance_tracksuit_order_2.id == team_instance_tracksuit_order.id



@pytest.mark.asyncio
async def test_delete_sync_team_instance_tracksuit_order(
	db: AsyncSession,
) -> None:
	# --

	jacket_size = 'XXL'
	pants_size = 'XL'

	team_instance_tracksuit_order_in = TeamInstanceTracksuitOrderSchemaCreate(
		jacket_size=jacket_size,
		pants_size=pants_size,
	)

	team_instance_tracksuit_order = await db.run_sync(
		team_instance_tracksuit_order_crud.create_sync,
		obj_in=team_instance_tracksuit_order_in,
	)


	team_instance_tracksuit_order_2 = await db.run_sync(
		team_instance_tracksuit_order_crud.delete_sync,
		id=team_instance_tracksuit_order.id,
	)

	team_instance_tracksuit_order_3 = await db.run_sync(
		team_instance_tracksuit_order_crud.get_sync,
		id=team_instance_tracksuit_order.id,
	)

	assert team_instance_tracksuit_order_3 is None
	assert team_instance_tracksuit_order_2.id == team_instance_tracksuit_order.id






