from typing import (
	Any,
	Dict,
	Optional,
	Union,
	List,
)


from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession


from sqlalchemy import (
	func,
	or_,
)


from main.crud.base import CRUDBase

from main.models._many.spng_surveys_spng_survey_questions import SpngSurveysSpngSurveyQuestionsModel

from main.schemas._many.spng_surveys_spng_survey_questions import (
	SpngSurveysSpngSurveyQuestionsSchemaCreate,
	SpngSurveysSpngSurveyQuestionsSchemaUpdate,
)



class CRUDSpngSurveysSpngSurveyQuestions(
	CRUDBase[
		SpngSurveysSpngSurveyQuestionsModel,
		SpngSurveysSpngSurveyQuestionsSchemaCreate,
		SpngSurveysSpngSurveyQuestionsSchemaUpdate,
	]):

	pass


spng_surveys_spng_survey_questions_crud = CRUDSpngSurveysSpngSurveyQuestions(SpngSurveysSpngSurveyQuestionsModel)



