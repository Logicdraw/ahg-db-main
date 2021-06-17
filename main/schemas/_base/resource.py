from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class ResourceBaseSchemaBase(BaseModel):
	is_live: Optional[bool] = None
	name: Optional[str] = None
	slug: Optional[str] = None
	thumbnail_image_url: Optional[str] = None
	type: Optional[str] = None
	category_id: Optional[int] = None



class ResourceBaseSchemaCreate(ResourceBaseSchemaBase):
	type: str



class ResourceBaseSchemaUpdate(ResourceBaseSchemaBase):
	pass



class ResourceBaseSchemaInDBBase(ResourceBaseSchemaBase):
	id: int

	class Config:
		orm_mode = True



class ResourceBaseSchema(ResourceBaseSchemaInDBBase):
	pass



class ResourceBaseSchemaInDB(ResourceBaseSchemaInDBBase):
	pass


