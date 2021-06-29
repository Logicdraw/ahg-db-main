from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.program.instance import (
	program_instance_crud,
)

from main.schemas.data.program.instance import (
	ProgramInstanceSchemaCreate,
	ProgramInstanceSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
	random_number,
)


import pytest





@pytest.mark.asyncio
async def test_create_program_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021
	spng_name_snake = random_lower_string()
	spng_shared_question_id = random_number()

	program_instance_in = ProgramInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		spng_name_snake=spng_name_snake,
		spng_shared_question_id=spng_shared_question_id,
	)

	program_instance = await program_instance_crud.create(
		db=db,
		obj_in=program_instance_in,
	)

	assert program_instance.year_start == year_start
	assert program_instance.spng_name_snake == spng_name_snake



@pytest.mark.asyncio
async def test_create_sync_program_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021
	spng_name_snake = random_lower_string()
	spng_shared_question_id = random_number()

	program_instance_in = ProgramInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		spng_name_snake=spng_name_snake,
		spng_shared_question_id=spng_shared_question_id,
	)

	program_instance = await db.run_sync(
		program_instance_crud.create_sync,
		obj_in=program_instance_in,
	)

	assert program_instance.year_start == year_start
	assert program_instance.spng_name_snake == spng_name_snake



@pytest.mark.asyncio
async def test_get_program_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021
	spng_name_snake = random_lower_string()
	spng_shared_question_id = random_number()

	program_instance_in = ProgramInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		spng_name_snake=spng_name_snake,
		spng_shared_question_id=spng_shared_question_id,
	)

	program_instance = await program_instance_crud.create(
		db=db,
		obj_in=program_instance_in,
	)

	program_instance_2 = await program_instance_crud.get(
		db=db,
		id=program_instance.id,
	)

	assert program_instance_2
	assert jsonable_encoder(program_instance) == jsonable_encoder(program_instance_2)



@pytest.mark.asyncio
async def test_get_sync_program_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021
	spng_name_snake = random_lower_string()
	spng_shared_question_id = random_number()

	program_instance_in = ProgramInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		spng_name_snake=spng_name_snake,
		spng_shared_question_id=spng_shared_question_id,
	)

	program_instance = await db.run_sync(
		program_instance_crud.create_sync,
		obj_in=program_instance_in,
	)

	program_instance_2 = await db.run_sync(
		program_instance_crud.get_sync,
		id=program_instance.id,
	)

	assert program_instance_2
	assert jsonable_encoder(program_instance) == jsonable_encoder(program_instance_2)





@pytest.mark.asyncio
async def test_update_program_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021
	spng_name_snake = random_lower_string()
	spng_shared_question_id = random_number()

	program_instance_in = ProgramInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		spng_name_snake=spng_name_snake,
		spng_shared_question_id=spng_shared_question_id,
	)

	program_instance = await program_instance_crud.create(
		db=db,
		obj_in=program_instance_in,
	)

	new_spng_name_snake = random_lower_string()

	while spng_name_snake == new_spng_name_snake:
		new_spng_name_snake = random_lower_string()

	program_instance_in_update = ProgramInstanceSchemaUpdate(
		spng_name_snake=new_spng_name_snake,
	)

	program_instance_2 = await program_instance_crud.update(
		db=db,
		db_obj=program_instance,
		obj_in=program_instance_in_update,
	)


	assert program_instance_2
	assert program_instance_2.spng_name_snake
	assert program_instance_2.spng_name_snake == new_spng_name_snake




@pytest.mark.asyncio
async def test_update_sync_program_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021
	spng_name_snake = random_lower_string()
	spng_shared_question_id = random_number()

	program_instance_in = ProgramInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		spng_name_snake=spng_name_snake,
		spng_shared_question_id=spng_shared_question_id,
	)

	program_instance = await db.run_sync(
		program_instance_crud.create_sync,
		obj_in=program_instance_in,
	)

	new_spng_name_snake = random_lower_string()

	while spng_name_snake == new_spng_name_snake:
		new_spng_name_snake = random_lower_string()

	program_instance_in_update = ProgramInstanceSchemaUpdate(
		spng_name_snake=new_spng_name_snake,
	)

	program_instance_2 = await db.run_sync(
		program_instance_crud.update_sync,
		db_obj=program_instance,
		obj_in=program_instance_in_update,
	)


	assert program_instance_2
	assert program_instance_2.spng_name_snake
	assert program_instance_2.spng_name_snake == new_spng_name_snake



@pytest.mark.asyncio
async def test_delete_program_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021
	spng_name_snake = random_lower_string()
	spng_shared_question_id = random_number()

	program_instance_in = ProgramInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		spng_name_snake=spng_name_snake,
		spng_shared_question_id=spng_shared_question_id,
	)

	program_instance = await program_instance_crud.create(
		db=db,
		obj_in=program_instance_in,
	)


	program_instance_2 = await program_instance_crud.delete(
		db=db,
		id=program_instance.id,
	)


	program_instance_3 = await program_instance_crud.get(
		db=db,
		id=program_instance.id,
	)


	assert program_instance_3 is None
	assert program_instance_2.id == program_instance.id



@pytest.mark.asyncio
async def test_delete_sync_program_instance(
	db: AsyncSession,
) -> None:
	# --

	year_start = 2021
	year_end = 2021
	spng_name_snake = random_lower_string()
	spng_shared_question_id = random_number()

	program_instance_in = ProgramInstanceSchemaCreate(
		year_start=year_start,
		year_end=year_end,
		spng_name_snake=spng_name_snake,
		spng_shared_question_id=spng_shared_question_id,
	)

	program_instance = await db.run_sync(
		program_instance_crud.create_sync,
		obj_in=program_instance_in,
	)


	program_instance_2 = await db.run_sync(
		program_instance_crud.delete_sync,
		id=program_instance.id,
	)


	program_instance_3 = await db.run_sync(
		program_instance_crud.get_sync,
		id=program_instance.id,
	)


	assert program_instance_3 is None
	assert program_instance_2.id == program_instance.id





