from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class SpngSurveyQuestionTableMapSchemaBase(BaseModel):
	pass



class SpngSurveyQuestionTableMapSchemaCreate(SpngSurveyQuestionTableMapSchemaBase):
	pass



class SpngSurveyQuestionTableMapSchemaUpdate(SpngSurveyQuestionTableMapSchemaBase):
	pass



class SpngSurveyQuestionTableMapSchemaInDBBase(SpngSurveyQuestionTableMapSchemaBase):
	id: int

	class Config:
		orm_mode = True



class SpngSurveyQuestionTableMapSchema(SpngSurveyQuestionTableMapSchemaInDBBase):
	pass



class SpngSurveyQuestionTableMapSchemaInDB(SpngSurveyQuestionTableMapSchemaInDBBase):
	pass


