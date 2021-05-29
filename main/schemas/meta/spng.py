from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class SpngMetaSchemaBase(BaseModel):
	pass



class SpngMetaSchemaCreate(SpngMetaSchemaBase):
	pass



class SpngMetaSchemaUpdate(SpngMetaSchemaBase):
	pass



class SpngMetaSchemaInDBBase(SpngMetaSchemaBase):
	id: int

	class Config:
		orm_mode = True



class SpngMetaSchema(SpngMetaSchemaInDBBase):
	pass



class SpngMetaSchemaInDB(SpngMetaSchemaInDBBase):
	pass


