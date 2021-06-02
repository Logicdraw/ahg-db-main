from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.program import (
	program_crud,
)

from main.schemas.data.program import (
	ProgramSchemaCreate,
	ProgramSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest





@pytest.mark.asyncio
async def test_create_program(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()

	program_in = ProgramSchemaCreate(
		name=name,
	)

	program = await program_crud.create(
		db=db,
		obj_in=program_in,
	)


	assert program
	assert program.name == name



@pytest.mark.asyncio
async def test_create_sync_program(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	program_in = ProgramSchemaCreate(
		name=name,
	)

	program = await db.run_sync(
		program_crud.create_sync,
		obj_in=program_in,
	)

	assert program
	assert program.name == name



@pytest.mark.asyncio
async def test_get_program(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	program_in = ProgramSchemaCreate(
		name=name,
	)

	program = await program_crud.create(
		db=db,
		obj_in=program_in,
	)

	program_2 = await program_crud.get(
		db=db,
		id=program.id,
	)


	assert program_2
	assert jsonable_encoder(program) == jsonable_encoder(program_2)



@pytest.mark.asyncio
async def test_get_sync_program(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	program_in = ProgramSchemaCreate(
		name=name,
	)

	program = await db.run_sync(
		program_crud.create_sync,
		obj_in=program_in,
	)

	program_2 = await db.run_sync(
		program_crud.get_sync,
		id=program.id,
	)

	assert program_2
	assert jsonable_encoder(program) == jsonable_encoder(program_2)



@pytest.mark.asyncio
async def test_update_program(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	program_in = ProgramSchemaCreate(
		name=name,
	)

	program = await program_crud.create(
		db=db,
		obj_in=program_in,
	)

	new_name = random_lower_string()

	program_in_update = ProgramSchemaUpdate(
		name=new_name,
	)


	program_2 = await program_crud.update(
		db=db,
		db_obj=program,
		obj_in=program_in_update,
	)

	assert program_2
	assert program_2.name
	assert program_2.name == new_name



@pytest.mark.asyncio
async def test_update_sync_program(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	program_in = ProgramSchemaCreate(
		name=name,
	)

	program = await db.run_sync(
		program_crud.create_sync,
		obj_in=program_in,
	)

	new_name = random_lower_string()

	program_in_update = ProgramSchemaUpdate(
		name=new_name,
	)


	program_2 = await db.run_sync(
		program_crud.update_sync,
		db_obj=program,
		obj_in=program_in_update,
	)

	assert program_2
	assert program_2.name
	assert program_2.name == new_name



@pytest.mark.asyncio
async def test_delete_program(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	program_in = ProgramSchemaCreate(
		name=name,
	)

	program = await program_crud.create(
		db=db,
		obj_in=program_in,
	)

	program_2 = await program_crud.delete(
		db=db,
		id=program.id,
	)

	program_3 = await program_crud.get(
		db=db,
		id=program.id,
	)


	assert program_3 is None
	assert program_2.id == program.id




@pytest.mark.asyncio
async def test_delete_sync_program(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	program_in = ProgramSchemaCreate(
		name=name,
	)

	program = await db.run_sync(
		program_crud.create_sync,
		obj_in=program_in,
	)

	program_2 = await db.run_sync(
		program_crud.delete_sync,
		id=program.id,
	)

	program_3 = await db.run_sync(
		program_crud.get_sync,
		id=program.id,
	)


	assert program_3 is None
	assert program_2.id == program.id











