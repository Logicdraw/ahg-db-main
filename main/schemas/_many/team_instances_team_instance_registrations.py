from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstancesTeamInstanceRegistrationsSchemaBase(
	BaseModel,
):
	team_instance_id: Optional[int] = None
	team_instance_registration_id: Optional[int] = None



class TeamInstancesTeamInstanceRegistrationsSchemaCreate(
	TeamInstancesTeamInstanceRegistrationsSchemaBase,
):
	team_instance_id: int
	team_instance_registration_id: int



class TeamInstancesTeamInstanceRegistrationsSchemaUpdate(
	TeamInstancesTeamInstanceRegistrationsSchemaBase,
):
	pass



class TeamInstancesTeamInstanceRegistrationsSchemaInDBBase(
	TeamInstancesTeamInstanceRegistrationsSchemaBase,
):

	class Config:
		orm_mode = True



class TeamInstancesTeamInstanceRegistrationsSchema(
	TeamInstancesTeamInstanceRegistrationsSchemaInDBBase,
):
	pass



class TeamInstancesTeamInstanceRegistrationsSchemaInDB(
	TeamInstancesTeamInstanceRegistrationsSchemaInDBBase,
):
	pass


