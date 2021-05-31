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

from main.models.external.spng_survey.program import SpngSurveyProgramModel

from main.schemas.external.spng_survey.program import (
	SpngSurveyProgramSchemaCreate,
	SpngSurveyProgramSchemaUpdate,
)



class CRUDSpngSurveyProgram(
	CRUDBase[
		SpngSurveyProgramModel,
		SpngSurveyProgramSchemaCreate,
		SpngSurveyProgramSchemaUpdate,
	]):
	pass






spng_survey_program_crud = CRUDSpngSurveyProgram(SpngSurveyProgramModel)





