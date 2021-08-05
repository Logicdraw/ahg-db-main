from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstanceJerseySocksOrderUpdateSchemaBase(
	BaseModel,
):
	team_instance_jersey_socks_order_id: Optional[int] = None
	new_player_full_name: Optional[str] = None
	new_jersey_number: Optional[int] = None
	new_jersey_size: Optional[str] = None
	new_socks_size: Optional[str] = None



class TeamInstanceJerseySocksOrderUpdateSchemaCreate(
	TeamInstanceJerseySocksOrderUpdateSchemaBase,
):
	pass



class TeamInstanceJerseySocksOrderUpdateSchemaUpdate(
	TeamInstanceJerseySocksOrderUpdateSchemaBase,
):
	pass



class TeamInstanceJerseySocksOrderUpdateSchemaInDBBase(
	TeamInstanceJerseySocksOrderUpdateSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class TeamInstanceJerseySocksOrderUpdateSchema(
	TeamInstanceJerseySocksOrderUpdateSchemaInDBBase,
):
	pass



class TeamInstanceJerseySocksOrderUpdateSchemaInDB(
	TeamInstanceJerseySocksOrderUpdateSchemaInDBBase,
):
	pass


