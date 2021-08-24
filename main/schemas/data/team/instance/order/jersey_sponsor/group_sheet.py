from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstanceJerseySponsorOrderGroupSheetSchemaBase(
	BaseModel,
):
	uuid: Optional[str] = None
	team_instance_id: Optional[int] = None



class TeamInstanceJerseySponsorOrderGroupSheetSchemaCreate(
	TeamInstanceJerseySponsorOrderGroupSheetSchemaBase,
):
	pass



class TeamInstanceJerseySponsorOrderGroupSheetSchemaUpdate(
	TeamInstanceJerseySponsorOrderGroupSheetSchemaBase,
):
	pass



class TeamInstanceJerseySponsorOrderGroupSheetSchemaInDBBase(
	TeamInstanceJerseySponsorOrderGroupSheetSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class TeamInstanceJerseySponsorOrderGroupSheetSchema(
	TeamInstanceJerseySponsorOrderGroupSheetSchemaInDBBase,
):
	pass



class TeamInstanceJerseySponsorOrderGroupSheetSchemaInDB(
	TeamInstanceJerseySponsorOrderGroupSheetSchemaInDBBase,
):
	pass


