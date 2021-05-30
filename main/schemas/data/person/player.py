from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)


import datetime



class PlayerSchemaBase(BaseModel):
	first_name: Optional[str] = None
	last_name: Optional[str] = None
	date_of_birth: Optional[datetime.date] = None
	medicare_number: Optional[str] = None
	street_address_1: Optional[str] = None
	street_address_2: Optional[str] = None
	postal_code: Optional[str] = None
	city: Optional[str] = None
	province: Optional[str] = None
	country: Optional[str] = None
	gender: Optional[str] = None
	language: Optional[str] = None
	se_persona_id: Optional[int] = None


class PlayerSchemaCreate(PlayerSchemaBase):
	pass



class PlayerSchemaUpdate(PlayerSchemaBase):
	pass



class PlayerSchemaInDBBase(PlayerSchemaBase):
	id: int

	class Config:
		orm_mode = True



class PlayerSchema(PlayerSchemaInDBBase):
	# full_name: Optional[str] = None
	pass



class PlayerSchemaInDB(PlayerSchemaInDBBase):
	pass


