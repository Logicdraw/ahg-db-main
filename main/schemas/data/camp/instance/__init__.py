from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class CampInstanceSchemaBase(BaseModel):
	camp_id: Optional[int] = None
	year_start: Optional[int] = None
	year_end: Optional[int] = None
	se_name_snake: Optional[str] = None
	se_shared_question_id: Optional[int] = None



class CampInstanceSchemaCreate(CampInstanceSchemaBase):
	pass



class CampInstanceSchemaUpdate(CampInstanceSchemaBase):
	pass



class CampInstanceSchemaInDBBase(CampInstanceSchemaBase):
	id: int

	class Config:
		orm_mode = True



class CampInstanceSchema(CampInstanceSchemaInDBBase):
	pass



class CampInstanceSchemaInDB(CampInstanceSchemaInDBBase):
	pass



