from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class DivisionSchemaBase(BaseModel):
	pass



class DivisionSchemaCreate(DivisionSchemaBase):
	pass



class DivisionSchemaUpdate(DivisionSchemaBase):
	pass



class DivisionSchemaInDBBase(DivisionSchemaBase):
	id: int

	class Config:
		orm_mode = True



class DivisionSchema(DivisionSchemaInDBBase):
	pass



class DivisionSchemaInDB(DivisionSchemaInDBBase):
	pass


