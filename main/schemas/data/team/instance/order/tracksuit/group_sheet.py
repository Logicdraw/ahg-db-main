from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstanceTracksuitOrderGroupSheetSchemaBase(
	BaseModel,
):
	uuid: Optional[str] = None
	team_instance_id: Optional[int] = None



class TeamInstanceTracksuitOrderGroupSheetSchemaCreate(
	TeamInstanceTracksuitOrderGroupSheetSchemaBase,
):
	pass



class TeamInstanceTracksuitOrderGroupSheetSchemaUpdate(
	TeamInstanceTracksuitOrderGroupSheetSchemaBase,
):
	pass



class TeamInstanceTracksuitOrderGroupSheetSchemaInDBBase(
	TeamInstanceTracksuitOrderGroupSheetSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class TeamInstanceTracksuitOrderGroupSheetSchema(
	TeamInstanceTracksuitOrderGroupSheetSchemaInDBBase,
):
	pass



class TeamInstanceTracksuitOrderGroupSheetSchemaInDB(
	TeamInstanceTracksuitOrderGroupSheetSchemaInDBBase,
):
	pass


