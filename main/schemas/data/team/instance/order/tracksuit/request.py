from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstanceTracksuitOrderRequestSchemaBase(
	BaseModel,
):
	pass



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


