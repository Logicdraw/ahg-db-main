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




class SpngSurveyTeamInstanceSchemaBase(
	SpngSurveyBaseSchemaBase,
):
	# default_team_instance_id: Optional[int] = None
	pass



class SpngSurveyTeamInstanceSchemaCreate(
	SpngSurveyTeamInstanceSchemaBase,
	SpngSurveyBaseSchemaCreate,
):
	type: str = 'team_instance'



class SpngSurveyTeamInstanceSchemaUpdate(
	SpngSurveyTeamInstanceSchemaBase,
	SpngSurveyBaseSchemaUpdate,
):
	pass



class SpngSurveyTeamInstanceSchemaInDBBase(
	SpngSurveyTeamInstanceSchemaBase,
	SpngSurveyBaseSchemaInDBBase,
):
	id: int

	class Config:
		orm_mode = True



class SpngSurveyTeamInstanceSchema(
	SpngSurveyTeamInstanceSchemaInDBBase,
	SpngSurveyBaseSchema,
):
	pass



class SpngSurveyTeamInstanceSchemaInDB(
	SpngSurveyTeamInstanceSchemaInDBBase,
	SpngSurveyBaseSchemaInDB,
):
	pass





