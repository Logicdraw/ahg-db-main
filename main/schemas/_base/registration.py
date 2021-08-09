from typing import (
	Optional,
	Any,
)

from pydantic import (
	BaseModel,
	EmailStr,
)



import datetime




class RegistrationBaseSchemaBase(BaseModel):
	placed_at_datetime: Optional[datetime.datetime] = None
	comment: Optional[str] = None
	coaches_comment: Optional[str] = None
	notes: Optional[str] = None
	player_id: Optional[int] = None




class SpngRegistrationMixinSchema(BaseModel):
	spng_survey_id: Optional[int] = None
	spng_survey_result_id: Optional[int] = None
	spng_persona_id: Optional[int] = None
	spng_user_id: Optional[int] = None
	roster_player_id: Optional[int] = None
	status: Optional[str] = None
	completed: Optional[bool] = None
	registration_sport: Optional[str] = None
	registration_type: Optional[str] = None
	registrant_type: Optional[str] = None
	extra_question_answers: Optional[Any] = None



class RegistrationFinancialsMixinSchema(BaseModel):
	total: Optional[float] = None
	paid: Optional[float] = None
	owes: Optional[float] = None
	discounts: Optional[float] = None
	discount_names: Optional[str] = None
	refunds: Optional[float] = None
	refund_reason: Optional[str] = None


class SpngRegistrationFinancialsMixinSchema(BaseModel):
	spng_order_number: Optional[str] = None



class PlayerRegistrationMixinSchema(BaseModel):
	position: Optional[str] = None
	registration_insurance: Optional[bool] = None
	player_submitted_notes: Optional[str] = None





class RegistrationBaseSchemaCreate(
	RegistrationBaseSchemaBase,
):
	pass



class RegistrationBaseSchemaUpdate(
	RegistrationBaseSchemaBase,
):
	pass



class RegistrationBaseSchemaInDBBase(
	RegistrationBaseSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class RegistrationBaseSchema(
	RegistrationBaseSchemaInDBBase,
):
	pass



class RegistrationBaseSchemaInDB(
	RegistrationBaseSchemaInDBBase,
):
	pass





