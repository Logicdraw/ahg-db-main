from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.camp.group import (
	camp_group_crud,
)

from main.schemas.data.camp.group import (
	CampGroupSchemaCreate,
	CampGroupSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest





@pytest.mark.asyncio
async def test_create_camp_group(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()

	camp_group_in = CampGroupSchemaCreate(
		name=name,
	)

	camp_group = await camp_group_crud.create(
		db=db,
		obj_in=camp_group_in,
	)


	assert camp_group.name == name



@pytest.mark.asyncio
async def test_create_sync_camp_group(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()

	camp_group_in = CampGroupSchemaCreate(
		name=name,
	)

	camp_group = await db.run_sync(
		camp_group_crud.create_sync,
		obj_in=camp_group_in,
	)


	assert camp_group.name == name



@pytest.mark.asyncio
async def test_get_camp_group(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	camp_group_in = CampGroupSchemaCreate(
		name=name,
	)

	camp_group = await camp_group_crud.create(
		db=db,
		obj_in=camp_group_in,
	)

	camp_group_2 = await camp_group_crud.get(
		db=db,
		id=camp_group.id,
	)


	assert camp_group_2
	assert jsonable_encoder(camp_group) == jsonable_encoder(camp_group_2)



@pytest.mark.asyncio
async def test_get_sync_camp_group(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	camp_group_in = CampGroupSchemaCreate(
		name=name,
	)

	camp_group = await db.run_sync(
		camp_group_crud.create_sync,
		obj_in=camp_group_in,
	)

	camp_group_2 = await db.run_sync(
		camp_group_crud.get_sync,
		id=camp_group.id,
	)


	assert camp_group_2
	assert jsonable_encoder(camp_group) == jsonable_encoder(camp_group_2)



@pytest.mark.asyncio
async def test_update_camp_group(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	camp_group_in = CampGroupSchemaCreate(
		name=name,
	)

	camp_group = await camp_group_crud.create(
		db=db,
		obj_in=camp_group_in,
	)

	new_name = random_lower_string()

	camp_group_in_update = CampGroupSchemaUpdate(
		name=new_name,
	)

	camp_group_2 = await camp_group_crud.update(
		db=db,
		db_obj=camp_group,
		obj_in=camp_group_in_update,
	)


	assert camp_group_2
	assert camp_group_2.name
	assert camp_group_2.name == new_name



@pytest.mark.asyncio
async def test_update_sync_camp_group(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	camp_group_in = CampGroupSchemaCreate(
		name=name,
	)

	camp_group = await db.run_sync(
		camp_group_crud.create_sync,
		obj_in=camp_group_in,
	)

	new_name = random_lower_string()

	camp_group_in_update = CampGroupSchemaUpdate(
		name=new_name,
	)

	camp_group_2 = await db.run_sync(
		camp_group_crud.update_sync,
		db_obj=camp_group,
		obj_in=camp_group_in_update,
	)


	assert camp_group_2
	assert camp_group_2.name
	assert camp_group_2.name == new_name



@pytest.mark.asyncio
async def test_delete_camp_group(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	camp_group_in = CampGroupSchemaCreate(
		name=name,
	)

	camp_group = await camp_group_crud.create(
		db=db,
		obj_in=camp_group_in,
	)

	camp_group_2 = await camp_group_crud.delete(
		db=db,
		id=camp_group.id,
	)

	camp_group_3 = await camp_group_crud.get(
		db=db,
		id=camp_group.id,
	)

	assert camp_group_3 is None
	assert camp_group_2.id == camp_group.id



@pytest.mark.asyncio
async def test_delete_sync_camp_group(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	camp_group_in = CampGroupSchemaCreate(
		name=name,
	)

	camp_group = await db.run_sync(
		camp_group_crud.create_sync,
		obj_in=camp_group_in,
	)

	camp_group_2 = await db.run_sync(
		camp_group_crud.delete_sync,
		id=camp_group.id,
	)

	camp_group_3 = await db.run_sync(
		camp_group_crud.get_sync,
		id=camp_group.id,
	)

	assert camp_group_3 is None
	assert camp_group_2.id == camp_group.id





