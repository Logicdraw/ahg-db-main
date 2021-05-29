from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class ConferenceSchemaBase(BaseModel):
	pass



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


