from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class ConferenceSchemaBase(BaseModel):
	name: Optional[str] = None
	season_id: Optional[int] = None
	league_id: Optional[int] = None



class ConferenceSchemaCreate(ConferenceSchemaBase):
	pass



class ConferenceSchemaUpdate(ConferenceSchemaBase):
	pass



class ConferenceSchemaInDBBase(ConferenceSchemaBase):
	id: int

	class Config:
		orm_mode = True



class ConferenceSchema(ConferenceSchemaInDBBase):
	pass



class ConferenceSchemaInDB(ConferenceSchemaInDBBase):
	pass


