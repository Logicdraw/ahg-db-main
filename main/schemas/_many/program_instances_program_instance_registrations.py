from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class ProgramInstancesProgramInstanceRegistrationsSchemaBase(
	BaseModel,
):
	program_instance_id: Optional[int] = None
	program_instance_registration_id: Optional[int] = None



class ProgramInstancesProgramInstanceRegistrationsSchemaCreate(
	ProgramInstancesProgramInstanceRegistrationsSchemaBase,
):
	program_instance_id: int
	program_instance_registration_id: int



class ProgramInstancesProgramInstanceRegistrationsSchemaUpdate(
	ProgramInstancesProgramInstanceRegistrationsSchemaBase,
):
	pass



class ProgramInstancesProgramInstanceRegistrationsSchemaInDBBase(
	ProgramInstancesProgramInstanceRegistrationsSchemaBase,
):

	class Config:
		orm_mode = True



class ProgramInstancesProgramInstanceRegistrationsSchema(
	ProgramInstancesProgramInstanceRegistrationsSchemaInDBBase,
):
	pass



class ProgramInstancesProgramInstanceRegistrationsSchemaInDB(
	ProgramInstancesProgramInstanceRegistrationsSchemaInDBBase,
):
	pass


