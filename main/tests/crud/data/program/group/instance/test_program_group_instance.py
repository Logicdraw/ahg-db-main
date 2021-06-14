from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.program.group.instance import (
	program_group_instance_crud,
)

from main.schemas.data.program.group.instance import (
	ProgramGroupInstanceSchemaCreate,
	ProgramGroupInstanceSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest





@pytest.mark.asyncio
async def test_create_program_group_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	program_group_instance_in = ProgramGroupInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	program_group_instance = await program_group_instance_crud.create(
		db=db,
		obj_in=program_group_instance_in,
	)

	assert program_group_instance.year_start == year_start
	assert program_group_instance.year_end == year_end



@pytest.mark.asyncio
async def test_create_sync_program_group_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	program_group_instance_in = ProgramGroupInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	program_group_instance = await db.run_sync(
		program_group_instance_crud.create_sync,
		obj_in=program_group_instance_in,
	)

	assert program_group_instance.year_start == year_start
	assert program_group_instance.year_end == year_end




@pytest.mark.asyncio
async def test_get_program_group_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	program_group_instance_in = ProgramGroupInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	program_group_instance = await program_group_instance_crud.create(
		db=db,
		obj_in=program_group_instance_in,
	)

	program_group_instance_2 = await program_group_instance_crud.get(
		db=db,
		id=program_group_instance.id,
	)

	assert program_group_instance_2
	assert jsonable_encoder(program_group_instance_2) == jsonable_encoder(program_group_instance)



@pytest.mark.asyncio
async def test_get_sync_program_group_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	program_group_instance_in = ProgramGroupInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	program_group_instance = await db.run_sync(
		program_group_instance_crud.create_sync,
		obj_in=program_group_instance_in,
	)

	program_group_instance_2 = await db.run_sync(
		program_group_instance_crud.get_sync,
		id=program_group_instance.id,
	)

	assert program_group_instance_2
	assert jsonable_encoder(program_group_instance_2) == jsonable_encoder(program_group_instance)




@pytest.mark.asyncio
async def test_update_program_group_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	program_group_instance_in = ProgramGroupInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	program_group_instance = await program_group_instance_crud.create(
		db=db,
		obj_in=program_group_instance_in,
	)

	new_year_start = 2020

	program_group_instance_in_update = ProgramGroupInstanceSchemaUpdate(
		year_start=new_year_start,
	)

	program_group_instance_2 = await program_group_instance_crud.update(
		db=db,
		db_obj=program_group_instance,
		obj_in=program_group_instance_in_update,
	)

	assert program_group_instance_2
	assert program_group_instance_2.year_start
	assert program_group_instance_2.year_start == new_year_start



@pytest.mark.asyncio
async def test_update_sync_program_group_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	program_group_instance_in = ProgramGroupInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	program_group_instance = await db.run_sync(
		program_group_instance_crud.create_sync,
		obj_in=program_group_instance_in,
	)

	new_year_start = 2020

	program_group_instance_in_update = ProgramGroupInstanceSchemaUpdate(
		year_start=new_year_start,
	)

	program_group_instance_2 = await db.run_sync(
		program_group_instance_crud.get_sync,
		id=program_group_instance.id,
	)


	assert program_group_instance_2
	assert jsonable_encoder(program_group_instance) == jsonable_encoder(program_group_instance_2)



@pytest.mark.asyncio
async def test_delete_program_group_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	program_group_instance_in = ProgramGroupInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	program_group_instance = await program_group_instance_crud.create(
		db=db,
		obj_in=program_group_instance_in,
	)

	program_group_instance_2 = await program_group_instance_crud.delete(
		db=db,
		id=program_group_instance.id,
	)

	program_group_instance_3 = await program_group_instance_crud.get(
		db=db,
		id=program_group_instance.id,
	)


	assert program_group_instance_3 is None
	assert program_group_instance_2.id == program_group_instance.id




@pytest.mark.asyncio
async def test_delete_sync_program_group_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021

	program_group_instance_in = ProgramGroupInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
	)

	program_group_instance = await db.run_sync(
		program_group_instance_crud.create_sync,
		obj_in=program_group_instance_in,
	)


	program_group_instance_2 = await db.run_sync(
		program_group_instance_crud.delete_sync,
		id=program_group_instance.id,
	)


	program_group_instance_3 = await db.run_sync(
		program_group_instance_crud.get_sync,
		id=program_group_instance.id,
	)


	assert program_group_instance_3 is None
	assert program_group_instance_2.id == program_group_instance.id





