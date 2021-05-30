from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class LeagueInstanceSchemaBase(BaseModel):
	year_end: Optional[int] = None
	year_start: Optional[int] = None
	league_id: Optional[int] = None
	season_instance_id: Optional[int] = None


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


