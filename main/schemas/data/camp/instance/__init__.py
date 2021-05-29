from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class CampInstanceSchemaBase(BaseModel):
	pass



class CampInstanceSchemaCreate(CampInstanceSchemaBase):
	pass



class CampInstanceSchemaUpdate(CampInstanceSchemaBase):
	pass



class CampInstanceSchemaInDBBase(CampInstanceSchemaBase):
	id: int

	class Config:
		orm_mode = True



class CampInstanceSchema(CampInstanceSchemaInDBBase):
	pass



class CampInstanceSchemaInDB(CampInstanceSchemaInDBBase):
	pass


