from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)





class ResourceCategorySchemaBase(BaseModel):
	is_live: Optional[bool] = None
	name: Optional[str] = None
	slug: Optional[str] = None

	# resources - relationship ???


class ResourceCategorySchemaCreate(ResourceCategorySchemaBase):
	pass



class ResourceCategorySchemaUpdate(ResourceCategorySchemaBase):
	pass



class ResourceCategorySchemaInDBBase(ResourceCategorySchemaBase):
	id: int

	class Config:
		orm_mode = True



class ResourceCategorySchema(ResourceCategorySchemaInDBBase):
	pass



class ResourceCategorySchemaInDB(ResourceCategorySchemaInDBBase):
	pass


