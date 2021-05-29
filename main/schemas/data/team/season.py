from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class SeasonSchemaBase(BaseModel):
	pass



class SeasonSchemaCreate(SeasonSchemaBase):
	pass



class SeasonSchemaUpdate(SeasonSchemaBase):
	pass



class SeasonSchemaInDBBase(SeasonSchemaBase):
	id: int

	class Config:
		orm_mode = True



class SeasonSchema(SeasonSchemaInDBBase):
	pass



class SeasonSchemaInDB(SeasonSchemaInDBBase):
	pass


