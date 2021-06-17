from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstancesAdultRepsSchemaBase(BaseModel):
	team_instance_id: Optional[int] = None
	adult_rep_id: Optional[int] = None
	role: Optional[str] = None



class TeamInstancesAdultRepsSchemaCreate(TeamInstancesAdultRepsSchemaBase):
	team_instance_id: int
	adult_rep_id: int



class TeamInstancesAdultRepsSchemaUpdate(TeamInstancesAdultRepsSchemaBase):
	pass



class TeamInstancesAdultRepsSchemaInDBBase(TeamInstancesAdultRepsSchemaBase):

	class Config:
		orm_mode = True



class TeamInstancesAdultRepsSchema(TeamInstancesAdultRepsSchemaInDBBase):
	pass



class TeamInstancesAdultRepsSchemaInDB(TeamInstancesAdultRepsSchemaInDBBase):
	pass


