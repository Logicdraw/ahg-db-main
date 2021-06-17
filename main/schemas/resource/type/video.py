from typing import Optional

from pydantic import (
	BaseModel,
	EmailStr,
)


from main.schemas._base.resource import (
	ResourceBaseSchemaBase,
	ResourceBaseSchemaCreate,
	ResourceBaseSchemaUpdate,
	ResourceBaseSchemaInDBBase,
	ResourceBaseSchema,
	ResourceBaseSchemaInDB,
)




class ResourceVideoSchemaBase(
	ResourceBaseSchemaBase,
):
	video_url: Optional[str] = None



class ResourceVideoSchemaCreate(
	ResourceVideoSchemaBase,
	ResourceBaseSchemaCreate,
):
	pass



class ResourceVideoSchemaUpdate(
	ResourceVideoSchemaBase,
	ResourceBaseSchemaUpdate,
):
	pass



class ResourceVideoSchemaInDBBase(
	ResourceVideoSchemaBase,
	ResourceBaseSchemaInDBBase,
):
	id: int

	class Config:
		orm_mode = True



class ResourceVideoSchema(
	ResourceVideoSchemaInDBBase,
	ResourceBaseSchema,
):
	pass



class ResourceVideoSchemaInDB(
	ResourceVideoSchemaInDBBase,
	ResourceBaseSchemaInDB,
):
	pass





