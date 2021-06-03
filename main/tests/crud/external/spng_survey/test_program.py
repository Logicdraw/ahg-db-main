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

	pass



@pytest.mark.asyncio
async def test_create_sync_spng_survey_program(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_get_spng_survey_program(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_get_sync_spng_survey_program(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_update_spng_survey_program(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_update_sync_spng_survey_program(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_delete_spng_survey_program(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_delete_sync_spng_survey_program(
	db: AsyncSession,
) -> None:
	# --

	pass





