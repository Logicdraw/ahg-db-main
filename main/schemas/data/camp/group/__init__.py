from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)




class CampGroupSchemaBase(BaseModel):
	name: Optional[str] = None
	camp_id: Optional[int] = None



class CampGroupSchemaCreate(CampGroupSchemaBase):
	pass



class CampGroupSchemaUpdate(CampGroupSchemaBase):
	pass



class CampGroupSchemaInDBBase(CampGroupSchemaBase):
	id: int

	class Config:
		orm_mode = True



class CampGroupSchema(CampGroupSchemaInDBBase):
	pass



class CampGroupSchemaInDB(CampGroupSchemaInDBBase):
	pass


