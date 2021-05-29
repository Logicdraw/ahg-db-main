from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class GuardianSchemaBase(BaseModel):
	pass



class GuardianSchemaCreate(GuardianSchemaBase):
	pass



class GuardianSchemaUpdate(GuardianSchemaBase):
	pass



class GuardianSchemaInDBBase(GuardianSchemaBase):
	id: int

	class Config:
		orm_mode = True



class GuardianSchema(GuardianSchemaInDBBase):
	pass



class GuardianSchemaInDB(GuardianSchemaInDBBase):
	pass


