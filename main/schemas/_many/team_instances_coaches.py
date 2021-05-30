from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstancesCoachesSchemaBase(BaseModel):
	team_instance_id: Optional[int] = None
	coach_id: Optional[int] = None
	role: Optional[str] = None



class TeamInstancesCoachesSchemaCreate(TeamInstancesCoachesSchemaBase):
	pass



class TeamInstancesCoachesSchemaUpdate(TeamInstancesCoachesSchemaBase):
	pass



class TeamInstancesCoachesSchemaInDBBase(TeamInstancesCoachesSchemaBase):

	class Config:
		orm_mode = True



class TeamInstancesCoachesSchema(TeamInstancesCoachesSchemaInDBBase):
	pass



class TeamInstancesCoachesSchemaInDB(TeamInstancesCoachesSchemaInDBBase):
	pass


