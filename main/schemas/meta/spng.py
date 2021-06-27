from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)


import datetime



class SpngMetaSchemaBase(BaseModel):
	last_fetched_registrations: Optional[datetime.datetime] = None



class SpngMetaSchemaCreate(SpngMetaSchemaBase):
	access_token: Optional[str] = None
	refresh_token: Optional[str] = None



class SpngMetaSchemaUpdate(SpngMetaSchemaBase):
	access_token: Optional[str] = None
	refresh_token: Optional[str] = None



class SpngMetaSchemaInDBBase(SpngMetaSchemaBase):
	id: int

	class Config:
		orm_mode = True



class SpngMetaSchema(SpngMetaSchemaInDBBase):
	access_token_encoded: Optional[str] = None
	refresh_token_encoded: Optional[str] = None



class SpngMetaSchemaInDB(SpngMetaSchemaInDBBase):
	pass


