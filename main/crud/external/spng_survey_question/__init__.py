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

from main.models.external.spng_survey_question import SpngSurveyQuestionModel

from main.schemas.external.spng_survey_question import (
	SpngSurveyQuestionSchemaCreate,
	SpngSurveyQuestionSchemaUpdate,
)



class CRUDSpngSurveyQuestion(
	CRUDBase[
		SpngSurveyQuestionModel,
		SpngSurveyQuestionSchemaCreate,
		SpngSurveyQuestionSchemaUpdate,
	]):
	pass





spng_survey_question_crud = CRUDSpngSurveyQuestion(SpngSurveyQuestionModel)





