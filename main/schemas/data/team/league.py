from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class LeagueSchemaBase(BaseModel):
	season_id: Optional[int] = None
	name: Optional[str] = None



class LeagueSchemaCreate(LeagueSchemaBase):
	pass



class LeagueSchemaUpdate(LeagueSchemaBase):
	pass



class LeagueSchemaInDBBase(LeagueSchemaBase):
	id: int

	class Config:
		orm_mode = True



class LeagueSchema(LeagueSchemaInDBBase):
	pass



class LeagueSchemaInDB(LeagueSchemaInDBBase):
	pass


