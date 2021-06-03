from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.instance.division import (
	division_instance_crud,
)

from main.schemas.data.team.instance.division import (
	DivisionInstanceSchemaCreate,
	DivisionInstanceSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest





@pytest.mark.asyncio
async def test_create_division_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	division_instance_in = DivisionInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	division_instance = await division_instance_crud.create(
		db=db,
		obj_in=division_instance_in,
	)

	assert division_instance.year_start == year_start
	assert division_instance.year_end == year_end



@pytest.mark.asyncio
async def test_create_sync_division_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	division_instance_in = DivisionInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	division_instance = await db.run_sync(
		division_instance_crud.create_sync,
		obj_in=division_instance_in,
	)

	assert division_instance.year_start == year_start
	assert division_instance.year_end == year_end



@pytest.mark.asyncio
async def test_get_division_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	division_instance_in = DivisionInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	division_instance = await division_instance_crud.create(
		db=db,
		obj_in=division_instance_in,
	)

	division_instance_2 = await division_instance_crud.get(
		db=db,
		id=division_instance.id,
	)

	assert division_instance_2
	assert jsonable_encoder(division_instance_2) == jsonable_encoder(division_instance)



@pytest.mark.asyncio
async def test_get_sync_division_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	division_instance_in = DivisionInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	division_instance = await db.run_sync(
		division_instance_crud.create_sync,
		obj_in=division_instance_in,
	)

	division_instance_2 = await db.run_sync(
		division_instance_crud.get_sync,
		id=division_instance.id,
	)

	assert division_instance_2
	assert jsonable_encoder(division_instance_2) == jsonable_encoder(division_instance)



@pytest.mark.asyncio
async def test_update_division_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	division_instance_in = DivisionInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	division_instance = await division_instance_crud.create(
		db=db,
		obj_in=division_instance_in,
	)

	new_year_start = 2022

	division_instance_in_update = DivisionInstanceSchemaUpdate(
		year_start=new_year_start,
	)

	division_instance_2 = await division_instance_crud.update(
		db=db,
		db_obj=division_instance,
		obj_in=division_instance_in_update,
	)

	assert division_instance_2
	assert division_instance_2.year_start
	assert division_instance_2.year_start == new_year_start



@pytest.mark.asyncio
async def test_update_sync_division_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	division_instance_in = DivisionInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	division_instance = await db.run_sync(
		division_instance_crud.create_sync,
		obj_in=division_instance_in,
	)

	new_year_start = 2022

	division_instance_in_update = DivisionInstanceSchemaUpdate(
		year_start=new_year_start,
	)

	division_instance_2 = await db.run_sync(
		division_instance_crud.update_sync,
		db_obj=division_instance,
		obj_in=division_instance_in_update,
	)

	assert division_instance_2
	assert division_instance_2.year_start
	assert division_instance_2.year_start == new_year_start




@pytest.mark.asyncio
async def test_delete_division_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	division_instance_in = DivisionInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	division_instance = await division_instance_crud.create(
		db=db,
		obj_in=division_instance_in,
	)

	division_instance_2 = await division_instance_crud.delete(
		db=db,
		id=division_instance.id,
	)

	division_instance_3 = await division_instance_crud.get(
		db=db,
		id=division_instance.id,
	)

	assert division_instance_3 is None
	assert division_instance_2.id == division_instance.id


@pytest.mark.asyncio
async def test_delete_sync_division_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	division_instance_in = DivisionInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	division_instance = await db.run_sync(
		division_instance_crud.create_sync,
		obj_in=division_instance_in,
	)

	division_instance_2 = await db.run_sync(
		division_instance_crud.delete_sync,
		id=division_instance.id,
	)

	division_instance_3 = await db.run_sync(
		division_instance_crud.get_sync,
		id=division_instance.id,
	)

	assert division_instance_3 is None
	assert division_instance_2.id == division_instance.id





