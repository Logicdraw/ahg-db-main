from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class AdultRepSchemaBase(BaseModel):
	full_name: Optional[str] = None
	email: Optional[EmailStr] = None
	user_id: Optional[int] = None



class AdultRepSchemaCreate(AdultRepSchemaBase):
	pass



class AdultRepSchemaUpdate(AdultRepSchemaBase):
	pass



class AdultRepSchemaInDBBase(AdultRepSchemaBase):
	id: int

	class Config:
		orm_mode = True



class AdultRepSchema(AdultRepSchemaInDBBase):
	pass



class AdultRepSchemaInDB(AdultRepSchemaInDBBase):
	pass


