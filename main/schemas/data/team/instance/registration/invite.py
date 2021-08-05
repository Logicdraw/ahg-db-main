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



class TeamInstanceRegistrationInviteSchemaBase(
	RegistrationInviteBaseSchemaBase,
	BaseModel,
):
	team_instance_id: Optional[int] = None
	team_instance_registration_id: Optional[int] = None



class TeamInstanceRegistrationInviteSchemaCreate(
	RegistrationInviteBaseSchemaCreate,
	TeamInstanceRegistrationInviteSchemaBase,
):
	# team_instance_id: int
	pass



class TeamInstanceRegistrationInviteSchemaUpdate(
	RegistrationInviteBaseSchemaUpdate,
	TeamInstanceRegistrationInviteSchemaBase,
):
	pass



class TeamInstanceRegistrationInviteSchemaInDBBase(
	RegistrationInviteBaseSchemaInDBBase,
	TeamInstanceRegistrationInviteSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class TeamInstanceRegistrationInviteSchema(
	RegistrationInviteBaseSchema,
	TeamInstanceRegistrationInviteSchemaInDBBase,
):
	pass



class TeamInstanceRegistrationInviteSchemaInDB(
	RegistrationInviteBaseSchemaInDB,
	TeamInstanceRegistrationInviteSchemaInDBBase,
):
	pass




