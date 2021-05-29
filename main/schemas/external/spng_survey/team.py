from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)


from main.schemas._base.spng_survey import (
	SpngSurveyBaseSchemaBase,
	SpngSurveyBaseSchemaCreate,
	SpngSurveyBaseSchemaUpdate,
	SpngSurveyBaseSchemaInDBBase,
	SpngSurveyBaseSchema,
	SpngSurveyBaseSchemaInDB,
)




class SpngSurveyTeamSchemaBase(
	SpngSurveyBaseSchemaBase,
):
	pass



class SpngSurveyTeamSchemaCreate(
	SpngSurveyTeamSchemaBase,
	SpngSurveyBaseSchemaCreate,
):
	pass



class SpngSurveyTeamSchemaUpdate(
	SpngSurveyTeamSchemaBase,
	SpngSurveyBaseSchemaUpdate,
):
	pass



class SpngSurveyTeamSchemaInDBBase(
	SpngSurveyTeamSchemaBase,
	SpngSurveyBaseSchemaInDBBase,
):
	id: int

	class Config:
		orm_mode = True



class SpngSurveyTeamSchema(
	SpngSurveyTeamSchemaInDBBase,
	SpngSurveyBaseSchema,
):
	pass



class SpngSurveyTeamSchemaInDB(
	SpngSurveyTeamSchemaInDBBase,
	SpngSurveyBaseSchemaInDB,
):
	pass





