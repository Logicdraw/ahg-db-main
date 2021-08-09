from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)


from main.schemas._base.registration import (
	SpngRegistrationMixinSchema,
	SpngRegistrationFinancialsMixinSchema,
	RegistrationFinancialsMixinSchema,
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




class TeamInstanceRegistrationSchemaBase(
	RegistrationBaseSchemaBase,
	SpngRegistrationMixinSchema,
	SpngRegistrationFinancialsMixinSchema,
	RegistrationFinancialsMixinSchema,
	PlayerRegistrationMixinSchema,
):
	spng_survey_team_instance_id: Optional[int] = None
	needs_jersey: Optional[bool] = None
	needs_socks: Optional[bool] = None



class TeamInstanceRegistrationSchemaCreate(
	RegistrationBaseSchemaCreate,
	TeamInstanceRegistrationSchemaBase,
):
	pass



class TeamInstanceRegistrationSchemaUpdate(
	RegistrationBaseSchemaUpdate,
	TeamInstanceRegistrationSchemaBase,
):
	pass



class TeamInstanceRegistrationSchemaInDBBase(
	RegistrationBaseSchemaInDBBase,
	TeamInstanceRegistrationSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class TeamInstanceRegistrationSchema(
	RegistrationBaseSchema,
	TeamInstanceRegistrationSchemaInDBBase,
):
	pass



class TeamInstanceRegistrationSchemaInDB(
	RegistrationBaseSchemaInDB,
	TeamInstanceRegistrationSchemaInDBBase,
):
	pass




