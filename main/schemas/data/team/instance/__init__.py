from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstanceSchemaBase(BaseModel):
	pass



class TeamInstanceSchemaCreate(TeamInstanceSchemaBase):
	pass



class TeamInstanceSchemaUpdate(TeamInstanceSchemaBase):
	pass



class TeamInstanceSchemaInDBBase(TeamInstanceSchemaBase):
	id: int

	class Config:
		orm_mode = True



class TeamInstanceSchema(TeamInstanceSchemaInDBBase):
	pass



class TeamInstanceSchemaInDB(TeamInstanceSchemaInDBBase):
	pass


