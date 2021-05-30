from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class GSMetaSchemaBase(BaseModel):
	access_token_encoded: Optional[str] = None



class GSMetaSchemaCreate(GSMetaSchemaBase):
	pass
	# access_token ...



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


