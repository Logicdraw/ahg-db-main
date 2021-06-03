from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


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
async def test_create_spng_survey_question(
	db: AsyncSession,
) -> None:
	# --
	use_answer_text_mappings = True
	shared_question_ids = {
		'Apple Pie': 'apple_pie',
		'Cheese Cake': 'cheese_cake',
	}
	answer_text_mappings = random_lower_string()

	spng_survey_question_in = SpngSurveyQuestionSchemaCreate(
		use_answer_text_mappings=use_answer_text_mappings,
		shared_question_ids=shared_question_ids,
		answer_text_mappings=answer_text_mappings,
	)

	spng_survey_question = await spng_survey_question_crud.create(
		db=db,
		obj_in=spng_survey_question_in,
	)


	assert spng_survey_question.use_answer_text_mappings == use_answer_text_mappings
	assert spng_survey_question.shared_question_ids == shared_question_ids
	assert spng_survey_question.answer_text_mappings == answer_text_mappings



@pytest.mark.asyncio
async def test_create_sync_spng_survey_question(
	db: AsyncSession,
) -> None:
	# --
	use_answer_text_mappings = True
	shared_question_ids = {
		'Apple Pie': 'apple_pie',
		'Cheese Cake': 'cheese_cake',
	}
	answer_text_mappings = random_lower_string()

	spng_survey_question_in = SpngSurveyQuestionSchemaCreate(
		use_answer_text_mappings=use_answer_text_mappings,
		shared_question_ids=shared_question_ids,
		answer_text_mappings=answer_text_mappings,
	)

	spng_survey_question = await db.run_sync(
		spng_survey_question_crud.create_sync,
		obj_in=spng_survey_question_in,
	)


	assert spng_survey_question.use_answer_text_mappings == use_answer_text_mappings
	assert spng_survey_question.shared_question_ids == shared_question_ids
	assert spng_survey_question.answer_text_mappings == answer_text_mappings



@pytest.mark.asyncio
async def test_get_spng_survey_question(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_get_sync_spng_survey_question(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_update_spng_survey_question(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_update_sync_spng_survey_question(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_delete_spng_survey_question(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_delete_sync_spng_survey_question(
	db: AsyncSession,
) -> None:
	# --

	pass





