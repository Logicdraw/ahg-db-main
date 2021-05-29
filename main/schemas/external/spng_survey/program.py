from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class SpngSurveyProgramSchemaBase(BaseModel):
	pass



class SpngSurveyProgramSchemaCreate(SpngSurveyProgramSchemaBase):
	pass



class SpngSurveyProgramSchemaUpdate(SpngSurveyProgramSchemaBase):
	pass



class SpngSurveyProgramSchemaInDBBase(SpngSurveyProgramSchemaBase):
	id: int

	class Config:
		orm_mode = True



class SpngSurveyProgramSchema(SpngSurveyProgramSchemaInDBBase):
	pass



class SpngSurveyProgramSchemaInDB(SpngSurveyProgramSchemaInDBBase):
	pass


