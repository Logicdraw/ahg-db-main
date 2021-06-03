from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.team.division import (
	division_crud,
)

from main.schemas.data.team.division import (
	DivisionSchemaCreate,
	DivisionSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest




@pytest.mark.asyncio
async def test_create_division(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()

	division_in = DivisionSchemaCreate(
		name=name,
	)

	division = await division_crud.create(
		db=db,
		obj_in=division_in,
	)

	assert division.name == name


@pytest.mark.asyncio
async def test_create_sync_division(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()

	division_in = DivisionSchemaCreate(
		name=name,
	)

	division = await db.run_sync(
		division_crud.create_sync,
		obj_in=division_in,
	)

	assert division.name == name



@pytest.mark.asyncio
async def test_get_division(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	division_in = DivisionSchemaCreate(
		name=name,
	)

	division = await division_crud.create(
		db=db,
		obj_in=division_in,
	)

	division_2 = await division_crud.get(
		db=db,
		id=division.id,
	)

	assert division_2
	assert jsonable_encoder(division_2) == jsonable_encoder(division)



@pytest.mark.asyncio
async def test_get_sync_division(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	division_in = DivisionSchemaCreate(
		name=name,
	)

	division = await db.run_sync(
		division_crud.create_sync,
		obj_in=division_in,
	)

	division_2 = await db.run_sync(
		division_crud.get_sync,
		id=division.id,
	)

	assert division_2
	assert jsonable_encoder(division_2) == jsonable_encoder(division)



@pytest.mark.asyncio
async def test_update_division(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	division_in = DivisionSchemaCreate(
		name=name,
	)

	division = await division_crud.create(
		db=db,
		obj_in=division_in,
	)

	new_name = random_lower_string()
	while new_name == name:
		new_name = random_lower_string()

	division_in_update = DivisionSchemaUpdate(
		name=new_name,
	)

	division_2 = await division_crud.update(
		db=db,
		db_obj=division,
		obj_in=division_in_update,
	)

	assert division_2
	assert division_2.name
	assert division_2.name == new_name



@pytest.mark.asyncio
async def test_update_sync_division(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	division_in = DivisionSchemaCreate(
		name=name,
	)

	division = await db.run_sync(
		division_crud.create_sync,
		obj_in=division_in,
	)

	new_name = random_lower_string()
	while new_name == name:
		new_name = random_lower_string()

	division_in_update = DivisionSchemaUpdate(
		name=new_name,
	)

	division_2 = await db.run_sync(
		division_crud.update_sync,
		db_obj=division,
		obj_in=division_in_update,
	)

	assert division_2
	assert division_2.name
	assert division_2.name == new_name



@pytest.mark.asyncio
async def test_delete_division(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	division_in = DivisionSchemaCreate(
		name=name,
	)

	division = await division_crud.create(
		db=db,
		obj_in=division_in,
	)

	division_2 = await division_crud.delete(
		db=db,
		id=division.id,
	)

	division_3 = await division_crud.get(
		db=db,
		id=division.id,
	)

	assert division_3 is None
	assert division_2.id == division.id



@pytest.mark.asyncio
async def test_delete_sync_division(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()

	division_in = DivisionSchemaCreate(
		name=name,
	)

	division = await db.run_sync(
		division_crud.create_sync,
		obj_in=division_in,
	)

	division_2 = await db.run_sync(
		division_crud.delete_sync,
		id=division.id,
	)

	division_3 = await db.run_sync(
		division_crud.get_sync,
		id=division.id,
	)

	assert division_3 is None
	assert division_2.id == division.id




