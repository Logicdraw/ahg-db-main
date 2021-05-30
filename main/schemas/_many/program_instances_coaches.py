from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class ProgramInstancesCoachesSchemaBase(BaseModel):
	program_instance_id: Optional[int] = None
	coach_id: Optional[int] = None
	role: Optional[str] = None



class ProgramInstancesCoachesSchemaCreate(ProgramInstancesCoachesSchemaBase):
	pass



class ProgramInstancesCoachesSchemaUpdate(ProgramInstancesCoachesSchemaBase):
	pass



class ProgramInstancesCoachesSchemaInDBBase(ProgramInstancesCoachesSchemaBase):

	class Config:
		orm_mode = True



class ProgramInstancesCoachesSchema(ProgramInstancesCoachesSchemaInDBBase):
	pass



class ProgramInstancesCoachesSchemaInDB(ProgramInstancesCoachesSchemaInDBBase):
	pass


