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




class CampInstanceRegistrationSchemaBase(
	RegistrationBaseSchemaBase,
	SpngRegistrationBaseSchema,
	SpngRegistrationFinancialsBaseSchema,
	PlayerRegistrationBaseSchema,
):
	pass



class CampInstanceRegistrationSchemaCreate(
	CampInstanceRegistrationSchemaBase,
	RegistrationBaseSchemaCreate,
):
	pass



class CampInstanceRegistrationSchemaUpdate(
	CampInstanceRegistrationSchemaBase,
	RegistrationBaseSchemaUpdate,
):
	pass



class CampInstanceRegistrationSchemaInDBBase(
	CampInstanceRegistrationSchemaBase,
	RegistrationBaseSchemaInDBBase,
):
	id: int

	class Config:
		orm_mode = True



class CampInstanceRegistrationSchema(
	CampInstanceRegistrationSchemaInDBBas,
	RegistrationBaseSchema,
):
	pass



class CampInstanceRegistrationSchemaInDB(
	CampInstanceRegistrationSchemaInDBBase,
	RegistrationBaseSchemaInDB,
):
	pass




