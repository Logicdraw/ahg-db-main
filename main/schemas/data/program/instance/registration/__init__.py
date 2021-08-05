from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)


from main.schemas._base.registration import (
	SpngRegistrationMixinSchema,
	SpngRegistrationFinancialsMixinSchema,
	PlayerRegistrationMixinSchema,
)


from main.schemas._base.registration import (
	RegistrationBaseSchemaBase,
	RegistrationBaseSchemaCreate,
	RegistrationBaseSchemaUpdate,
	RegistrationBaseSchemaInDBBase,
	RegistrationBaseSchema,
	RegistrationBaseSchemaInDB,
)




class ProgramInstanceRegistrationSchemaBase(
	RegistrationBaseSchemaBase,
	SpngRegistrationMixinSchema,
	SpngRegistrationFinancialsMixinSchema,
	PlayerRegistrationMixinSchema,
):
	program_instance_id: Optional[int] = None
	program_group_instance_id: Optional[int] = None
	spng_survey_program_id: Optional[int] = None



class ProgramInstanceRegistrationSchemaCreate(
	RegistrationBaseSchemaCreate,
	ProgramInstanceRegistrationSchemaBase,
):
	pass



class ProgramInstanceRegistrationSchemaUpdate(
	RegistrationBaseSchemaUpdate,
	ProgramInstanceRegistrationSchemaBase,
):
	pass



class ProgramInstanceRegistrationSchemaInDBBase(
	RegistrationBaseSchemaInDBBase,
	ProgramInstanceRegistrationSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class ProgramInstanceRegistrationSchema(
	RegistrationBaseSchema,
	ProgramInstanceRegistrationSchemaInDBBase,
):
	pass



class ProgramInstanceRegistrationSchemaInDB(
	RegistrationBaseSchemaInDB,
	ProgramInstanceRegistrationSchemaInDBBase,
):
	pass




