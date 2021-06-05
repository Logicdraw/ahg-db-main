from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud._base.spng_survey import (
	spng_survey_base_crud,
)

from main.schemas._base.spng_survey import (
	SpngSurveyBaseSchemaCreate,
	SpngSurveyBaseSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)

import pytest



@pytest.mark.asyncio
async def test_create_spng_survey_base(
	db: AsyncSession,
) -> None:
	# --
	survey_id = 123
	name = random_name()
	type = 'other'

	spng_survey_base_in = SpngSurveyBaseSchemaCreate(
		survey_id=survey_id,
		name=name,
		type=type,
	)
	spng_survey_base = await spng_survey_base_crud.create(
		db=db,
		obj_in=spng_survey_base_in,
	)

	assert spng_survey_base.survey_id == survey_id
	assert spng_survey_base.name == name



@pytest.mark.asyncio
async def test_create_sync_spng_survey_base(
	db: AsyncSession,
) -> None:
	# --
	survey_id = 123
	name = random_name()
	type = 'other'

	spng_survey_base_in = SpngSurveyBaseSchemaCreate(
		survey_id=survey_id,
		name=name,
		type=type,
	)
	spng_survey_base = await db.run_sync(
		spng_survey_base_crud.create_sync,
		obj_in=spng_survey_base_in,
	)

	assert spng_survey_base.survey_id == survey_id
	assert spng_survey_base.name == name



@pytest.mark.asyncio
async def test_get_spng_survey_base(
	db: AsyncSession,
) -> None:
	# --
	survey_id = 123
	name = random_name()
	type = 'other'

	spng_survey_base_in = SpngSurveyBaseSchemaCreate(
		survey_id=survey_id,
		name=name,
		type=type,
	)
	spng_survey_base = await spng_survey_base_crud.create(
		db=db,
		obj_in=spng_survey_base_in,
	)

	spng_survey_base_2 = await spng_survey_base_crud.get(
		db=db,
		id=spng_survey_base.id,
	)


	assert spng_survey_base_2
	assert jsonable_encoder(spng_survey_base) == jsonable_encoder(spng_survey_base_2)



@pytest.mark.asyncio
async def test_get_sync_spng_survey_base(
	db: AsyncSession,
) -> None:
	# --

	survey_id = 123
	name = random_name()
	type = 'other'

	spng_survey_base_in = SpngSurveyBaseSchemaCreate(
		survey_id=survey_id,
		name=name,
		type=type,
	)
	spng_survey_base = await db.run_sync(
		spng_survey_base_crud.create_sync,
		obj_in=spng_survey_base_in,
	)

	spng_survey_base_2 = await db.run_sync(
		spng_survey_base_crud.get_sync,
		id=spng_survey_base.id,
	)


	assert spng_survey_base_2
	assert jsonable_encoder(spng_survey_base) == jsonable_encoder(spng_survey_base_2)





@pytest.mark.asyncio
async def test_update_spng_survey_base(
	db: AsyncSession,
) -> None:
	# --
	survey_id = 123
	name = random_name()
	type = 'other'

	spng_survey_base_in = SpngSurveyBaseSchemaCreate(
		survey_id=survey_id,
		name=name,
		type=type,
	)
	spng_survey_base = await spng_survey_base_crud.create(
		db=db,
		obj_in=spng_survey_base_in,
	)


	new_name = random_name()
	while new_name == name:
		new_name = random_name()

	spng_survey_base_in_update = SpngSurveyBaseSchemaUpdate(
		name=new_name,
	)

	spng_survey_base_2 = await spng_survey_base_crud.update(
		db=db,
		db_obj=spng_survey_base,
		obj_in=spng_survey_base_in_update,
	)


	assert spng_survey_base_2
	assert spng_survey_base_2.name
	assert spng_survey_base_2.name == new_name



@pytest.mark.asyncio
async def test_update_sync_spng_survey_base(
	db: AsyncSession,
) -> None:
	# --

	survey_id = 123
	name = random_name()
	type = 'other'

	spng_survey_base_in = SpngSurveyBaseSchemaCreate(
		survey_id=survey_id,
		name=name,
		type=type,
	)
	spng_survey_base = await db.run_sync(
		spng_survey_base_crud.create_sync,
		obj_in=spng_survey_base_in,
	)

	new_name = random_name()
	while new_name == name:
		new_name = random_name()

	spng_survey_base_in_update = SpngSurveyBaseSchemaUpdate(
		name=new_name,
	)

	spng_survey_base_2 = await db.run_sync(
		spng_survey_base_crud.update_sync,
		db_obj=spng_survey_base,
		obj_in=spng_survey_base_in_update,
	)


	assert spng_survey_base_2
	assert spng_survey_base_2.name
	assert spng_survey_base_2.name == new_name



@pytest.mark.asyncio
async def test_delete_spng_survey_base(
	db: AsyncSession,
) -> None:
	# --
	survey_id = 123
	name = random_name()
	type = 'other'

	spng_survey_base_in = SpngSurveyBaseSchemaCreate(
		survey_id=survey_id,
		name=name,
		type=type,
	)
	spng_survey_base = await spng_survey_base_crud.create(
		db=db,
		obj_in=spng_survey_base_in,
	)

	spng_survey_base_2 = await spng_survey_base_crud.delete(
		db=db,
		id=spng_survey_base.id,
	)

	spng_survey_base_3 = await spng_survey_base_crud.get(
		db=db,
		id=spng_survey_base.id,
	)


	assert spng_survey_base_3 is None
	assert spng_survey_base_2.id == spng_survey_base.id




@pytest.mark.asyncio
async def test_delete_sync_spng_survey_base(
	db: AsyncSession,
) -> None:
	# --

	survey_id = 123
	name = random_name()
	type = 'other'

	spng_survey_base_in = SpngSurveyBaseSchemaCreate(
		survey_id=survey_id,
		name=name,
		type=type,
	)
	spng_survey_base = await db.run_sync(
		spng_survey_base_crud.create_sync,
		obj_in=spng_survey_base_in,
	)

	spng_survey_base_2 = await db.run_sync(
		spng_survey_base_crud.delete_sync,
		id=spng_survey_base.id,
	)

	spng_survey_base_3 = await db.run_sync(
		spng_survey_base_crud.get_sync,
		id=spng_survey_base.id,
	)


	assert spng_survey_base_3 is None
	assert spng_survey_base_2.id == spng_survey_base.id






