from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class SpngSurveysSpngSurveyQuestionsSchemaBase(BaseModel):
	pass



class SpngSurveysSpngSurveyQuestionsSchemaCreate(SpngSurveysSpngSurveyQuestionsSchemaBase):
	pass



class SpngSurveysSpngSurveyQuestionsSchemaUpdate(SpngSurveysSpngSurveyQuestionsSchemaBase):
	pass



class SpngSurveysSpngSurveyQuestionsSchemaInDBBase(SpngSurveysSpngSurveyQuestionsSchemaBase):
	id: int

	class Config:
		orm_mode = True



class SpngSurveysSpngSurveyQuestionsSchema(SpngSurveysSpngSurveyQuestionsSchemaInDBBase):
	pass



class SpngSurveysSpngSurveyQuestionsSchemaInDB(SpngSurveysSpngSurveyQuestionsSchemaInDBBase):
	pass


