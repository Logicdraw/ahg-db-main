from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)




class AddressSchemaBase(BaseModel):
	pass



class AddressSchemaCreate(AddressSchemaBase):
	pass



class AddressSchemaUpdate(AddressSchemaBase):
	pass



class AddressSchemaInDBBase(AddressSchemaBase):
	id: int

	class Config:
		orm_mode = True



class AddressSchema(AddressSchemaInDBBase):
	pass



class AddressSchemaInDB(AddressSchemaInDBBase):
	pass





