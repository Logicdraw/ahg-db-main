from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.external.spng_survey.program import (
	spng_survey_program_crud,
)

from main.schemas.external.spng_survey.program import (
	SpngSurveyProgramSchemaCreate,
	SpngSurveyProgramSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest






@pytest.mark.asyncio
async def test_create_spng_survey_program(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	is_active = True
	type = 'program'

	spng_survey_program_in = SpngSurveyProgramSchemaCreate(
		name=name,
		is_active=is_active,
		type=type,
	)

	spng_survey_program = await spng_survey_program_crud.create(
		db=db,
		obj_in=spng_survey_program_in,
	)

	assert spng_survey_program.name == name
	assert spng_survey_program.is_active == is_active
	assert spng_survey_program.type == type



@pytest.mark.asyncio
async def test_create_spng_survey_program(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	is_active = True
	type = 'program'

	spng_survey_program_in = SpngSurveyProgramSchemaCreate(
		name=name,
		is_active=is_active,
		type=type,
	)

	spng_survey_program = await db.run_sync(
		spng_survey_program_crud.create_sync,
		obj_in=spng_survey_program_in,
	)

	assert spng_survey_program.name == name
	assert spng_survey_program.is_active == is_active
	assert spng_survey_program.type == type



@pytest.mark.asyncio
async def test_get_spng_survey_program(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	is_active = True
	type = 'program'

	spng_survey_program_in = SpngSurveyProgramSchemaCreate(
		name=name,
		is_active=is_active,
		type=type,
	)

	spng_survey_program = await spng_survey_program_crud.create(
		db=db,
		obj_in=spng_survey_program_in,
	)

	spng_survey_program_2 = await spng_survey_program_crud.get(
		db=db,
		id=spng_survey_program.id,
	)

	assert spng_survey_program_2
	assert jsonable_encoder(spng_survey_program_2) == jsonable_encoder(spng_survey_program)



@pytest.mark.asyncio
async def test_get_sync_spng_survey_program(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	is_active = True
	type = 'program'

	spng_survey_program_in = SpngSurveyProgramSchemaCreate(
		name=name,
		is_active=is_active,
		type=type,
	)

	spng_survey_program = await db.run_sync(
		spng_survey_program_crud.create_sync,
		obj_in=spng_survey_program_in,
	)

	spng_survey_program_2 = await db.run_sync(
		spng_survey_program_crud.get_sync,
		id=spng_survey_program.id,
	)

	assert spng_survey_program_2
	assert jsonable_encoder(spng_survey_program_2) == jsonable_encoder(spng_survey_program)



@pytest.mark.asyncio
async def test_update_spng_survey_program(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	is_active = True
	type = 'program'

	spng_survey_program_in = SpngSurveyProgramSchemaCreate(
		name=name,
		is_active=is_active,
		type=type,
	)

	spng_survey_program = await spng_survey_program_crud.create(
		db=db,
		obj_in=spng_survey_program_in,
	)

	new_name = random_lower_string()
	while new_name == name:
		new_name = random_lower_string()

	spng_survey_program_in_update = SpngSurveyProgramSchemaUpdate(
		name=new_name,
	)

	spng_survey_program_2 = await spng_survey_program_crud.update(
		db=db,
		db_obj=spng_survey_program,
		obj_in=spng_survey_program_in_update,
	)

	assert spng_survey_program_2
	assert spng_survey_program_2.name
	assert spng_survey_program_2.name == new_name



@pytest.mark.asyncio
async def test_update_sync_spng_survey_program(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	is_active = True
	type = 'program'

	spng_survey_program_in = SpngSurveyProgramSchemaCreate(
		name=name,
		is_active=is_active,
		type=type,
	)

	spng_survey_program = await db.run_sync(
		spng_survey_program_crud.create_sync,
		obj_in=spng_survey_program_in,
	)

	spng_survey_program_2 = await db.run_sync(
		spng_survey_program_crud.update_sync,
		db_obj=spng_survey_program,
		obj_in=spng_survey_program_in_update,
	)

	assert spng_survey_program_2
	assert spng_survey_program_2.name
	assert spng_survey_program_2.name == new_name


@pytest.mark.asyncio
async def test_delete_spng_survey_program(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	is_active = True
	type = 'program'

	spng_survey_program_in = SpngSurveyProgramSchemaCreate(
		name=name,
		is_active=is_active,
		type=type,
	)

	spng_survey_program = await spng_survey_program_crud.create(
		db=db,
		obj_in=spng_survey_program_in,
	)

	spng_survey_program_2 = await spng_survey_program_crud.delete(
		db=db,
		id=spng_survey_program.id,
	)

	spng_survey_program_3 = await spng_survey_program_crud.get(
		db=db,
		id=spng_survey_program.id,
	)

	assert spng_survey_program_3 is None
	assert spng_survey_program_2.id == spng_survey_program.id


@pytest.mark.asyncio
async def test_delete_sync_spng_survey_program(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	is_active = True
	type = 'program'

	spng_survey_program_in = SpngSurveyProgramSchemaCreate(
		name=name,
		is_active=is_active,
		type=type,
	)

	spng_survey_program = await db.run_sync(
		spng_survey_program_crud.create_sync,
		obj_in=spng_survey_program_in,
	)

	spng_survey_program_2 = await db.run_sync(
		spng_survey_program_crud.delete_sync,
		id=spng_survey_program.id,
	)

	spng_survey_program_3 = await db.run_sync(
		spng_survey_program_crud.get_sync,
		id=spng_survey_program.id,
	)

	assert spng_survey_program_3 is None
	assert spng_survey_program_2.id == spng_survey_program.id



