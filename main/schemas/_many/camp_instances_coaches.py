from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class CampInstancesCoachesSchemaBase(BaseModel):
	pass



class CampInstancesCoachesSchemaCreate(CampInstancesCoachesSchemaBase):
	pass



class CampInstancesCoachesSchemaUpdate(CampInstancesCoachesSchemaBase):
	pass



class CampInstancesCoachesSchemaInDBBase(CampInstancesCoachesSchemaBase):
	id: int

	class Config:
		orm_mode = True



class CampInstancesCoachesSchema(CampInstancesCoachesSchemaInDBBase):
	pass



class CampInstancesCoachesSchemaInDB(CampInstancesCoachesSchemaInDBBase):
	pass


