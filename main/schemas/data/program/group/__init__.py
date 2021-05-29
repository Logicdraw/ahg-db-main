from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class ProgramGroupSchemaBase(BaseModel):
	pass



class ProgramGroupSchemaCreate(ProgramGroupSchemaBase):
	pass



class ProgramGroupSchemaUpdate(ProgramGroupSchemaBase):
	pass



class ProgramGroupSchemaInDBBase(ProgramGroupSchemaBase):
	id: int

	class Config:
		orm_mode = True



class ProgramGroupSchema(ProgramGroupSchemaInDBBase):
	pass



class ProgramGroupSchemaInDB(ProgramGroupSchemaInDBBase):
	pass


