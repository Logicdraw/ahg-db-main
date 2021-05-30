from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class SpngMetaSchemaBase(BaseModel):
	access_token_encoded: Optional[str] = None
	refresh_token_encoded: Optional[str] = None



class SpngMetaSchemaCreate(SpngMetaSchemaBase):
	pass
	# access_token ...
	# refresh_token ...



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


