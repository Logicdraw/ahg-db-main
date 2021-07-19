from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class ProgramGroupInstanceSchemaBase(BaseModel):
	program_instance_id: Optional[int] = None
	program_group_id: Optional[int] = None
	year_start: Optional[int] = None
	year_end: Optional[int] = None



class ProgramGroupInstanceSchemaCreate(
	ProgramGroupInstanceSchemaBase,
):
	pass



class ProgramGroupInstanceSchemaUpdate(
	ProgramGroupInstanceSchemaBase,
):
	pass



class ProgramGroupInstanceSchemaInDBBase(
	ProgramGroupInstanceSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class ProgramGroupInstanceSchema(
	ProgramGroupInstanceSchemaInDBBase,
):
	pass



class ProgramGroupInstanceSchemaInDB(
	ProgramGroupInstanceSchemaInDBBase,
):
	pass


