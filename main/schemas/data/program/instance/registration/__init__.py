from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)


from main.schemas._base.registration import (
	SpngRegistrationBaseSchema,
	SpngRegistrationFinancialsBaseSchema,
	PlayerRegistrationBaseSchema,
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
	SpngRegistrationBaseSchema,
	SpngRegistrationFinancialsBaseSchema,
	PlayerRegistrationBaseSchema,
):
	program_instance_id: Optional[int] = None
	program_instance_group_id: Optional[int] = None
	spng_survey_id: Optional[int] = None



class ProgramInstanceRegistrationSchemaCreate(
	ProgramInstanceRegistrationSchemaBase,
	RegistrationBaseSchemaCreate,
):
	pass



class ProgramInstanceRegistrationSchemaUpdate(
	ProgramInstanceRegistrationSchemaBase,
	RegistrationBaseSchemaUpdate,
):
	pass



class ProgramInstanceRegistrationSchemaInDBBase(
	ProgramInstanceRegistrationSchemaBase,
	RegistrationBaseSchemaInDBBase,
):
	id: int

	class Config:
		orm_mode = True



class ProgramInstanceRegistrationSchema(
	ProgramInstanceRegistrationSchemaInDBBas,
	RegistrationBaseSchema,
):
	pass



class ProgramInstanceRegistrationSchemaInDB(
	ProgramInstanceRegistrationSchemaInDBBase,
	RegistrationBaseSchemaInDB,
):
	pass




