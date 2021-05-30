from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class CampInstancesCoachesSchemaBase(BaseModel):
	camp_instance_id: Optional[int] = None
	coach_id: Optional[int] = None
	role: Optional[str] = None



class CampInstancesCoachesSchemaCreate(CampInstancesCoachesSchemaBase):
	pass



class CampInstancesCoachesSchemaUpdate(CampInstancesCoachesSchemaBase):
	pass



class CampInstancesCoachesSchemaInDBBase(CampInstancesCoachesSchemaBase):

	class Config:
		orm_mode = True



class CampInstancesCoachesSchema(CampInstancesCoachesSchemaInDBBase):
	pass



class CampInstancesCoachesSchemaInDB(CampInstancesCoachesSchemaInDBBase):
	pass


