from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstanceJerseySponsorOrderUpdateSchemaBase(
	BaseModel,
):
	team_instance_jersey_sponsor_order_id: Optional[int] = None
	old_player_full_name: Optional[str] = None
	old_name: Optional[str] = None
	old_amount: Optional[float] = None
	new_player_full_name: Optional[str] = None
	new_name: Optional[str] = None
	new_amount: Optional[float] = None



class TeamInstanceJerseySponsorOrderUpdateSchemaCreate(
	TeamInstanceJerseySponsorOrderUpdateSchemaBase,
):
	pass



class TeamInstanceJerseySponsorOrderUpdateSchemaUpdate(
	TeamInstanceJerseySponsorOrderUpdateSchemaBase,
):
	pass



class TeamInstanceJerseySponsorOrderUpdateSchemaInDBBase(
	TeamInstanceJerseySponsorOrderUpdateSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class TeamInstanceJerseySponsorOrderUpdateSchema(
	TeamInstanceJerseySponsorOrderUpdateSchemaInDBBase,
):
	pass



class TeamInstanceJerseySponsorOrderUpdateSchemaInDB(
	TeamInstanceJerseySponsorOrderUpdateSchemaInDBBase,
):
	pass


