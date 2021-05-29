from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class SeasonInstanceSchemaBase(BaseModel):
	pass



class SeasonInstanceSchemaCreate(SeasonInstanceSchemaBase):
	pass



class SeasonInstanceSchemaUpdate(SeasonInstanceSchemaBase):
	pass



class SeasonInstanceSchemaInDBBase(SeasonInstanceSchemaBase):
	id: int

	class Config:
		orm_mode = True



class SeasonInstanceSchema(SeasonInstanceSchemaInDBBase):
	pass



class SeasonInstanceSchemaInDB(SeasonInstanceSchemaInDBBase):
	pass


