from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.instance.order.jersey_socks.group_sheet import (
	team_instance_jersey_socks_order_group_sheet_crud,
)

from main.schemas.data.team.instance.order.jersey_socks.group_sheet import (
	TeamInstanceJerseySocksOrderGroupSheetSchemaCreate,
	TeamInstanceJerseySocksOrderGroupSheetSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
	random_number,
)


import uuid as _uuid


import pytest





@pytest.mark.asyncio
async def test_create_team_instance_jersey_socks_order_group_sheet(
	db: AsyncSession,
) -> None:
	# --

	uuid = _uuid.hex()

	team_instance_jersey_socks_order_group_sheet_in = TeamInstanceJerseySocksOrderGroupSheetSchemaCreate(
		uuid=uuid,
	)

	team_instance_jersey_socks_order_group_sheet = await team_instance_jersey_socks_order_group_sheet_crud.create(
		db=db,
		obj_in=team_instance_jersey_socks_order_group_sheet_in,
	)

	assert team_instance_jersey_socks_order_group_sheet.uuid == uuid




@pytest.mark.asyncio
async def test_create_sync_team_instance_jersey_socks_order_group_sheet(
	db: AsyncSession,
) -> None:
	# --

	uuid = _uuid.hex()

	team_instance_jersey_socks_order_group_sheet_in = TeamInstanceJerseySocksOrderGroupSheetSchemaCreate(
		uuid=uuid,
	)

	team_instance_jersey_socks_order_group_sheet = await db.run_sync(
		team_instance_jersey_socks_order_group_sheet_crud.create_sync,
		obj_in=team_instance_jersey_socks_order_group_sheet_in,
	)

	assert team_instance_jersey_socks_order_group_sheet.uuid == uuid




@pytest.mark.asyncio
async def test_get_team_instance_jersey_socks_order_group_sheet(
	db: AsyncSession,
) -> None:
	# --

	uuid = _uuid.hex()

	team_instance_jersey_socks_order_group_sheet_in = TeamInstanceJerseySocksOrderGroupSheetSchemaCreate(
		uuid=uuid,
	)

	team_instance_jersey_socks_order_group_sheet = await team_instance_jersey_socks_order_group_sheet_crud.create(
		db=db,
		obj_in=team_instance_jersey_socks_order_group_sheet_in,
	)

	team_instance_jersey_socks_order_group_sheet_2 = await team_instance_jersey_socks_order_group_sheet_crud.get(
		db=db,
		id=team_instance_jersey_socks_order_group_sheet.id,
	)

	assert team_instance_jersey_socks_order_group_sheet_2
	assert jsonable_encoder(team_instance_jersey_socks_order_group_sheet_2) == jsonable_encoder(team_instance_jersey_socks_order_group_sheet)



@pytest.mark.asyncio
async def test_get_sync_team_instance_jersey_socks_order_group_sheet(
	db: AsyncSession,
) -> None:
	# --

	uuid = _uuid.hex()

	team_instance_jersey_socks_order_group_sheet_in = TeamInstanceJerseySocksOrderGroupSheetSchemaCreate(
		uuid=uuid,
	)

	team_instance_jersey_socks_order_group_sheet = await db.run_sync(
		team_instance_jersey_socks_order_group_sheet_crud.create_sync,
		obj_in=team_instance_jersey_socks_order_group_sheet_in,
	)

	team_instance_jersey_socks_order_group_sheet_2 = await db.run_sync(
		team_instance_jersey_socks_order_group_sheet_crud.get_sync,
		id=team_instance_jersey_socks_order_group_sheet.id,
	)

	assert team_instance_jersey_socks_order_group_sheet_2
	assert jsonable_encoder(team_instance_jersey_socks_order_group_sheet_2) == jsonable_encoder(team_instance_jersey_socks_order_group_sheet)




@pytest.mark.asyncio
async def test_update_team_instance_jersey_socks_order_group_sheet(
	db: AsyncSession,
) -> None:
	# --

	uuid = _uuid.hex()

	team_instance_jersey_socks_order_group_sheet_in = TeamInstanceJerseySocksOrderGroupSheetSchemaCreate(
		uuid=uuid,
	)

	team_instance_jersey_socks_order_group_sheet = await team_instance_jersey_socks_order_group_sheet_crud.create(
		db=db,
		obj_in=team_instance_jersey_socks_order_group_sheet_in,
	)

	new_uuid = _uuid.hex()


	team_instance_jersey_socks_order_group_sheet_in_update = TeamInstanceJerseySocksOrderGroupSheetSchemaUpdate(
		uuid=new_uuid,
	)

	team_instance_jersey_socks_order_group_sheet_2 = await team_instance_jersey_socks_order_group_sheet_crud.update(
		db=db,
		db_obj=team_instance_jersey_socks_order_group_sheet,
		obj_in=team_instance_jersey_socks_order_group_sheet_in_update,
	)

	assert team_instance_jersey_socks_order_group_sheet_2
	assert team_instance_jersey_socks_order_group_sheet_2.uuid
	assert team_instance_jersey_socks_order_group_sheet_2.uuid == new_uuid




