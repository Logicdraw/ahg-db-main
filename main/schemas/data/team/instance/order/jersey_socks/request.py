from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstanceJerseySocksOrderRequestSchemaBase(
	BaseModel,
):
	team_instance_id: Optional[int] = None
	team_instance_registration_id: Optional[int] = None
	team_instance_jersey_socks_order_id: Optional[int] = None
	player_full_name: Optional[str] = None
	jersey_number: Optional[int] = None
	jersey_size: Optional[str] = None
	socks_size: Optional[str] = None
	details: Optional[str] = None
	approved: Optional[bool] = None
	rejected: Optional[bool] = None
	rejected_reason: Optional[str] = None



class TeamInstanceJerseySocksOrderRequestSchemaCreate(
	TeamInstanceJerseySocksOrderRequestSchemaBase,
):
	pass



class TeamInstanceJerseySocksOrderRequestSchemaUpdate(
	TeamInstanceJerseySocksOrderRequestSchemaBase,
):
	pass



class TeamInstanceJerseySocksOrderRequestSchemaInDBBase(
	TeamInstanceJerseySocksOrderRequestSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class TeamInstanceJerseySocksOrderRequestSchema(
	TeamInstanceJerseySocksOrderRequestSchemaInDBBase,
):
	pass



class TeamInstanceJerseySocksOrderRequestSchemaInDB(
	TeamInstanceJerseySocksOrderRequestSchemaInDBBase,
):
	pass


