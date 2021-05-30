from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamSchemaBase(BaseModel):
	name: Optional[str] = None
	city: Optional[str] = None
	province: Optional[str] = None
	gender: Optional[str] = None
	division_id: Optional[int] = None
	league_id: Optional[int] = None
	season_id: Optional[int] = None



class TeamSchemaCreate(TeamSchemaBase):
	pass



class TeamSchemaUpdate(TeamSchemaBase):
	pass



class TeamSchemaInDBBase(TeamSchemaBase):
	id: int

	class Config:
		orm_mode = True



class TeamSchema(TeamSchemaInDBBase):
	pass



class TeamSchemaInDB(TeamSchemaInDBBase):
	pass


