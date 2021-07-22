from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstanceJerseySocksOrderGroupSheetSchemaBase(
	BaseModel,
):
	pass



class TeamInstanceJerseySocksOrderGroupSheetSchemaCreate(
	TeamInstanceJerseySocksOrderGroupSheetSchemaBase,
):
	pass



class TeamInstanceJerseySocksOrderGroupSheetSchemaUpdate(
	TeamInstanceJerseySocksOrderGroupSheetSchemaBase,
):
	pass



class TeamInstanceJerseySocksOrderGroupSheetSchemaInDBBase(
	TeamInstanceJerseySocksOrderGroupSheetSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class TeamInstanceJerseySocksOrderGroupSheetSchema(
	TeamInstanceJerseySocksOrderGroupSheetSchemaInDBBase,
):
	pass



class TeamInstanceJerseySocksOrderGroupSheetSchemaInDB(
	TeamInstanceJerseySocksOrderGroupSheetSchemaInDBBase,
):
	pass


