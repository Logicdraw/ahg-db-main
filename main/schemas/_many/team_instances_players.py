from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstancesPlayersSchemaBase(BaseModel):
	pass



class TeamInstancesPlayersSchemaCreate(TeamInstancesPlayersSchemaBase):
	pass



class TeamInstancesPlayersSchemaUpdate(TeamInstancesPlayersSchemaBase):
	pass



class TeamInstancesPlayersSchemaInDBBase(TeamInstancesPlayersSchemaBase):
	id: int

	class Config:
		orm_mode = True



class TeamInstancesPlayersSchema(TeamInstancesPlayersSchemaInDBBase):
	pass



class TeamInstancesPlayersSchemaInDB(TeamInstancesPlayersSchemaInDBBase):
	pass


