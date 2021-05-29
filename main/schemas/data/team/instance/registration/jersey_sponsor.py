from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class TeamInstanceRegistrationJerseySponsorSchemaBase(BaseModel):
	pass



class TeamInstanceRegistrationJerseySponsorSchemaCreate(TeamInstanceRegistrationJerseySponsorSchemaBase):
	pass



class TeamInstanceRegistrationJerseySponsorSchemaUpdate(TeamInstanceRegistrationJerseySponsorSchemaBase):
	pass



class TeamInstanceRegistrationJerseySponsorSchemaInDBBase(TeamInstanceRegistrationJerseySponsorSchemaBase):
	id: int

	class Config:
		orm_mode = True



class TeamInstanceRegistrationJerseySponsorSchema(TeamInstanceRegistrationJerseySponsorSchemaInDBBase):
	pass



class TeamInstanceRegistrationJerseySponsorSchemaInDB(TeamInstanceRegistrationJerseySponsorSchemaInDBBase):
	pass


