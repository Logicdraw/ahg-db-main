from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class CampGroupInstanceSchemaBase(
	BaseModel,
):
	camp_instance_id: Optional[int] = None
	camp_group_id: Optional[int] = None
	year_end: Optional[int] = None
	year_start: Optional[int] = None



class CampGroupInstanceSchemaCreate(
	CampGroupInstanceSchemaBase,
):
	pass



class CampGroupInstanceSchemaUpdate(
	CampGroupInstanceSchemaBase,
):
	pass



class CampGroupInstanceSchemaInDBBase(
	CampGroupInstanceSchemaBase,
):
	id: int

	class Config:
		orm_mode = True



class CampGroupInstanceSchema(
	CampGroupInstanceSchemaInDBBase,
):
	pass



class CampGroupInstanceSchemaInDB(
	CampGroupInstanceSchemaInDBBase,
):
	pass


