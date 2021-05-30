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
	camp_instance_id: Optional[int] = None
	camp_instance_group_id: Optional[int] = None
	spng_survey_camp_id: Optional[int] = None



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




