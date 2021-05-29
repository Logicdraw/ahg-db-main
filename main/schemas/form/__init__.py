from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class FormSchemaBase(BaseModel):
	pass



class FormSchemaCreate(FormSchemaBase):
	pass



class FormSchemaUpdate(FormSchemaBase):
	pass



class FormSchemaInDBBase(FormSchemaBase):
	id: int

	class Config:
		orm_mode = True



class FormSchema(FormSchemaInDBBase):
	pass



class FormSchemaInDB(FormSchemaInDBBase):
	pass


