from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.person.adult_rep import (
	adult_rep_crud,
)

from main.schemas.data.person.adult_rep import (
	AdultRepSchemaCreate,
	AdultRepSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest




@pytest.mark.asyncio
async def test_create_adult_rep(
	db: AsyncSession,
) -> None:
	# --
	full_name = random_name()
	email = random_email()

	adult_rep_in = AdultRepSchemaCreate(
		full_name=full_name,
		email=email,
	)
	
	adult_rep = await adult_rep_crud.create(
		db=db,
		obj_in=adult_rep_in,
	)

	assert adult_rep
	assert adult_rep.full_name == full_name
	assert adult_rep.email == email



@pytest.mark.asyncio
async def test_create_sync_adult_rep(
	db: AsyncSession,
) -> None:
	# --
	full_name = random_name()
	email = random_email()

	adult_rep_in = AdultRepSchemaCreate(
		full_name=full_name,
		email=email,
	)

	adult_rep = await db.run_sync(
		adult_rep_crud.create_sync,
		obj_in=adult_rep_in,
	)

	assert adult_rep
	assert adult_rep.full_name == full_name
	assert adult_rep.email == email



@pytest.mark.asyncio
async def test_get_adult_rep(
	db: AsyncSession,
) -> None:
	# --
	full_name = random_name()
	email = random_email()

	adult_rep_in = AdultRepSchemaCreate(
		full_name=full_name,
		email=email,
	)

	adult_rep = await adult_rep_crud.create(
		db=db,
		obj_in=adult_rep_in,
	)

	adult_rep_2 = await adult_rep_crud.get(
		db=db,
		id=adult_rep.id,
	)

	assert adult_rep_2
	assert jsonable_encoder(adult_rep) == jsonable_encoder(adult_rep_2)



@pytest.mark.asyncio
async def test_get_sync_adult_rep(
	db: AsyncSession,
) -> None:
	# --
	full_name = random_name()
	email = random_email()

	adult_rep_in = AdultRepSchemaCreate(
		full_name=full_name,
		email=email,
	)

	adult_rep = await db.run_sync(
		adult_rep_crud.create_sync,
		obj_in=adult_rep_in,
	)

	adult_rep_2 = await db.run_sync(
		adult_rep_crud.get_sync,
		id=adult_rep.id,
	)

	assert adult_rep_2
	assert jsonable_encoder(adult_rep) == jsonable_encoder(adult_rep_2)



@pytest.mark.asyncio
async def test_update_adult_rep(
	db: AsyncSession,
) -> None:
	# --
	full_name = random_name()
	email = random_email()

	adult_rep_in = AdultRepSchemaCreate(
		full_name=full_name,
		email=email,
	)
	adult_rep = await adult_rep_crud.create(
		db=db,
		obj_in=adult_rep_in,
	)

	new_full_name = random_name()

	adult_rep_in_update = AdultRepSchemaUpdate(
		full_name=new_full_name, # New Name --
	)

	adult_rep_2 = await adult_rep_crud.update(
		db=db,
		db_obj=adult_rep,
		obj_in=adult_rep_in_update,
	)

	assert adult_rep_2
	assert adult_rep_2.full_name
	assert adult_rep_2.full_name == new_full_name



@pytest.mark.asyncio
async def test_update_sync_adult_rep(
	db: AsyncSession,
) -> None:
	# --
	full_name = random_name()
	email = random_email()

	adult_rep_in = AdultRepSchemaCreate(
		full_name=full_name,
		email=email,
	)

	adult_rep = await db.run_sync(
		adult_rep_crud.create_sync,
		obj_in=adult_rep_in,
	)


	new_full_name = random_name()

	adult_rep_in_update = AdultRepSchemaUpdate(
		full_name=new_full_name, # New Name --
	)


	adult_rep_2 = await db.run_sync(
		adult_rep_crud.update_sync,
		db_obj=adult_rep,
		obj_in=adult_rep_in_update,
	)

	assert adult_rep_2
	assert adult_rep_2.full_name
	assert adult_rep_2.full_name == new_full_name



@pytest.mark.asyncio
async def test_delete_adult_rep(
	db: AsyncSession,
) -> None:
	# --
	full_name = random_name()
	email = random_email()

	adult_rep_in = AdultRepSchemaCreate(
		full_name=full_name,
		email=email,
	)
	adult_rep = await adult_rep_crud.create(
		db=db,
		obj_in=adult_rep_in,
	)

	adult_rep_2 = await adult_rep_crud.delete(
		db=db,
		id=adult_rep.id,
	)

	adult_rep_3 = await adult_rep_crud.get(
		db=db,
		id=adult_rep.id,
	)

	assert adult_rep_3 is None
	assert adult_rep_2.id == adult_rep.id



@pytest.mark.asyncio
async def test_delete_sync_adult_rep(
	db: AsyncSession,
) -> None:
	# --
	full_name = random_name()
	email = random_email()

	adult_rep_in = AdultRepSchemaCreate(
		full_name=full_name,
		email=email,
	)

	adult_rep = await db.run_sync(
		adult_rep_crud.create_sync,
		obj_in=adult_rep_in,
	)

	adult_rep_2 = await db.run_sync(
		adult_rep_crud.delete_sync,
		id=adult_rep.id,
	)

	adult_rep_3 = await db.run_sync(
		adult_rep_crud.get_sync,
		id=adult_rep.id,
	)


	assert adult_rep_3 is None
	assert adult_rep_2.id == adult_rep.id





