from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class ProgramInstanceSchemaBase(BaseModel):
	pass



class ProgramInstanceSchemaCreate(ProgramInstanceSchemaBase):
	pass



class ProgramInstanceSchemaUpdate(ProgramInstanceSchemaBase):
	pass



class ProgramInstanceSchemaInDBBase(ProgramInstanceSchemaBase):
	id: int

	class Config:
		orm_mode = True



class ProgramInstanceSchema(ProgramInstanceSchemaInDBBase):
	pass



class ProgramInstanceSchemaInDB(ProgramInstanceSchemaInDBBase):
	pass


