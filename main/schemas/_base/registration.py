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
	se_survey_id: Optional[int] = None
	se_survey_result_id: Optional[int] = None
	spng_persona_id: Optional[int] = None
	spng_user_id: Optional[int] = None
	roster_player_id: Optional[int] = None
	status: Optional[str] = None
	completed: Optional[bool] = None
	registration_sport: Optional[str] = None
	registration_type: Optional[str] = None
	registrant_type: Optional[str] = None
	extra_question_answers: Optional[Any] = None



class SpngRegistrationFinancialsMixinSchema(BaseModel):
	gross: Optional[float] = None
	net: Optional[float] = None
	service_fee: Optional[float] = None
	gross_forecast: Optional[float] = None
	net_forecast: Optional[float] = None
	service_fee_forecast: Optional[float] = None
	gross_outstanding: Optional[float] = None
	order_number: Optional[str] = None
	discounts: Optional[float] = None
	refunds: Optional[str] = None




class PlayerRegistrationMixinSchema(BaseModel):
	position: Optional[str] = None
	registration_insurance: Optional[bool] = None
	player_submitted_notes: Optional[str] = None







