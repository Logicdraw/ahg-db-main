from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class CampGroupInstanceSchemaBase(BaseModel):
	pass



class CampGroupInstanceSchemaCreate(CampGroupInstanceSchemaBase):
	pass



class CampGroupInstanceSchemaUpdate(CampGroupInstanceSchemaBase):
	pass



class CampGroupInstanceSchemaInDBBase(CampGroupInstanceSchemaBase):
	id: int

	class Config:
		orm_mode = True



class CampGroupInstanceSchema(CampGroupInstanceSchemaInDBBase):
	pass



class CampGroupInstanceSchemaInDB(CampGroupInstanceSchemaInDBBase):
	pass


