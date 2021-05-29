from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class CoachSchemaBase(BaseModel):
	pass



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


