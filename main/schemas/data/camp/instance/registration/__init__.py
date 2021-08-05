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




class CampInstanceRegistrationSchemaBase(
	RegistrationBaseSchemaBase,
	SpngRegistrationMixinSchema,
	SpngRegistrationFinancialsMixinSchema,
	PlayerRegistrationMixinSchema,
):
	camp_instance_id: Optional[int] = None
	camp_group_instance_id: Optional[int] = None
	spng_survey_camp_id: Optional[int] = None



class CampInstanceRegistrationSchemaCreate(
	RegistrationBaseSchemaCreate,
	CampInstanceRegistrationSchemaBase,
):
	pass



class CampInstanceRegistrationSchemaUpdate(
	RegistrationBaseSchemaUpdate,
	CampInstanceRegistrationSchemaBase,
):
	pass



class CampInstanceRegistrationSchemaInDBBase(
	RegistrationBaseSchemaInDBBase,
	CampInstanceRegistrationSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class CampInstanceRegistrationSchema(
	RegistrationBaseSchema,
	CampInstanceRegistrationSchemaInDBBase,
):
	pass



class CampInstanceRegistrationSchemaInDB(
	RegistrationBaseSchemaInDB,
	CampInstanceRegistrationSchemaInDBBase,
):
	pass




