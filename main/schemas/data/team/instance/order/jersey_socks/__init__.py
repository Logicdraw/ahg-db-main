from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstanceJerseySocksOrderSchemaBase(
	BaseModel,
):
	team_instance_id: Optional[int] = None
	team_instance_registration_id: Optional[int] = None
	player_full_name: Optional[str] = None
	jersey_number: Optional[int] = None
	jersey_size: Optional[str] = None
	socks_size: Optional[str] = None



class TeamInstanceJerseySocksOrderSchemaCreate(
	TeamInstanceJerseySocksOrderSchemaBase,
):
	pass



class TeamInstanceJerseySocksOrderSchemaUpdate(
	TeamInstanceJerseySocksOrderSchemaBase,
):
	pass



class TeamInstanceJerseySocksOrderSchemaInDBBase(
	TeamInstanceJerseySocksOrderSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class TeamInstanceJerseySocksOrderSchema(
	TeamInstanceJerseySocksOrderSchemaInDBBase,
):
	pass



class TeamInstanceJerseySocksOrderSchemaInDB(
	TeamInstanceJerseySocksOrderSchemaInDBBase,
):
	pass


