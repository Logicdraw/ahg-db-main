from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.program.group import (
	program_group_crud,
)

from main.schemas.data.program.group import (
	ProgramGroupSchemaCreate,
	ProgramGroupSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest





@pytest.mark.asyncio
async def test_create_program_group(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	program_group_in = ProgramGroupSchemaCreate(
		name=name,
	)

	program_group = await program_group_crud.create(
		db=db,
		obj_in=program_group_in,
	)


	assert program_group.name == name



@pytest.mark.asyncio
async def test_create_sync_program_group(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	program_group_in = ProgramGroupSchemaCreate(
		name=name,
	)

	program_group = await db.run_sync(
		program_group_crud.create_sync,
		obj_in=program_group_in,
	)


	assert program_group.name == name




@pytest.mark.asyncio
async def test_get_program_group(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	program_group_in = ProgramGroupSchemaCreate(
		name=name,
	)

	program_group = await program_group_crud.create(
		db=db,
		obj_in=program_group_in,
	)

	program_group_2 = await program_group_crud.get(
		db=db,
		id=program_group.id,
	)


	assert program_group_2
	assert jsonable_encoder(program_group) == jsonable_encoder(program_group_2)



@pytest.mark.asyncio
async def test_get_sync_program_group(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	program_group_in = ProgramGroupSchemaCreate(
		name=name,
	)

	program_group = await db.run_sync(
		program_group_crud.create_sync,
		obj_in=program_group_in,
	)

	program_group_2 = await db.run_sync(
		program_group_crud.get_sync,
		id=program_group.id,
	)


	assert program_group_2
	assert jsonable_encoder(program_group) == jsonable_encoder(program_group_2)



@pytest.mark.asyncio
async def test_update_program_group(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	program_group_in = ProgramGroupSchemaCreate(
		name=name,
	)

	program_group = await program_group_crud.create(
		db=db,
		obj_in=program_group_in,
	)

	new_name = random_lower_string()

	program_group_in_update = ProgramGroupSchemaUpdate(
		name=new_name,
	)

	program_group_2 = await program_group_crud.update(
		db=db,
		db_obj=program_group,
		obj_in=program_group_in_update,
	)


	assert program_group_2
	assert program_group_2.name
	assert program_group_2.name == new_name



@pytest.mark.asyncio
async def test_update_sync_program_group(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	program_group_in = ProgramGroupSchemaCreate(
		name=name,
	)

	program_group = await db.run_sync(
		program_group_crud.create_sync,
		obj_in=program_group_in,
	)

	new_name = random_lower_string()

	program_group_in_update = ProgramGroupSchemaUpdate(
		name=new_name,
	)

	program_group_2 = await db.run_sync(
		program_group_crud.update_sync,
		db_obj=program_group,
		obj_in=program_group_in_update,
	)


	assert program_group_2
	assert program_group_2.name
	assert program_group_2.name == new_name



@pytest.mark.asyncio
async def test_delete_program_group(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	program_group_in = ProgramGroupSchemaCreate(
		name=name,
	)

	program_group = await program_group_crud.create(
		db=db,
		obj_in=program_group_in,
	)

	program_group_2 = await program_group_crud.delete(
		db=db,
		id=program_group.id,
	)

	program_group_3 = await program_group_crud.get(
		db=db,
		id=program_group.id,
	)

	assert program_group_3 is None
	assert program_group_2.id == program_group.id



@pytest.mark.asyncio
async def test_delete_sync_program_group(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	program_group_in = ProgramGroupSchemaCreate(
		name=name,
	)

	program_group = await db.run_sync(
		program_group_crud.create_sync,
		obj_in=program_group_in,
	)

	program_group_2 = await db.run_sync(
		program_group_crud.delete_sync,
		id=program_group.id,
	)

	program_group_3 = await db.run_sync(
		program_group_crud.get_sync,
		id=program_group.id,
	)

	assert program_group_3 is None
	assert program_group_2.id == program_group.id





