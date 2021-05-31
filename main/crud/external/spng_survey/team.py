from typing import (
	Any,
	Dict,
	Optional,
	Union,
	List,
)


from sqlalchemy.ext.asyncio import AsyncSession


from sqlalchemy import (
	func,
	or_,
)


from main.crud.base import CRUDBase

from main.models.external.spng_survey.team import SpngSurveyTeamModel

from main.schemas.external.spng_survey.team import (
	SpngSurveyTeamSchemaCreate,
	SpngSurveyTeamSchemaUpdate,
)



class CRUDSpngSurveyTeam(
	CRUDBase[
		SpngSurveyTeamModel,
		SpngSurveyTeamSchemaCreate,
		SpngSurveyTeamSchemaUpdate,
	]):
	pass






spng_survey_team_crud = CRUDSpngSurveyTeam(SpngSurveyTeamModel)





