from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.camp.group.instance import (
	camp_group_instance_crud,
)

from main.schemas.data.camp.group.instance import (
	CampGroupInstanceSchemaCreate,
	CampGroupInstanceSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest




@pytest.mark.asyncio
async def test_create_camp_group_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	camp_group_instance_in = CampGroupInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	camp_group_instance = await camp_group_instance_crud.create(
		db=db,
		obj_in=camp_group_instance_in,
	)

	assert camp_group_instance.year_start == year_start
	assert camp_group_instance.year_end == year_end



@pytest.mark.asyncio
async def test_create_sync_camp_group_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	camp_group_instance_in = CampGroupInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	camp_group_instance = await db.run_sync(
		camp_group_instance_crud.create_sync,
		obj_in=camp_group_instance_in,
	)

	assert camp_group_instance.year_start == year_start
	assert camp_group_instance.year_end == year_end




@pytest.mark.asyncio
async def test_get_camp_group_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	camp_group_instance_in = CampGroupInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	camp_group_instance = await camp_group_instance_crud.create(
		db=db,
		obj_in=camp_group_instance_in,
	)

	camp_group_instance_2 = await camp_group_instance_crud.get(
		db=db,
		id=camp_group_instance.id,
	)

	assert camp_group_instance_2
	assert jsonable_encoder(camp_group_instance_2) == jsonable_encoder(camp_group_instance)



@pytest.mark.asyncio
async def test_get_sync_camp_group_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	camp_group_instance_in = CampGroupInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	camp_group_instance = await db.run_sync(
		camp_group_instance_crud.create_sync,
		obj_in=camp_group_instance_in,
	)

	camp_group_instance_2 = await db.run_sync(
		camp_group_instance_crud.get_sync,
		id=camp_group_instance.id,
	)

	assert camp_group_instance_2
	assert jsonable_encoder(camp_group_instance_2) == jsonable_encoder(camp_group_instance)




@pytest.mark.asyncio
async def test_update_camp_group_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	camp_group_instance_in = CampGroupInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	camp_group_instance = await camp_group_instance_crud.create(
		db=db,
		obj_in=camp_group_instance_in,
	)

	new_year_start = 2020

	camp_group_instance_in_update = CampGroupInstanceSchemaUpdate(
		year_start=new_year_start,
	)

	camp_group_instance_2 = await camp_group_instance_crud.update(
		db=db,
		db_obj=camp_group_instance,
		obj_in=camp_group_instance_in_update,
	)

	assert camp_group_instance_2
	assert camp_group_instance_2.year_start
	assert camp_group_instance_2.year_start == new_year_start



@pytest.mark.asyncio
async def test_update_sync_camp_group_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	camp_group_instance_in = CampGroupInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	camp_group_instance = await db.run_sync(
		camp_group_instance_crud.create_sync,
		obj_in=camp_group_instance_in,
	)

	new_year_start = 2020

	camp_group_instance_in_update = CampGroupInstanceSchemaUpdate(
		year_start=new_year_start,
	)

	camp_group_instance_2 = await db.run_sync(
		camp_group_instance.get_sync,
		id=camp_group_instance.id,
	)


	assert camp_group_instance_2
	assert jsonable_encoder(camp_group_instance) == jsonable_encoder(camp_group_instance_2)



@pytest.mark.asyncio
async def test_delete_camp_group_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	camp_group_instance_in = CampGroupInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	camp_group_instance = await camp_group_instance_crud.create(
		db=db,
		obj_in=camp_group_instance_in,
	)

	camp_group_instance_2 = await camp_group_instance_crud.delete(
		db=db,
		id=camp_group_instance.id,
	)

	camp_group_instance_3 = await camp_group_instance_crud.get(
		db=db,
		id=camp_group_instance.id,
	)


	assert camp_group_instance_3 is None
	assert camp_group_instance_2.id == camp_group_instance.id




@pytest.mark.asyncio
async def test_delete_sync_camp_group_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	camp_group_instance_in = CampGroupInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	camp_group_instance = await db.run_sync(
		camp_group_instance_crud.create_sync,
		obj_in=camp_group_instance_in,
	)


	camp_group_instance_2 = await db.run_sync(
		camp_group_instance_crud.delete_sync,
		id=camp_group_instance.id,
	)


	camp_group_instance_3 = await db.run_sync(
		camp_group_instance_crud.get_sync,
		id=camp_group_instance.id,
	)


	assert camp_group_instance_3 is None
	assert camp_group_instance_2.id == camp_group_instance.id





