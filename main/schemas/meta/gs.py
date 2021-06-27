from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class GSMetaSchemaBase(BaseModel):
	pass



class GSMetaSchemaCreate(GSMetaSchemaBase):
	access_token: Optional[str] = None



class GSMetaSchemaUpdate(GSMetaSchemaBase):
	access_token: Optional[str] = None



class GSMetaSchemaInDBBase(GSMetaSchemaBase):
	id: int

	class Config:
		orm_mode = True



class GSMetaSchema(GSMetaSchemaInDBBase):
	access_token_encoded: Optional[str] = None



class GSMetaSchemaInDB(GSMetaSchemaInDBBase):
	pass


