from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstanceTracksuitOrderSchemaBase(
	BaseModel,
):
	team_instance_id: Optional[int] = None
	coach_full_name: Optional[str] = None
	jacket_size: Optional[str] = None
	pants_size: Optional[str] = None



class TeamInstanceTracksuitOrderSchemaCreate(
	TeamInstanceTracksuitOrderSchemaBase,
):
	pass



class TeamInstanceTracksuitOrderSchemaUpdate(
	TeamInstanceTracksuitOrderSchemaBase,
):
	pass



class TeamInstanceTracksuitOrderSchemaInDBBase(
	TeamInstanceTracksuitOrderSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class TeamInstanceTracksuitOrderSchema(
	TeamInstanceTracksuitOrderSchemaInDBBase,
):
	pass



class TeamInstanceTracksuitOrderSchemaInDB(
	TeamInstanceTracksuitOrderSchemaInDBBase,
):
	pass


