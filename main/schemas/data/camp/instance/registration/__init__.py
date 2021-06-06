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
)




class CampInstanceRegistrationSchemaBase(
	RegistrationBaseSchemaBase,
	SpngRegistrationBaseSchema,
	SpngRegistrationFinancialsBaseSchema,
	PlayerRegistrationBaseSchema,
):
	camp_instance_id: Optional[int] = None
	camp_group_instance_id: Optional[int] = None
	spng_survey_camp_id: Optional[int] = None



class CampInstanceRegistrationSchemaCreate(
	CampInstanceRegistrationSchemaBase,
):
	pass



class CampInstanceRegistrationSchemaUpdate(
	CampInstanceRegistrationSchemaBase,
):
	pass



class CampInstanceRegistrationSchemaInDBBase(
	CampInstanceRegistrationSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class CampInstanceRegistrationSchema(
	CampInstanceRegistrationSchemaInDBBase,
):
	pass



class CampInstanceRegistrationSchemaInDB(
	CampInstanceRegistrationSchemaInDBBase,
):
	pass




