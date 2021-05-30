from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class ProgramSchemaBase(BaseModel):
	name: Optional[str] = None



class ProgramSchemaCreate(ProgramSchemaBase):
	pass



class ProgramSchemaUpdate(ProgramSchemaBase):
	pass



class ProgramSchemaInDBBase(ProgramSchemaBase):
	id: int

	class Config:
		orm_mode = True



class ProgramSchema(ProgramSchemaInDBBase):
	pass



class ProgramSchemaInDB(ProgramSchemaInDBBase):
	pass


