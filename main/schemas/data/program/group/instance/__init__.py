from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class ProgramGroupInstanceSchemaBase(BaseModel):
	pass



class ProgramGroupInstanceSchemaCreate(ProgramGroupInstanceSchemaBase):
	pass



class ProgramGroupInstanceSchemaUpdate(ProgramGroupInstanceSchemaBase):
	pass



class ProgramGroupInstanceSchemaInDBBase(ProgramGroupInstanceSchemaBase):
	id: int

	class Config:
		orm_mode = True



class ProgramGroupInstanceSchema(ProgramGroupInstanceSchemaInDBBase):
	pass



class ProgramGroupInstanceSchemaInDB(ProgramGroupInstanceSchemaInDBBase):
	pass


