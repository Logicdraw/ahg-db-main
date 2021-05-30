from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class SpngSurveysSpngSurveyQuestionsSchemaBase(BaseModel):
	spng_survey_id: Optional[int] = None
	spng_survey_question_id: Optional[int] = None
	included_in_db: Optional[bool] = None



class SpngSurveysSpngSurveyQuestionsSchemaCreate(SpngSurveysSpngSurveyQuestionsSchemaBase):
	pass



class SpngSurveysSpngSurveyQuestionsSchemaUpdate(SpngSurveysSpngSurveyQuestionsSchemaBase):
	pass



class SpngSurveysSpngSurveyQuestionsSchemaInDBBase(SpngSurveysSpngSurveyQuestionsSchemaBase):

	class Config:
		orm_mode = True



class SpngSurveysSpngSurveyQuestionsSchema(SpngSurveysSpngSurveyQuestionsSchemaInDBBase):
	pass



class SpngSurveysSpngSurveyQuestionsSchemaInDB(SpngSurveysSpngSurveyQuestionsSchemaInDBBase):
	pass


