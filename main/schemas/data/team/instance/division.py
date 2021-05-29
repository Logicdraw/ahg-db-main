from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class DivisionInstanceSchemaBase(BaseModel):
	pass



class DivisionInstanceSchemaCreate(DivisionInstanceSchemaBase):
	pass



class DivisionInstanceSchemaUpdate(DivisionInstanceSchemaBase):
	pass



class DivisionInstanceSchemaInDBBase(DivisionInstanceSchemaBase):
	id: int

	class Config:
		orm_mode = True



class DivisionInstanceSchema(DivisionInstanceSchemaInDBBase):
	pass



class DivisionInstanceSchemaInDB(DivisionInstanceSchemaInDBBase):
	pass


