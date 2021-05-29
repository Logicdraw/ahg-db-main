from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class LeagueInstanceSchemaBase(BaseModel):
	pass



class LeagueInstanceSchemaCreate(LeagueInstanceSchemaBase):
	pass



class LeagueInstanceSchemaUpdate(LeagueInstanceSchemaBase):
	pass



class LeagueInstanceSchemaInDBBase(LeagueInstanceSchemaBase):
	id: int

	class Config:
		orm_mode = True



class LeagueInstanceSchema(LeagueInstanceSchemaInDBBase):
	pass



class LeagueInstanceSchemaInDB(LeagueInstanceSchemaInDBBase):
	pass


