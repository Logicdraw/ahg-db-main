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
	pass



@pytest.mark.asyncio
async def test_get_spng_survey_base(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_update_spng_survey_base(
	db: AsyncSession,
) -> None:
	pass



@pytest.mark.asyncio
async def test_delete_spng_survey_base(
	db: AsyncSession,
) -> None:
	pass





