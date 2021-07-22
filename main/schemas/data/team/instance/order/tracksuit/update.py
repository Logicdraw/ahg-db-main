from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstanceTracksuitOrderUpdateSchemaBase(
	BaseModel,
):
	pass



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


