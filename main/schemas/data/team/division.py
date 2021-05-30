from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class DivisionSchemaBase(BaseModel):
	name: Optional[str] = None
	season_id: Optional[int] = None
	league_id: Optional[int] = None
	conference_id: Optional[int] = None



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


