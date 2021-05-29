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

from app.models.data.external.spng_survey_program import SpngSurveyProgramModel

from app.schemas.data.external.spng_survey_program import (
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





