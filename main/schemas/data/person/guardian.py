from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class GuardianSchemaBase(BaseModel):
	full_name: Optional[str] = None
	mobile_phone: Optional[str] = None
	home_phone: Optional[str] = None
	work_phone: Optional[str] = None
	email: Optional[EmailStr] = None
	user_id: Optional[int] = None


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


