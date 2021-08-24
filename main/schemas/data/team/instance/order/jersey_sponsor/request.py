from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstanceJerseySponsorOrderRequestSchemaBase(
	BaseModel,
):
	team_instance_id: Optional[int] = None
	team_instance_jersey_sponsor_order_id: Optional[int] = None
	name: Optional[str] = None
	amount: Optional[float] = None
	details: Optional[str] = None
	approved: Optional[bool] = None
	rejected: Optional[bool] = None
	rejection_reason: Optional[str] = None



class TeamInstanceJerseySponsorOrderRequestSchemaCreate(
	TeamInstanceJerseySponsorOrderRequestSchemaBase,
):
	pass



class TeamInstanceJerseySponsorOrderRequestSchemaUpdate(
	TeamInstanceJerseySponsorOrderRequestSchemaBase,
):
	pass



class TeamInstanceJerseySponsorOrderRequestSchemaInDBBase(
	TeamInstanceJerseySponsorOrderRequestSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class TeamInstanceJerseySponsorOrderRequestSchema(
	TeamInstanceJerseySponsorOrderRequestSchemaInDBBase,
):
	pass



class TeamInstanceJerseySponsorOrderRequestSchemaInDB(
	TeamInstanceJerseySponsorOrderRequestSchemaInDBBase,
):
	pass


