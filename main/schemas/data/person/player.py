from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class PlayerSchemaBase(BaseModel):
	pass



class PlayerSchemaCreate(PlayerSchemaBase):
	pass



class PlayerSchemaUpdate(PlayerSchemaBase):
	pass



class PlayerSchemaInDBBase(PlayerSchemaBase):
	id: int

	class Config:
		orm_mode = True



class PlayerSchema(PlayerSchemaInDBBase):
	pass



class PlayerSchemaInDB(PlayerSchemaInDBBase):
	pass


