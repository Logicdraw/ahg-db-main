from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class SpngSurveyTeamSchemaBase(BaseModel):
	pass



class SpngSurveyTeamSchemaCreate(SpngSurveyTeamSchemaBase):
	pass



class SpngSurveyTeamSchemaUpdate(SpngSurveyTeamSchemaBase):
	pass



class SpngSurveyTeamSchemaInDBBase(SpngSurveyTeamSchemaBase):
	id: int

	class Config:
		orm_mode = True



class SpngSurveyTeamSchema(SpngSurveyTeamSchemaInDBBase):
	pass



class SpngSurveyTeamSchemaInDB(SpngSurveyTeamSchemaInDBBase):
	pass


