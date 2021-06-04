from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud._many.spng_surveys_spng_survey_questions import (
	spng_surveys_spng_survey_questions_crud,
)

from main.schemas._many.spng_surveys_spng_survey_questions import (
	SpngSurveysSpngSurveyQuestionsSchemaCreate,
	SpngSurveysSpngSurveyQuestionsSchemaUpdate,
)



from main.crud._base.spng_survey import (
	spng_survey_base_crud,
)

from main.schemas._base.spng_survey import (
	SpngSurveyBaseSchemaCreate,
	SpngSurveyBaseSchemaUpdate,
)


from main.crud.external.spng_survey_question import (
	spng_survey_question_crud,
)

from main.schemas.external.spng_survey_question import (
	SpngSurveyQuestionSchemaCreate,
	SpngSurveyQuestionSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest




@pytest.mark.asyncio
async def test_create_spng_survey_spng_survey_question(
	db: AsyncSession,
) -> None:
	# --

	spng_survey_in = SpngSurveyBaseSchemaCreate(
		type='other',
	)

	spng_survey = await spng_survey_base_crud.create(
		db=db,
		obj_in=spng_survey_in,
	)


	spng_survey_question_in = SpngSurveyQuestionSchemaCreate()

	spng_survey_question = await spng_survey_question_crud.create(
		db=db,
		obj_in=spng_survey_question_in,
	)


	spng_survey_spng_survey_question_in = SpngSurveysSpngSurveyQuestionsSchemaCreate(
		spng_survey_id=spng_survey.id,
		spng_survey_question_id=spng_survey_question.id,
		included_in_db=True,
	)


	spng_survey_spng_survey_question = await spng_surveys_spng_survey_questions_crud.create(
		db=db,
		obj_in=spng_survey_spng_survey_question_in,
	)


	assert spng_survey_spng_survey_question.spng_survey_id == spng_survey.id
	assert spng_survey_spng_survey_question.spng_survey_question_id == spng_survey_question.id



@pytest.mark.asyncio
async def test_create_sync_spng_survey_spng_survey_question(
	db: AsyncSession,
) -> None:
	# --

	spng_survey_in = SpngSurveyBaseSchemaCreate(
		type='other',
	)

	spng_survey = await db.run_sync(
		spng_survey_base_crud.create_sync,
		obj_in=spng_survey_in,
	)


	spng_survey_question_in = SpngSurveyQuestionSchemaCreate()

	spng_survey_question = await db.run_sync(
		spng_survey_question_crud.create_sync,
		obj_in=spng_survey_question_in,
	)


	spng_survey_spng_survey_question_in = SpngSurveysSpngSurveyQuestionsSchemaCreate(
		spng_survey_id=spng_survey.id,
		spng_survey_question_id=spng_survey_question.id,
		included_in_db=True,
	)


	spng_survey_spng_survey_question = await db.run_sync(
		spng_surveys_spng_survey_questions_crud.create_sync,
		obj_in=spng_survey_spng_survey_question_in,
	)


	assert spng_survey_spng_survey_question.spng_survey_id == spng_survey.id
	assert spng_survey_spng_survey_question.spng_survey_question_id == spng_survey_question.id





@pytest.mark.asyncio
async def test_get_spng_survey_spng_survey_question(
	db: AsyncSession,
) -> None:
	# --

	spng_survey_in = SpngSurveyBaseSchemaCreate(
		type='other',
	)

	spng_survey = await spng_survey_base_crud.create(
		db=db,
		obj_in=spng_survey_in,
	)


	spng_survey_question_in = SpngSurveyQuestionSchemaCreate()

	spng_survey_question = await spng_survey_question_crud.create(
		db=db,
		obj_in=spng_survey_question_in,
	)


	spng_survey_spng_survey_question_in = SpngSurveysSpngSurveyQuestionsSchemaCreate(
		spng_survey_id=spng_survey.id,
		spng_survey_question_id=spng_survey_question.id,
		included_in_db=True,
	)


	spng_survey_spng_survey_question = await spng_surveys_spng_survey_questions_crud.create(
		db=db,
		obj_in=spng_survey_spng_survey_question_in,
	)

	spng_survey_spng_survey_question_2 = await spng_surveys_spng_survey_questions_crud.get(
		db=db,
		spng_survey_id=spng_survey.id,
		spng_survey_question_id=spng_survey_question.id,
	)

	assert spng_survey_spng_survey_question_2
	assert jsonable_encoder(spng_survey_spng_survey_question_2) == jsonable_encoder(spng_survey_spng_survey_question)



@pytest.mark.asyncio
async def test_get_sync_spng_survey_spng_survey_question(
	db: AsyncSession,
) -> None:
	# --

	spng_survey_in = SpngSurveyBaseSchemaCreate(
		type='other',
	)

	spng_survey = await db.run_sync(
		spng_survey_base_crud.create_sync,
		obj_in=spng_survey_in,
	)


	spng_survey_question_in = SpngSurveyQuestionSchemaCreate()

	spng_survey_question = await db.run_sync(
		spng_survey_question_crud.create_sync,
		obj_in=spng_survey_question_in,
	)


	spng_survey_spng_survey_question_in = SpngSurveysSpngSurveyQuestionsSchemaCreate(
		spng_survey_id=spng_survey.id,
		spng_survey_question_id=spng_survey_question.id,
		included_in_db=True,
	)


	spng_survey_spng_survey_question = await db.run_sync(
		spng_surveys_spng_survey_questions_crud.create_sync,
		obj_in=spng_survey_spng_survey_question_in,
	)


	spng_survey_spng_survey_question_2 = await db.run_sync(
		spng_surveys_spng_survey_questions_crud.get_sync,
		spng_survey_id=spng_survey.id,
		spng_survey_question_id=spng_survey_question.id,
	)

	assert spng_survey_spng_survey_question_2
	assert jsonable_encoder(spng_survey_spng_survey_question_2) == jsonable_encoder(spng_survey_spng_survey_question)




@pytest.mark.asyncio
async def test_update_spng_survey_spng_survey_question(
	db: AsyncSession,
) -> None:
	# --

	spng_survey_in = SpngSurveyBaseSchemaCreate(
		type='other',
	)

	spng_survey = await spng_survey_base_crud.create(
		db=db,
		obj_in=spng_survey_in,
	)


	spng_survey_question_in = SpngSurveyQuestionSchemaCreate()

	spng_survey_question = await spng_survey_question_crud.create(
		db=db,
		obj_in=spng_survey_question_in,
	)


	spng_survey_spng_survey_question_in = SpngSurveysSpngSurveyQuestionsSchemaCreate(
		spng_survey_id=spng_survey.id,
		spng_survey_question_id=spng_survey_question.id,
		included_in_db=True,
	)


	spng_survey_spng_survey_question = await spng_surveys_spng_survey_questions_crud.create(
		db=db,
		obj_in=spng_survey_spng_survey_question_in,
	)

	new_included_in_db = False

	spng_survey_spng_survey_question_in_update = SpngSurveysSpngSurveyQuestionsSchemaUpdate(
		included_in_db=new_included_in_db,
	)

	spng_survey_spng_survey_question_2 = await spng_surveys_spng_survey_questions_crud.update(
		db=db,
		db_obj=spng_survey_spng_survey_question,
		obj_in=spng_survey_spng_survey_question_in_update,
	)

	assert spng_survey_spng_survey_question_2
	assert spng_survey_spng_survey_question_2.included_in_db is not None
	assert spng_survey_spng_survey_question_2.included_in_db == new_included_in_db




@pytest.mark.asyncio
async def test_update_sync_spng_survey_spng_survey_question(
	db: AsyncSession,
) -> None:
	# --

	spng_survey_in = SpngSurveyBaseSchemaCreate(
		type='other',
	)

	spng_survey = await db.run_sync(
		spng_survey_base_crud.create_sync,
		obj_in=spng_survey_in,
	)


	spng_survey_question_in = SpngSurveyQuestionSchemaCreate()

	spng_survey_question = await db.run_sync(
		spng_survey_question_crud.create_sync,
		obj_in=spng_survey_question_in,
	)


	spng_survey_spng_survey_question_in = SpngSurveysSpngSurveyQuestionsSchemaCreate(
		spng_survey_id=spng_survey.id,
		spng_survey_question_id=spng_survey_question.id,
		included_in_db=True,
	)


	spng_survey_spng_survey_question = await db.run_sync(
		spng_surveys_spng_survey_questions_crud.create_sync,
		obj_in=spng_survey_spng_survey_question_in,
	)

	new_included_in_db = False

	spng_survey_spng_survey_question_in_update = SpngSurveysSpngSurveyQuestionsSchemaUpdate(
		included_in_db=new_included_in_db,
	)

	spng_survey_spng_survey_question_2 = await db.run_sync(
		spng_surveys_spng_survey_questions_crud.update_sync,
		db_obj=spng_survey_spng_survey_question,
		obj_in=spng_survey_spng_survey_question_in_update,
	)

	assert spng_survey_spng_survey_question_2
	assert spng_survey_spng_survey_question_2.included_in_db is not None
	assert spng_survey_spng_survey_question_2.included_in_db == new_included_in_db




@pytest.mark.asyncio
async def test_delete_spng_survey_spng_survey_question(
	db: AsyncSession,
) -> None:
	# --

	spng_survey_in = SpngSurveyBaseSchemaCreate(
		type='other',
	)

	spng_survey = await spng_survey_base_crud.create(
		db=db,
		obj_in=spng_survey_in,
	)


	spng_survey_question_in = SpngSurveyQuestionSchemaCreate()

	spng_survey_question = await spng_survey_question_crud.create(
		db=db,
		obj_in=spng_survey_question_in,
	)


	spng_survey_spng_survey_question_in = SpngSurveysSpngSurveyQuestionsSchemaCreate(
		spng_survey_id=spng_survey.id,
		spng_survey_question_id=spng_survey_question.id,
		included_in_db=True,
	)


	spng_survey_spng_survey_question = await spng_surveys_spng_survey_questions_crud.create(
		db=db,
		obj_in=spng_survey_spng_survey_question_in,
	)

	spng_survey_spng_survey_question_2 = await spng_surveys_spng_survey_questions_crud.delete(
		db=db,
		spng_survey_id=spng_survey.id,
		spng_survey_question_id=spng_survey_question.id,
	)

	spng_survey_spng_survey_question_3 = await spng_surveys_spng_survey_questions_crud.get(
		db=db,
		spng_survey_id=spng_survey.id,
		spng_survey_question_id=spng_survey_question.id,
	)


	assert spng_survey_spng_survey_question_3 is None
	assert spng_survey_spng_survey_question_2.spng_survey_id == spng_survey_spng_survey_question.spng_survey_id
	assert spng_survey_spng_survey_question_2.spng_survey_question_id == spng_survey_spng_survey_question.spng_survey_question_id



@pytest.mark.asyncio
async def test_delete_sync_spng_survey_spng_survey_question(
	db: AsyncSession,
) -> None:
	# --

	spng_survey_in = SpngSurveyBaseSchemaCreate(
		type='other',
	)

	spng_survey = await db.run_sync(
		spng_survey_base_crud.create_sync,
		obj_in=spng_survey_in,
	)


	spng_survey_question_in = SpngSurveyQuestionSchemaCreate()

	spng_survey_question = await db.run_sync(
		spng_survey_question_crud.create_sync,
		obj_in=spng_survey_question_in,
	)


	spng_survey_spng_survey_question_in = SpngSurveysSpngSurveyQuestionsSchemaCreate(
		spng_survey_id=spng_survey.id,
		spng_survey_question_id=spng_survey_question.id,
		included_in_db=True,
	)


	spng_survey_spng_survey_question = await db.run_sync(
		spng_surveys_spng_survey_questions_crud.create_sync,
		obj_in=spng_survey_spng_survey_question_in,
	)


	spng_survey_spng_survey_question_2 = await db.run_sync(
		spng_surveys_spng_survey_questions_crud.delete_sync,
		spng_survey_id=spng_survey.id,
		spng_survey_question_id=spng_survey_question.id,
	)

	spng_survey_spng_survey_question_3 = await db.run_sync(
		spng_surveys_spng_survey_questions_crud.get_sync,
		spng_survey_id=spng_survey.id,
		spng_survey_question_id=spng_survey_question.id,
	)


	assert spng_survey_spng_survey_question_3 is None
	assert spng_survey_spng_survey_question_2.spng_survey_id == spng_survey_spng_survey_question.spng_survey_id
	assert spng_survey_spng_survey_question_2.spng_survey_question_id == spng_survey_spng_survey_question.spng_survey_question_id



