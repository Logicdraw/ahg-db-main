from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class CoachSchemaBase(BaseModel):
	full_name: Optional[str] = None
	email: Optional[EmailStr] = None
	user_id: Optional[int] = None



class CoachSchemaCreate(CoachSchemaBase):
	pass



class CoachSchemaUpdate(CoachSchemaBase):
	pass



class CoachSchemaInDBBase(CoachSchemaBase):
	id: int

	class Config:
		orm_mode = True



class CoachSchema(CoachSchemaInDBBase):
	pass



class CoachSchemaInDB(CoachSchemaInDBBase):
	pass


