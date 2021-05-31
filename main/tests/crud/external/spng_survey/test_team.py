from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.external.spng_survey.team import (
	spng_survey_team_crud,
)

from main.schemas.external.spng_survey.team import (
	SpngSurveyTeamSchemaCreate,
	SpngSurveyTeamSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)



def test_create_spng_survey_team(
	db: AsyncSession,
) -> None:
	pass



def test_get_spng_survey_team(
	db: AsyncSession,
) -> None:
	pass



def test_update_spng_survey_team(
	db: AsyncSession,
) -> None:
	pass



def test_delete_spng_survey_team(
	db: AsyncSession,
) -> None:
	pass





