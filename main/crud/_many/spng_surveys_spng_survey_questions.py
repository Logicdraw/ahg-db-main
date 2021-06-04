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

	async def get(
		self,
		db: AsyncSession,
		spng_survey_id: int,
		spng_survey_question_id: int,
	) -> Optional[SpngSurveysSpngSurveyQuestionsModel]:
		# --

		result = await db.execute(
			select(SpngSurveysSpngSurveyQuestionsModel).\
			filter_by(
				spng_survey_id=spng_survey_id,
				spng_survey_question_id=spng_survey_question_id,
			)
		)

		return result.scalars().first()




spng_surveys_spng_survey_questions_crud = CRUDSpngSurveysSpngSurveyQuestions(SpngSurveysSpngSurveyQuestionsModel)



