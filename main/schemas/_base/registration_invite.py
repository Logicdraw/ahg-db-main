from typing import (
	Optional,
	Any,
)

from pydantic import (
	BaseModel,
	EmailStr,
)





class RegistrationInviteBaseSchemaBase(BaseModel):
	email_to: Optional[EmailStr] = None
	has_registered: Optional[bool] = None
	extra_question_answers: Optional[Any] = None



class RegistrationInviteBaseSchemaCreate(
	RegistrationInviteBaseSchemaBase,
):
	email_to: EmailStr



class RegistrationInviteBaseSchemaUpdate(
	RegistrationInviteBaseSchemaBase,
):
	pass



class RegistrationInviteBaseSchemaInDBBase(
	RegistrationInviteBaseSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class RegistrationInviteBaseSchema(
	RegistrationInviteBaseSchemaInDBBase,
):
	pass



class RegistrationInviteBaseSchemaInDB(
	RegistrationInviteBaseSchemaInDBBase,
):
	pass



