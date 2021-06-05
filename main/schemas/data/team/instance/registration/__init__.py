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




class TeamInstanceRegistrationSchemaBase(
	RegistrationBaseSchemaBase,
	SpngRegistrationBaseSchema,
	SpngRegistrationFinancialsBaseSchema,
	PlayerRegistrationBaseSchema,
):
	team_instance_id: Optional[int] = None
	spng_survey_team_id: Optional[int] = None
	needs_jersey: Optional[bool] = None
	needs_socks: Optional[bool] = None



class TeamInstanceRegistrationSchemaCreate(
	TeamInstanceRegistrationSchemaBase,
):
	pass



class TeamInstanceRegistrationSchemaUpdate(
	TeamInstanceRegistrationSchemaBase,
):
	pass



class TeamInstanceRegistrationSchemaInDBBase(
	TeamInstanceRegistrationSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class TeamInstanceRegistrationSchema(
	TeamInstanceRegistrationSchemaInDBBase,
):
	pass



class TeamInstanceRegistrationSchemaInDB(
	TeamInstanceRegistrationSchemaInDBBase,
):
	pass




