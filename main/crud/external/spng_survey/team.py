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


from app.crud.base import CRUDBase

from app.models.data.external.spng_survey_team import SpngSurveyTeamModel

from app.schemas.data.external.spng_survey_team import (
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





