from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstanceJerseySponsorOrderSchemaBase(
	BaseModel,
):
	team_instance_id: Optional[int] = None
	player_full_name: Optional[str] = None
	name: Optional[str] = None
	amount: Optional[float] = None



class TeamInstanceJerseySponsorOrderSchemaCreate(
	TeamInstanceJerseySponsorOrderSchemaBase,
):
	pass



class TeamInstanceJerseySponsorOrderSchemaUpdate(
	TeamInstanceJerseySponsorOrderSchemaBase,
):
	pass



class TeamInstanceJerseySponsorOrderSchemaInDBBase(
	TeamInstanceJerseySponsorOrderSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class TeamInstanceJerseySponsorOrderSchema(
	TeamInstanceJerseySponsorOrderSchemaInDBBase,
):
	pass



class TeamInstanceJerseySponsorOrderSchemaInDB(
	TeamInstanceJerseySponsorOrderSchemaInDBBase,
):
	pass


