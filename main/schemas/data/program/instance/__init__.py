from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class ProgramInstanceSchemaBase(BaseModel):
	program_id: Optional[int] = None
	year_end: Optional[int] = None
	year_start: Optional[int] = None
	se_name_snake: Optional[str] = None
	se_shared_question_id: Optional[int] = None



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


