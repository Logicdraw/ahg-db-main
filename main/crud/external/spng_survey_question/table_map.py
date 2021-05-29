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

from app.models.data.external.spng_survey_question.table_map import SpngSurveyQuestionTableMapModel

from app.schemas.data.external.spng_survey_question.table_map import (
	SpngSurveyQuestionTableMapSchemaCreate,
	SpngSurveyQuestionTableMapSchemaUpdate,
)



class CRUDSpngSurveyQuestionTableMap(
	CRUDBase[
		SpngSurveyQuestionTableMapModel,
		SpngSurveyQuestionTableMapSchemaCreate,
		SpngSurveyQuestionTableMapSchemaUpdate,
	]):
	pass





spng_survey_question_table_map_crud = CRUDSpngSurveyQuestionTableMap(SpngSurveyQuestionTableMapModel)





