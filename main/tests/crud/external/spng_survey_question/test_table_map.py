from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.external.spng_survey_question.table_map import (
	spng_survey_question_table_map_crud,
)

from main.schemas.external.spng_survey_question.table_map import (
	SpngSurveyQuestionTableMapSchemaCreate,
	SpngSurveyQuestionTableMapSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
	random_number,
)


import pytest




@pytest.mark.asyncio
async def test_create_spng_survey_question_table_map(
	db: AsyncSession,
) -> None:
	# --
	db_table_name = random_lower_string()
	db_table_column_name = random_lower_string()

	spng_survey_question_table_map_in = SpngSurveyQuestionTableMapSchemaCreate(
		db_table_name=db_table_name,
		db_table_column_name=db_table_column_name,
	)

	spng_survey_question_table_map = await spng_survey_question_table_map_crud.create(
		db=db,
		obj_in=spng_survey_question_table_map_in,
	)


	assert spng_survey_question_table_map.db_table_name == db_table_name
	assert spng_survey_question_table_map.db_table_column_name == db_table_column_name



@pytest.mark.asyncio
async def test_create_sync_spng_survey_question_table_map(
	db: AsyncSession,
) -> None:
	# --
	db_table_name = random_lower_string()
	db_table_column_name = random_lower_string()

	spng_survey_question_table_map_in = SpngSurveyQuestionTableMapSchemaCreate(
		db_table_name=db_table_name,
		db_table_column_name=db_table_column_name,
	)

	spng_survey_question_table_map = await db.run_sync(
		spng_survey_question_table_map_crud.create_sync,
		obj_in=spng_survey_question_table_map_in,
	)


	assert spng_survey_question_table_map.db_table_name == db_table_name
	assert spng_survey_question_table_map.db_table_column_name == db_table_column_name



@pytest.mark.asyncio
async def test_get_spng_survey_question_table_map(
	db: AsyncSession,
) -> None:
	# --
	db_table_name = random_lower_string()
	db_table_column_name = random_lower_string()

	spng_survey_question_table_map_in = SpngSurveyQuestionTableMapSchemaCreate(
		db_table_name=db_table_name,
		db_table_column_name=db_table_column_name,
	)

	spng_survey_question_table_map = await spng_survey_question_table_map_crud.create(
		db=db,
		obj_in=spng_survey_question_table_map_in,
	)

	spng_survey_question_table_map_2 = await spng_survey_question_table_map_crud.get(
		db=db,
		id=spng_survey_question_table_map.id,
	)

	assert spng_survey_question_table_map_2
	assert jsonable_encoder(spng_survey_question_table_map_2) == jsonable_encoder(spng_survey_question_table_map)



@pytest.mark.asyncio
async def test_get_sync_spng_survey_question_table_map(
	db: AsyncSession,
) -> None:
	# --
	db_table_name = random_lower_string()
	db_table_column_name = random_lower_string()

	spng_survey_question_table_map_in = SpngSurveyQuestionTableMapSchemaCreate(
		db_table_name=db_table_name,
		db_table_column_name=db_table_column_name,
	)

	spng_survey_question_table_map = await db.run_sync(
		spng_survey_question_table_map_crud.create_sync,
		obj_in=spng_survey_question_table_map_in,
	)

	spng_survey_question_table_map_2 = await db.run_sync(
		spng_survey_question_table_map_crud.get_sync,
		id=spng_survey_question_table_map.id,
	)

	assert spng_survey_question_table_map_2
	assert jsonable_encoder(spng_survey_question_table_map_2) == jsonable_encoder(spng_survey_question_table_map)



