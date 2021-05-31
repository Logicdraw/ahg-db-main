from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.external.spng_survey.camp import (
	spng_survey_camp_crud,
)

from main.schemas.external.spng_survey.camp import (
	SpngSurveyCampSchemaCreate,
	SpngSurveyCampSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)



def test_create_spng_survey_camp(
	db: AsyncSession,
) -> None:
	pass



def test_get_spng_survey_camp(
	db: AsyncSession,
) -> None:
	pass



def test_update_spng_survey_camp(
	db: AsyncSession,
) -> None:
	pass



def test_delete_spng_survey_camp(
	db: AsyncSession,
) -> None:
	pass





