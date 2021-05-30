from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class FormSchemaBase(BaseModel):
	title: Optional[str] = None
	description: Optional[str] = None
	has_deadline: Optional[bool] = None
	deadline_on: Optional[str] = None



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


