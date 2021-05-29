from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class SpngSurveyQuestionSchemaBase(BaseModel):
	pass



class SpngSurveyQuestionSchemaCreate(SpngSurveyQuestionSchemaBase):
	pass



class SpngSurveyQuestionSchemaUpdate(SpngSurveyQuestionSchemaBase):
	pass



class SpngSurveyQuestionSchemaInDBBase(SpngSurveyQuestionSchemaBase):
	id: int

	class Config:
		orm_mode = True



class SpngSurveyQuestionSchema(SpngSurveyQuestionSchemaInDBBase):
	pass



class SpngSurveyQuestionSchemaInDB(SpngSurveyQuestionSchemaInDBBase):
	pass


