from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstanceTracksuitOrderRequestSchemaBase(
	BaseModel,
):
	team_instance_id: Optional[int] = None
	team_instance_tracksuit_order_id: Optional[int] = None
	jacket_size: Optional[str] = None
	pants_size: Optional[str] = None
	details: Optional[str] = None
	approved: Optional[bool] = None
	rejected: Optional[bool] = None
	rejected_reason: Optional[str] = None



class TeamInstanceTracksuitOrderRequestSchemaCreate(
	TeamInstanceTracksuitOrderRequestSchemaBase,
):
	pass



class TeamInstanceTracksuitOrderRequestSchemaUpdate(
	TeamInstanceTracksuitOrderRequestSchemaBase,
):
	pass



class TeamInstanceTracksuitOrderRequestSchemaInDBBase(
	TeamInstanceTracksuitOrderRequestSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class TeamInstanceTracksuitOrderRequestSchema(
	TeamInstanceTracksuitOrderRequestSchemaInDBBase,
):
	pass



class TeamInstanceTracksuitOrderRequestSchemaInDB(
	TeamInstanceTracksuitOrderRequestSchemaInDBBase,
):
	pass


