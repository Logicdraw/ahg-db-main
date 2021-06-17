from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class SpngSurveyBaseSchemaBase(BaseModel):
	survey_id: Optional[int] = None
	name: Optional[str] = None
	is_active: Optional[bool] = None
	type: Optional[str] = None

	# relationship -- /



class SpngSurveyBaseSchemaCreate(SpngSurveyBaseSchemaBase):
	type: str



class SpngSurveyBaseSchemaUpdate(SpngSurveyBaseSchemaBase):
	pass



class SpngSurveyBaseSchemaInDBBase(SpngSurveyBaseSchemaBase):
	id: int

	class Config:
		orm_mode = True



class SpngSurveyBaseSchema(SpngSurveyBaseSchemaInDBBase):
	pass



class SpngSurveyBaseSchemaInDB(SpngSurveyBaseSchemaInDBBase):
	pass


