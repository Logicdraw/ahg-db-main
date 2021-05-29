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




class ProgramInstanceRegistrationSchemaBase(
	BaseModel,
	SpngRegistrationBaseSchema,
	SpngRegistrationFinancialsBaseSchema,
	PlayerRegistrationBaseSchema,
):
	pass



class ProgramInstanceRegistrationSchemaCreate(ProgramInstanceRegistrationSchemaBase):
	pass



class ProgramInstanceRegistrationSchemaUpdate(ProgramInstanceRegistrationSchemaBase):
	pass



class ProgramInstanceRegistrationSchemaInDBBase(ProgramInstanceRegistrationSchemaBase):
	id: int

	class Config:
		orm_mode = True



class ProgramInstanceRegistrationSchema(ProgramInstanceRegistrationSchemaInDBBase):
	pass



class ProgramInstanceRegistrationSchemaInDB(ProgramInstanceRegistrationSchemaInDBBase):
	pass



