from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class SeasonInstanceSchemaBase(BaseModel):
	year_start: Optional[int] = None
	year_end: Optional[int] = None
	season_id: Optional[int] = None



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


