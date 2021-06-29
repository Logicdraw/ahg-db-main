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
	ProgramInstanceRegistrationSchemaBase,
):
	pass



class ProgramInstanceRegistrationSchemaUpdate(
	ProgramInstanceRegistrationSchemaBase,
):
	pass



class ProgramInstanceRegistrationSchemaInDBBase(
	ProgramInstanceRegistrationSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class ProgramInstanceRegistrationSchema(
	ProgramInstanceRegistrationSchemaInDBBase,
):
	pass



class ProgramInstanceRegistrationSchemaInDB(
	ProgramInstanceRegistrationSchemaInDBBase,
):
	pass




