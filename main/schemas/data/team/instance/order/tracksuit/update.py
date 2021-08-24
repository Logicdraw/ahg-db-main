from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstanceTracksuitOrderUpdateSchemaBase(
	BaseModel,
):
	team_instance_tracksuit_order_id: Optional[int] = None
	old_coach_full_name: Optional[str] = None
	old_jacket_size: Optional[str] = None
	old_pants_size: Optional[str] = None
	new_coach_full_name: Optional[str] = None
	new_jacket_size: Optional[str] = None
	new_pants_size: Optional[str] = None



class TeamInstanceTracksuitOrderUpdateSchemaCreate(
	TeamInstanceTracksuitOrderUpdateSchemaBase,
):
	pass



class TeamInstanceTracksuitOrderUpdateSchemaUpdate(
	TeamInstanceTracksuitOrderUpdateSchemaBase,
):
	pass



class TeamInstanceTracksuitOrderUpdateSchemaInDBBase(
	TeamInstanceTracksuitOrderUpdateSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class TeamInstanceTracksuitOrderUpdateSchema(
	TeamInstanceTracksuitOrderUpdateSchemaInDBBase,
):
	pass



class TeamInstanceTracksuitOrderUpdateSchemaInDB(
	TeamInstanceTracksuitOrderUpdateSchemaInDBBase,
):
	pass


