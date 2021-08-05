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



class CampInstanceRegistrationInviteSchemaBase(
	RegistrationInviteBaseSchemaBase,
	BaseModel,
):
	camp_instance_id: Optional[int] = None
	camp_instance_registration_id: Optional[int] = None



class CampInstanceRegistrationInviteSchemaCreate(
	RegistrationInviteBaseSchemaCreate,
	CampInstanceRegistrationInviteSchemaBase,
):
	# camp_instance_id: int
	pass



class CampInstanceRegistrationInviteSchemaUpdate(
	RegistrationInviteBaseSchemaUpdate,
	CampInstanceRegistrationInviteSchemaBase,
):
	pass



class CampInstanceRegistrationInviteSchemaInDBBase(
	RegistrationInviteBaseSchemaInDBBase,
	CampInstanceRegistrationInviteSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class CampInstanceRegistrationInviteSchema(
	RegistrationInviteBaseSchema,
	CampInstanceRegistrationInviteSchemaInDBBase,
):
	pass



class CampInstanceRegistrationInviteSchemaInDB(
	RegistrationInviteBaseSchemaInDB,
	CampInstanceRegistrationInviteSchemaInDBBase,
):
	pass




