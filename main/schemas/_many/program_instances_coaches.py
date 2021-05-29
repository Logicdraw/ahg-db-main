from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class ProgramInstancesCoachesSchemaBase(BaseModel):
	pass



class ProgramInstancesCoachesSchemaCreate(ProgramInstancesCoachesSchemaBase):
	pass



class ProgramInstancesCoachesSchemaUpdate(ProgramInstancesCoachesSchemaBase):
	pass



class ProgramInstancesCoachesSchemaInDBBase(ProgramInstancesCoachesSchemaBase):
	id: int

	class Config:
		orm_mode = True



class ProgramInstancesCoachesSchema(ProgramInstancesCoachesSchemaInDBBase):
	pass



class ProgramInstancesCoachesSchemaInDB(ProgramInstancesCoachesSchemaInDBBase):
	pass