@pytest.mark.asyncio
async def test_update_sync_team_instance_jersey_socks_order_group_sheet(
	db: AsyncSession,
) -> None:
	# --

	uuid = _uuid.hex()

	team_instance_jersey_socks_order_group_sheet_in = TeamInstanceJerseySocksOrderGroupSheetSchemaCreate(
		uuid=uuid,
	)

	team_instance_jersey_socks_order_group_sheet = await db.run_sync(
		team_instance_jersey_socks_order_group_sheet_crud.create_sync,
		obj_in=team_instance_jersey_socks_order_group_sheet_in,
	)


	new_uuid = _uuid.hex()


	team_instance_jersey_socks_order_group_sheet_in_update = TeamInstanceJerseySocksOrderGroupSheetSchemaUpdate(
		uuid=new_uuid,
	)

	team_instance_jersey_socks_order_group_sheet_2 = await db.run_sync(
		team_instance_jersey_socks_order_group_sheet_crud.update_sync,
		db_obj=team_instance_jersey_socks_order_group_sheet,
		obj_in=team_instance_jersey_socks_order_group_sheet_in_update,
	)

	assert team_instance_jersey_socks_order_group_sheet_2
	assert team_instance_jersey_socks_order_group_sheet_2.uuid
	assert team_instance_jersey_socks_order_group_sheet_2.uuid == new_uuid



@pytest.mark.asyncio
async def test_delete_team_instance_jersey_socks_order_group_sheet(
	db: AsyncSession,
) -> None:
	# --

	uuid = _uuid.hex()

	team_instance_jersey_socks_order_group_sheet_in = TeamInstanceJerseySocksOrderGroupSheetSchemaCreate(
		uuid=uuid,
	)

	team_instance_jersey_socks_order_group_sheet = await team_instance_jersey_socks_order_group_sheet_crud.create(
		db=db,
		obj_in=team_instance_jersey_socks_order_group_sheet_in,
	)

	team_instance_jersey_socks_order_group_sheet_2 = await team_instance_jersey_socks_order_group_sheet_crud.delete(
		db=db,
		id=team_instance_jersey_socks_order_group_sheet.id,
	)

	team_instance_jersey_socks_order_group_sheet_3 = await team_instance_jersey_socks_order_group_sheet_crud.get(
		db=db,
		id=team_instance_jersey_socks_order_group_sheet.id,
	)

	assert team_instance_jersey_socks_order_group_sheet_3 is None
	assert team_instance_jersey_socks_order_group_sheet_2.id == team_instance_jersey_socks_order_group_sheet.id



@pytest.mark.asyncio
async def test_delete_sync_team_instance_jersey_socks_order_group_sheet(
	db: AsyncSession,
) -> None:
	# --

	uuid = _uuid.hex()

	team_instance_jersey_socks_order_group_sheet_in = TeamInstanceJerseySocksOrderGroupSheetSchemaCreate(
		uuid=uuid,
	)

	team_instance_jersey_socks_order_group_sheet = await db.run_sync(
		team_instance_jersey_socks_order_group_sheet_crud.create_sync,
		obj_in=team_instance_jersey_socks_order_group_sheet_in,
	)

	team_instance_jersey_socks_order_group_sheet_2 = await db.run_sync(
		team_instance_jersey_socks_order_group_sheet_crud.delete_sync,
		id=team_instance_jersey_socks_order_group_sheet.id,
	)

	team_instance_jersey_socks_order_group_sheet_3 = await db.run_sync(
		team_instance_jersey_socks_order_group_sheet_crud.get_sync,
		id=team_instance_jersey_socks_order_group_sheet.id,
	)

	assert team_instance_jersey_socks_order_group_sheet_3 is None
	assert team_instance_jersey_socks_order_group_sheet_2.id == team_instance_jersey_socks_order_group_sheet.id






