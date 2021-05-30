from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstancesPlayersSchemaBase(BaseModel):
	team_instance_id: Optional[int] = None
	player_id: Optional[int] = None
	comment: Optional[str] = None
	position: Optional[str] = None
	sponsors: Optional[str] = None



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


