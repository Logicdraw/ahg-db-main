from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstanceJerseySocksOrderRequestSchemaBase(
	BaseModel,
):
	pass



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


