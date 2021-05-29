from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstanceJerseySocksOrderSchemaBase(BaseModel):
	pass



class TeamInstanceJerseySocksOrderSchemaCreate(TeamInstanceJerseySocksOrderSchemaBase):
	pass



class TeamInstanceJerseySocksOrderSchemaUpdate(TeamInstanceJerseySocksOrderSchemaBase):
	pass



class TeamInstanceJerseySocksOrderSchemaInDBBase(TeamInstanceJerseySocksOrderSchemaBase):
	id: int

	class Config:
		orm_mode = True



class TeamInstanceJerseySocksOrderSchema(TeamInstanceJerseySocksOrderSchemaInDBBase):
	pass



class TeamInstanceJerseySocksOrderSchemaInDB(TeamInstanceJerseySocksOrderSchemaInDBBase):
	pass


