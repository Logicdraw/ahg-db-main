from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)


import datetime


class FormSchemaBase(BaseModel):
	slug: Optional[str] = None
	title: Optional[str] = None
	description: Optional[str] = None
	has_deadline: Optional[bool] = None
	deadline_on: Optional[datetime.datetime] = None
	is_live: Optional[bool] = None



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


