from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class DivisionInstanceSchemaBase(BaseModel):
	year_start: Optional[int] = None
	year_end: Optional[int] = None
	division_id: Optional[int] = None
	season_instance_id: Optional[int] = None
	league_instance_id: Optional[int] = None
	conference_instance_id: Optional[int] = None



class DivisionInstanceSchemaCreate(DivisionInstanceSchemaBase):
	pass



class DivisionInstanceSchemaUpdate(DivisionInstanceSchemaBase):
	pass



class DivisionInstanceSchemaInDBBase(DivisionInstanceSchemaBase):
	id: int

	class Config:
		orm_mode = True



class DivisionInstanceSchema(DivisionInstanceSchemaInDBBase):
	pass



class DivisionInstanceSchemaInDB(DivisionInstanceSchemaInDBBase):
	pass


