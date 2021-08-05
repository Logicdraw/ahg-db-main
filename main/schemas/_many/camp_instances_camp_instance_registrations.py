from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class CampInstancesCampInstanceRegistrationsSchemaBase(
	BaseModel,
):
	camp_instance_id: Optional[int] = None
	camp_instance_registration_id: Optional[int] = None



class CampInstancesCampInstanceRegistrationsSchemaCreate(
	CampInstancesCampInstanceRegistrationsSchemaBase,
):
	camp_instance_id: int
	camp_instance_registration_id: int



class CampInstancesCampInstanceRegistrationsSchemaUpdate(
	CampInstancesCampInstanceRegistrationsSchemaBase,
):
	pass



class CampInstancesCampInstanceRegistrationsSchemaInDBBase(
	CampInstancesCampInstanceRegistrationsSchemaBase,
):

	class Config:
		orm_mode = True



class CampInstancesCampInstanceRegistrationsSchema(
	CampInstancesCampInstanceRegistrationsSchemaInDBBase,
):
	pass



class CampInstancesCampInstanceRegistrationsSchemaInDB(
	CampInstancesCampInstanceRegistrationsSchemaInDBBase,
):
	pass


