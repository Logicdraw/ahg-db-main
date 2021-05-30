from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class ConferenceInstanceSchemaBase(BaseModel):
	year_start: Optional[int] = None
	year_end: Optional[int] = None
	conference_id: Optional[int] = None
	league_instance_id: Optional[int] = None
	season_instance_id: Optional[int] = None



class ConferenceInstanceSchemaCreate(ConferenceInstanceSchemaBase):
	pass



class ConferenceInstanceSchemaUpdate(ConferenceInstanceSchemaBase):
	pass



class ConferenceInstanceSchemaInDBBase(ConferenceInstanceSchemaBase):
	id: int

	class Config:
		orm_mode = True



class ConferenceInstanceSchema(ConferenceInstanceSchemaInDBBase):
	pass



class ConferenceInstanceSchemaInDB(ConferenceInstanceSchemaInDBBase):
	pass


