from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class SpngSurveyCampSchemaBase(BaseModel):
	pass



class SpngSurveyCampSchemaCreate(SpngSurveyCampSchemaBase):
	pass



class SpngSurveyCampSchemaUpdate(SpngSurveyCampSchemaBase):
	pass



class SpngSurveyCampSchemaInDBBase(SpngSurveyCampSchemaBase):
	id: int

	class Config:
		orm_mode = True



class SpngSurveyCampSchema(SpngSurveyCampSchemaInDBBase):
	pass



class SpngSurveyCampSchemaInDB(SpngSurveyCampSchemaInDBBase):
	pass


