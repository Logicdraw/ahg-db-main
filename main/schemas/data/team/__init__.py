from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamSchemaBase(BaseModel):
	pass



class TeamSchemaCreate(TeamSchemaBase):
	pass



class TeamSchemaUpdate(TeamSchemaBase):
	pass



class TeamSchemaInDBBase(TeamSchemaBase):
	id: int

	class Config:
		orm_mode = True



class TeamSchema(TeamSchemaInDBBase):
	pass



class TeamSchemaInDB(TeamSchemaInDBBase):
	pass


