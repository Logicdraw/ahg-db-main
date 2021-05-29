from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstancesCoachesSchemaBase(BaseModel):
	pass



class TeamInstancesCoachesSchemaCreate(TeamInstancesCoachesSchemaBase):
	pass



class TeamInstancesCoachesSchemaUpdate(TeamInstancesCoachesSchemaBase):
	pass



class TeamInstancesCoachesSchemaInDBBase(TeamInstancesCoachesSchemaBase):
	id: int

	class Config:
		orm_mode = True



class TeamInstancesCoachesSchema(TeamInstancesCoachesSchemaInDBBase):
	pass



class TeamInstancesCoachesSchemaInDB(TeamInstancesCoachesSchemaInDBBase):
	pass


