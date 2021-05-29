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




class TeamInstanceRegistrationSchemaBase(
	BaseModel,
	SpngRegistrationBaseSchema,
	SpngRegistrationFinancialsBaseSchema,
	PlayerRegistrationBaseSchema,
):
	pass



class TeamInstanceRegistrationSchemaCreate(TeamInstanceRegistrationSchemaBase):
	pass



class TeamInstanceRegistrationSchemaUpdate(TeamInstanceRegistrationSchemaBase):
	pass



class TeamInstanceRegistrationSchemaInDBBase(TeamInstanceRegistrationSchemaBase):
	id: int

	class Config:
		orm_mode = True



class TeamInstanceRegistrationSchema(TeamInstanceRegistrationSchemaInDBBase):
	pass



class TeamInstanceRegistrationSchemaInDB(TeamInstanceRegistrationSchemaInDBBase):
	pass