@pytest.mark.asyncio
async def test_update_spng_survey_question_table_map(
	db: AsyncSession,
) -> None:
	# --

	db_table_name = random_lower_string()
	db_table_column_name = random_lower_string()

	spng_survey_question_table_map_in = SpngSurveyQuestionTableMapSchemaCreate(
		db_table_name=db_table_name,
		db_table_column_name=db_table_column_name,
	)

	spng_survey_question_table_map = await spng_survey_question_table_map_crud.create(
		db=db,
		obj_in=spng_survey_question_table_map_in,
	)

	new_db_table_name = random_lower_string()
	while new_db_table_name == db_table_name:
		new_db_table_name = random_lower_string()

	spng_survey_question_table_map_in_update = SpngSurveyQuestionTableMapSchemaUpdate(
		db_table_name=new_db_table_name,
	)

	spng_survey_question_table_map_2 = await spng_survey_question_table_map_crud.update(
		db=db,
		db_obj=spng_survey_question_table_map,
		obj_in=spng_survey_question_table_map_in_update,
	)

	assert spng_survey_question_table_map_2
	assert spng_survey_question_table_map_2.db_table_name
	assert spng_survey_question_table_map_2.db_table_name == new_db_table_name



@pytest.mark.asyncio
async def test_update_sync_spng_survey_question_table_map(
	db: AsyncSession,
) -> None:
	# --

	db_table_name = random_lower_string()
	db_table_column_name = random_lower_string()

	spng_survey_question_table_map_in = SpngSurveyQuestionTableMapSchemaCreate(
		db_table_name=db_table_name,
		db_table_column_name=db_table_column_name,
	)

	spng_survey_question_table_map = await db.run_sync(
		spng_survey_question_table_map_crud.create_sync,
		obj_in=spng_survey_question_table_map_in,
	)

	new_db_table_name = random_lower_string()
	while new_db_table_name == db_table_name:
		new_db_table_name = random_lower_string()

	spng_survey_question_table_map_in_update = SpngSurveyQuestionTableMapSchemaUpdate(
		db_table_name=new_db_table_name,
	)

	spng_survey_question_table_map_2 = await db.run_sync(
		spng_survey_question_table_map_crud.update_sync,
		db_obj=spng_survey_question_table_map,
		obj_in=spng_survey_question_table_map_in_update,
	)

	assert spng_survey_question_table_map_2
	assert spng_survey_question_table_map_2.db_table_name
	assert spng_survey_question_table_map_2.db_table_name == new_db_table_name



@pytest.mark.asyncio
async def test_delete_spng_survey_question_table_map(
	db: AsyncSession,
) -> None:
	# --

	db_table_name = random_lower_string()
	db_table_column_name = random_lower_string()

	spng_survey_question_table_map_in = SpngSurveyQuestionTableMapSchemaCreate(
		db_table_name=db_table_name,
		db_table_column_name=db_table_column_name,
	)

	spng_survey_question_table_map = await spng_survey_question_table_map_crud.create(
		db=db,
		obj_in=spng_survey_question_table_map_in,
	)

	spng_survey_question_table_map_2 = await spng_survey_question_table_map_crud.delete(
		db=db,
		id=spng_survey_question_table_map.id,
	)

	spng_survey_question_table_map_3 = await spng_survey_question_table_map_crud.get(
		db=db,
		id=spng_survey_question_table_map.id,
	)


	assert spng_survey_question_table_map_3 is None
	assert spng_survey_question_table_map_2.id == spng_survey_question_table_map.id




@pytest.mark.asyncio
async def test_delete_sync_spng_survey_question_table_map(
	db: AsyncSession,
) -> None:
	# --

	db_table_name = random_lower_string()
	db_table_column_name = random_lower_string()

	spng_survey_question_table_map_in = SpngSurveyQuestionTableMapSchemaCreate(
		db_table_name=db_table_name,
		db_table_column_name=db_table_column_name,
	)

	spng_survey_question_table_map = await db.run_sync(
		spng_survey_question_table_map_crud.create_sync,
		obj_in=spng_survey_question_table_map_in,
	)

	spng_survey_question_table_map_2 = await db.run_sync(
		spng_survey_question_table_map_crud.delete_sync,
		id=spng_survey_question_table_map.id,
	)

	spng_survey_question_table_map_3 = await db.run_sync(
		spng_survey_question_table_map_crud.get_sync,
		id=spng_survey_question_table_map.id,
	)


	assert spng_survey_question_table_map_3 is None
	assert spng_survey_question_table_map_2.id == spng_survey_question_table_map.id






