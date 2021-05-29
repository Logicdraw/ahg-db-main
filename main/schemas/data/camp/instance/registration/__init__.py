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




class CampInstanceRegistrationSchemaBase(
	BaseModel,
	SpngRegistrationBaseSchema,
	SpngRegistrationFinancialsBaseSchema,
	PlayerRegistrationBaseSchema,
):
	pass



class CampInstanceRegistrationSchemaCreate(CampInstanceRegistrationSchemaBase):
	pass



class CampInstanceRegistrationSchemaUpdate(CampInstanceRegistrationSchemaBase):
	pass



class CampInstanceRegistrationSchemaInDBBase(CampInstanceRegistrationSchemaBase):
	id: int

	class Config:
		orm_mode = True



class CampInstanceRegistrationSchema(CampInstanceRegistrationSchemaInDBBase):
	pass



class CampInstanceRegistrationSchemaInDB(CampInstanceRegistrationSchemaInDBBase):
	pass



