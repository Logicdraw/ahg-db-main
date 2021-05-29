from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class ConferenceInstanceSchemaBase(BaseModel):
	pass



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


