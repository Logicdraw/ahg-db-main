from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class CampSchemaBase(BaseModel):
	name: Optional[str] = None



class CampSchemaCreate(CampSchemaBase):
	pass



class CampSchemaUpdate(CampSchemaBase):
	pass



class CampSchemaInDBBase(CampSchemaBase):
	id: int

	class Config:
		orm_mode = True



class CampSchema(CampSchemaInDBBase):
	pass



class CampSchemaInDB(CampSchemaInDBBase):
	pass


