from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class FormEntrySchemaBase(BaseModel):
	slug: Optional[str] = None
	form_id: Optional[int] = None



class FormEntrySchemaCreate(FormEntrySchemaBase):
	pass



class FormEntrySchemaUpdate(FormEntrySchemaBase):
	pass



class FormEntrySchemaInDBBase(FormEntrySchemaBase):
	id: int

	class Config:
		orm_mode = True



class FormEntrySchema(FormEntrySchemaInDBBase):
	pass



class FormEntrySchemaInDB(FormEntrySchemaInDBBase):
	pass


