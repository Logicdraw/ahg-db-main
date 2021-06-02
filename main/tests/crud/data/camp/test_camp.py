from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.camp import (
	camp_crud,
)

from main.schemas.data.camp import (
	CampSchemaCreate,
	CampSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest




@pytest.mark.asyncio
async def test_create_camp(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()

	camp_in = CampSchemaCreate(
		name=name,
	)

	camp = await camp_crud.create(
		db=db,
		obj_in=camp_in,
	)


	assert camp.name == name



@pytest.mark.asyncio
async def test_create_sync_camp(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()

	camp_in = CampSchemaCreate(
		name=name,
	)

	camp = await db.run_sync(
		camp_crud.create_sync,
		obj_in=camp_in,
	)

	assert camp.name == name



@pytest.mark.asyncio
async def test_get_camp(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()

	camp_in = CampSchemaCreate(
		name=name,
	)

	camp = await camp_crud.create(
		db=db,
		obj_in=camp_in,
	)

	camp_2 = await camp_crud.get(
		db=db,
		id=camp.id,
	)

	assert camp_2
	assert jsonable_encoder(camp) == jsonable_encoder(camp_2)



@pytest.mark.asyncio
async def test_get_sync_camp(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()

	camp_in = CampSchemaCreate(
		name=name,
	)

	camp = await db.run_sync(
		camp_crud.create_sync,
		obj_in=camp_in,
	)

	camp_2 = await db.run_sync(
		camp_crud.get_sync,
		id=camp.id,
	)

	assert camp_2
	assert jsonable_encoder(camp) == jsonable_encoder(camp_2)



@pytest.mark.asyncio
async def test_update_camp(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()

	camp_in = CampSchemaCreate(
		name=name,
	)

	camp = await camp_crud.create(
		db=db,
		obj_in=camp_in,
	)

	new_name = random_lower_string()

	camp_in_update = CampSchemaUpdate(
		name=new_name,
	)


	camp_2 = await camp_crud.update(
		db=db,
		db_obj=camp,
		obj_in=camp_in_update,
	)

	assert camp_2
	assert camp_2.name
	assert camp_2.name == new_name



@pytest.mark.asyncio
async def test_update_sync_camp(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()

	camp_in = CampSchemaCreate(
		name=name,
	)

	camp = await db.run_sync(
		camp_crud.create_sync,
		obj_in=camp_in,
	)

	new_name = random_lower_string()

	camp_in_update = CampSchemaUpdate(
		name=new_name,
	)


	camp_2 = await db.run_sync(
		camp_crud.update_sync,
		db_obj=camp,
		obj_in=camp_in_update,
	)

	assert camp_2
	assert camp_2.name
	assert camp_2.name == new_name



@pytest.mark.asyncio
async def test_delete_camp(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()

	camp_in = CampSchemaCreate(
		name=name,
	)

	camp = await camp_crud.create(
		db=db,
		obj_in=camp_in,
	)

	
	camp_2 = await camp_crud.delete(
		db=db,
		id=camp.id,
	)


	camp_3 = await camp_crud.get(
		db=db,
		id=camp.id,
	)


	assert camp_3 is None
	assert camp_2.id == camp.id



@pytest.mark.asyncio
async def test_delete_sync_camp(
	db: AsyncSession,
) -> None:
	# --
	name = random_lower_string()

	camp_in = CampSchemaCreate(
		name=name,
	)

	camp = await db.run_sync(
		camp_crud.create_sync,
		obj_in=camp_in,
	)

	
	camp_2 = await db.run_sync(
		camp_crud.delete_sync,
		id=camp.id,
	)


	camp_3 = await db.run_sync(
		camp_crud.get_sync,
		id=camp.id,
	)


	assert camp_3 is None
	assert camp_2.id == camp.id




