from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)


from main.schemas._base.registration_invite import (
	RegistrationInviteBaseSchemaBase,
	RegistrationInviteBaseSchemaCreate,
	RegistrationInviteBaseSchemaUpdate,
	RegistrationInviteBaseSchemaInDBBase,
	RegistrationInviteBaseSchema,
	RegistrationInviteBaseSchemaInDB,
)



class ProgramInstanceRegistrationInviteSchemaBase(
	RegistrationInviteBaseSchemaBase,
	BaseModel,
):
	program_instance_id: Optional[int] = None
	program_instance_registration_id: Optional[int] = None



class ProgramInstanceRegistrationInviteSchemaCreate(
	RegistrationInviteBaseSchemaCreate,
	ProgramInstanceRegistrationInviteSchemaBase,
):
	# program_instance_id: int
	pass



class ProgramInstanceRegistrationInviteSchemaUpdate(
	RegistrationInviteBaseSchemaUpdate,
	ProgramInstanceRegistrationInviteSchemaBase,
):
	pass



class ProgramInstanceRegistrationInviteSchemaInDBBase(
	RegistrationInviteBaseSchemaInDBBase,
	ProgramInstanceRegistrationInviteSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class ProgramInstanceRegistrationInviteSchema(
	RegistrationInviteBaseSchema,
	ProgramInstanceRegistrationInviteSchemaInDBBase,
):
	pass



class ProgramInstanceRegistrationInviteSchemaInDB(
	RegistrationInviteBaseSchemaInDB,
	ProgramInstanceRegistrationInviteSchemaInDBBase,
):
	pass




