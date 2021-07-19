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

from main.models.external.spng_survey.team_instance import SpngSurveyTeamInstanceModel

from main.schemas.external.spng_survey.team_instance import (
	SpngSurveyTeamInstanceSchemaCreate,
	SpngSurveyTeamInstanceSchemaUpdate,
)



class CRUDSpngSurveyTeamInstance(
	CRUDBase[
		SpngSurveyTeamInstanceModel,
		SpngSurveyTeamInstanceSchemaCreate,
		SpngSurveyTeamInstanceSchemaUpdate,
	]):

	pass






spng_survey_team_instance_crud = CRUDSpngSurveyTeamInstance(SpngSurveyTeamInstanceModel)





