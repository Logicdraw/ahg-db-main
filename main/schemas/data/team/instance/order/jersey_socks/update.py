from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstanceJerseySocksOrderUpdateSchemaBase(
	BaseModel,
):
	pass



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


