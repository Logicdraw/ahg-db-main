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

from main.models.external.spng_survey.program_instance import SpngSurveyProgramInstanceModel

from main.schemas.external.spng_survey.program_instance import (
	SpngSurveyProgramInstanceSchemaCreate,
	SpngSurveyProgramInstanceSchemaUpdate,
)



class CRUDSpngSurveyProgramInstance(
	CRUDBase[
		SpngSurveyProgramInstanceModel,
		SpngSurveyProgramInstanceSchemaCreate,
		SpngSurveyProgramInstanceSchemaUpdate,
	]):
	pass






spng_survey_program_instance_crud = CRUDSpngSurveyProgramInstance(SpngSurveyProgramInstanceModel)





