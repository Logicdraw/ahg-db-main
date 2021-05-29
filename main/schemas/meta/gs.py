from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class GSMetaSchemaBase(BaseModel):
	pass



class GSMetaSchemaCreate(GSMetaSchemaBase):
	pass



class GSMetaSchemaUpdate(GSMetaSchemaBase):
	pass



class GSMetaSchemaInDBBase(GSMetaSchemaBase):
	id: int

	class Config:
		orm_mode = True



class GSMetaSchema(GSMetaSchemaInDBBase):
	pass



class GSMetaSchemaInDB(GSMetaSchemaInDBBase):
	pass


