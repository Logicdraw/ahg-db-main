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




class TeamInstanceRegistrationSchemaBase(
	RegistrationBaseSchemaBase,
	SpngRegistrationBaseSchema,
	SpngRegistrationFinancialsBaseSchema,
	PlayerRegistrationBaseSchema,
):
	pass



class TeamInstanceRegistrationSchemaCreate(
	TeamInstanceRegistrationSchemaBase,
	RegistrationBaseSchemaCreate,
):
	pass



class TeamInstanceRegistrationSchemaUpdate(
	TeamInstanceRegistrationSchemaBase,
	RegistrationBaseSchemaUpdate,
):
	pass



class TeamInstanceRegistrationSchemaInDBBase(
	TeamInstanceRegistrationSchemaBase,
	RegistrationBaseSchemaInDBBase,
):
	id: int

	class Config:
		orm_mode = True



class TeamInstanceRegistrationSchema(
	TeamInstanceRegistrationSchemaInDBBas,
	RegistrationBaseSchema,
):
	pass



class TeamInstanceRegistrationSchemaInDB(
	TeamInstanceRegistrationSchemaInDBBase,
	RegistrationBaseSchemaInDB,
):
	pass




